from rag.rag_pipeline import search_knowledge

from agents.diet_agent import handle_diet_query
from agents.fitness_agent import handle_fitness_query
from agents.health_agent import handle_health_query
from agents.life_coach_agent import handle_life_coach_query

from memory.user_memory import (
    save_name,
    get_name,
    save_age,
    get_age,
    save_weight,
    get_weight,
    save_height,
    get_height,
    save_goal,
    get_goal,
    save_diet_type,
    get_diet_type,
    save_activity_level,
    get_activity_level,
    get_profile
)
from utils.health_calculator import (
    calculate_bmi,
    fat_loss_calories,
    protein_requirement
)

from memory.progress_memory import (
    add_workout,
    get_workouts
)

def route_query(query):

    query_lower = query.lower()

    # ----------------------------
    # NAME MEMORY
    # ----------------------------

    if "my name is" in query_lower:

        name = query.split("is")[-1].strip()

        save_name(name)

        return f"Nice to meet you {name}. I will remember your name."

    if "what is my name" in query_lower:

        return f"Your name is {get_name()}"

    # ----------------------------
    # AGE MEMORY
    # ----------------------------

    if "i am" in query_lower and "years old" in query_lower:

        age = query_lower.replace("i am", "").replace("years old", "").strip()

        save_age(age)

        return f"Got it. Your age is {age}"

    if "what is my age" in query_lower:

        return f"Your age is {get_age()}"

    # ----------------------------
    # WEIGHT MEMORY
    # ----------------------------

    if "my weight is" in query_lower:

        weight = query.split("is")[-1].strip()

        save_weight(weight)

        return f"Got it. Your weight is {weight}"

    if "what is my weight" in query_lower:

        return f"Your weight is {get_weight()}"

    # ----------------------------
    # HEIGHT MEMORY
    # ----------------------------

    if "my height is" in query_lower:

        height = query.split("is")[-1].strip()

        save_height(height)

        return f"Height saved: {height}"

    if "what is my height" in query_lower:

        return f"Your height is {get_height()}"

    # ----------------------------
    # GOAL MEMORY
    # ----------------------------

    if "my goal is" in query_lower:

        goal = query.split("is")[-1].strip()

        save_goal(goal)

        return f"Goal saved: {goal}"

    if "what is my goal" in query_lower:

        return f"Your goal is {get_goal()}"

    # ----------------------------
    # DIET TYPE MEMORY
    # ----------------------------

    if "i am vegetarian" in query_lower:

        save_diet_type("Vegetarian")

        return "Diet type saved: Vegetarian"

    if "i am non vegetarian" in query_lower:

        save_diet_type("Non-Vegetarian")

        return "Diet type saved: Non-Vegetarian"

    if "what is my diet type" in query_lower:

        return f"Your diet type is {get_diet_type()}"

    # ----------------------------
    # ACTIVITY LEVEL MEMORY
    # ----------------------------

    if "i am moderately active" in query_lower:

        save_activity_level("Moderately Active")

        return "Activity level saved: Moderately Active"

    if "i am active" in query_lower:

        save_activity_level("Active")

        return "Activity level saved: Active"

    if "what is my activity level" in query_lower:

        return f"Your activity level is {get_activity_level()}"

    # ----------------------------
    # PROFILE SUMMARY
    # ----------------------------

    if (
        "what do you know about me" in query_lower
        or "show my profile" in query_lower
    ):

        profile = get_profile()

        return f"""
Name: {profile['name']}
Age: {profile['age']}
Weight: {profile['weight']}
Height: {profile['height']}
Goal: {profile['goal']}
Diet Type: {profile['diet_type']}
Activity Level: {profile['activity_level']}
"""

    # ----------------------------
    # HEALTH CALCULATORS
    # ----------------------------

    if "calculate my bmi" in query_lower:

        weight = get_weight()
        height = get_height()

        if not weight or not height:
            return "Please save your weight and height first."

        bmi = calculate_bmi(
            weight.replace("kg", "").strip(),
            height.replace("cm", "").strip()
        )

        return f"Your BMI is {bmi}"


    if "calculate my calories" in query_lower:

        weight = get_weight()

        if not weight:
            return "Please save your weight first."

        maintenance, fat_loss = fat_loss_calories(
            weight.replace("kg", "").strip()
        )

        return f"""
Maintenance Calories: {maintenance}

Fat Loss Calories: {fat_loss}
"""


    if "protein requirement" in query_lower:

        weight = get_weight()

        if not weight:
            return "Please save your weight first."

        protein = protein_requirement(
            weight.replace("kg", "").strip()
        )

        return f"""
Daily Protein Target:

{protein} grams
"""

        # ----------------------------
        # PROGRESS TRACKER
        # ----------------------------

    if "i completed my workout" in query_lower:

        total = add_workout()

        return f"""
    Workout logged successfully.

    Total Workouts Completed: {total}
    """


    if "show my progress" in query_lower:

        profile = get_profile()

        workouts = get_workouts()

        return f"""
    Name: {profile['name']}
    Goal: {profile['goal']}

    Workouts Completed: {workouts}
    """


    # ----------------------------
    # RAG KNOWLEDGE SEARCH
    # ----------------------------

    knowledge = search_knowledge(query)

    enhanced_query = f"""
Knowledge Base Context:

{knowledge}

User Question:

{query}
"""

    # ----------------------------
    # AGENT ROUTING
    # ----------------------------

    if any(word in query_lower for word in [
        "diet",
        "nutrition",
        "food",
        "meal",
        "protein",
        "weight loss"
    ]):

        return handle_diet_query(enhanced_query)

    elif any(word in query_lower for word in [
        "gym",
        "fitness",
        "exercise",
        "workout",
        "muscle",
        "training"
    ]):

        return handle_fitness_query(enhanced_query)

    elif any(word in query_lower for word in [
        "health",
        "fever",
        "headache",
        "cold",
        "pain",
        "symptom"
    ]):

        return handle_health_query(enhanced_query)

    else:

        return handle_life_coach_query(enhanced_query)