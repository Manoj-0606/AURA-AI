from rag.rag_pipeline import search_knowledge

from agents.diet_agent import handle_diet_query
from agents.fitness_agent import handle_fitness_query
from agents.health_agent import handle_health_query
from agents.life_coach_agent import handle_life_coach_query

from memory.user_memory import (
    save_name,
    get_name,
    save_weight,
    get_weight,
    save_goal,
    get_goal
)


def route_query(query):

    query_lower = query.lower()

    # ----------------------------
    # MEMORY
    # ----------------------------

    if "my name is" in query_lower:
        name = query.split("is")[-1].strip()
        save_name(name)
        return f"Nice to meet you {name}. I will remember your name."

    if "what is my name" in query_lower:
        name = get_name()
        return f"Your name is {name}"

    if "my weight is" in query_lower:
        weight = query.split("is")[-1].strip()
        save_weight(weight)
        return f"Got it. Your weight is {weight}"

    if "what is my weight" in query_lower:
        return f"Your weight is {get_weight()}"

    if "my goal is" in query_lower:
        goal = query.split("is")[-1].strip()
        save_goal(goal)
        return f"Goal saved: {goal}"

    if "what is my goal" in query_lower:
        return f"Your goal is {get_goal()}"

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
        "weight loss",
        "protein"
    ]):
        return handle_diet_query(enhanced_query)

    elif any(word in query_lower for word in [
        "workout",
        "gym",
        "fitness",
        "exercise",
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