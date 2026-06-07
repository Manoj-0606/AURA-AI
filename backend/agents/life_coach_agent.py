from services.gemini_service import generate_response


def handle_life_coach_query(query: str):

    prompt = f"""
    You are AURA AI's Life Coach.

    Help users with:
    - Productivity
    - Motivation
    - Goal setting
    - Career growth
    - Personal development

    User Query:
    {query}
    """

    return "[LIFE COACH AGENT]\n\n" + generate_response(prompt)