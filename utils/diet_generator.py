# utils/diet_generator.py

def generate_diet(age, weight, day):
    # Example logic: Add vegetarian on Tue/Thu/Sat
    vegetarian_days = ["Tuesday", "Thursday", "Saturday"]
    is_veg = day in vegetarian_days

    plan = []

    if weight < 50:
        plan.append("Breakfast: Banana smoothie and toast")
        plan.append("Lunch: Rice, dal, and vegetables")
        plan.append("Dinner: Khichdi and curd")
    elif weight < 70:
        plan.append("Breakfast: Poha and boiled eggs")
        plan.append("Lunch: Roti, sabzi, and paneer")
        plan.append("Dinner: Brown rice and vegetable curry")
    else:
        plan.append("Breakfast: Oats with fruits")
        plan.append("Lunch: Grilled chicken and quinoa salad")
        plan.append("Dinner: Soup and multigrain bread")

    if is_veg:
        plan.append("Note: Today is a vegetarian day.")

    return plan
