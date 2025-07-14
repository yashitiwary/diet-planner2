from flask import Flask, render_template, request
from flask_pymongo import PyMongo
from utils.diet_generator import generate_diet

app = Flask(__name__)

# MongoDB config (optional)
app.config["MONGO_URI"] = "mongodb://localhost:27017/diet_planner"
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        age = int(request.form['age'])
        weight = float(request.form['weight'])
        day = request.form['day']  # Add this in your HTML form as well

        # Call with all 3 arguments
        diet_chart = generate_diet(age, weight, day)

        # Optional MongoDB save
        mongo.db.plans.insert_one({
            'age': age,
            'weight': weight,
            'day': day,
            'diet': diet_chart
        })

        return render_template('result.html', diet=diet_chart, age=age, weight=weight, day=day)

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
