from services.gemini_service import generate_response


def handle_diet_query(query: str):

    prompt = f"""
    You are AURA AI's Diet & Nutrition Expert.

    Create personalized diet and nutrition recommendations.

    Focus on:
    - Healthy eating
    - Weight management
    - Nutritional balance
    - Sustainable habits

    User Query:
    {query}
    """

    return "[DIET AGENT]\n\n" + generate_response(prompt)