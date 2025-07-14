from flask import Flask, render_template, request
from flask_pymongo import PyMongo
from utils.diet_generator import generate_diet
import os

app = Flask(__name__)

# ✅ Smart MONGO_URI: Use environment variable if set, else use Atlas URI fallback
app.config["MONGO_URI"] = os.environ.get("MONGO_URI") or "mongodb+srv://yashitiwary:9838yashi@cluster0.r5x2deh.mongodb.net/diet_planner?retryWrites=true&w=majority"
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev")

mongo = PyMongo(app)  # Initialize MongoDB

# ✅ Home Page
@app.route('/')
def index():
    return render_template('index.html')

# ✅ Handle Form Submission
@app.route('/generate', methods=['POST'])
def generate():
    try:
        age = int(request.form['age'])
        weight = float(request.form['weight'])
        day = request.form['day']

        # Generate the diet plan
        diet_chart = generate_diet(age, weight, day)

        # Save to MongoDB
        mongo.db.plans.insert_one({
            'age': age,
            'weight': weight,
            'day': day,
            'diet': diet_chart
        })

        return render_template('result.html', diet=diet_chart, age=age, weight=weight, day=day)

    except Exception as e:
        return f"Error: {str(e)}"

# ✅ Run App (works locally and on Render)
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Render sets this automatically
    app.run(host='0.0.0.0', port=port)
