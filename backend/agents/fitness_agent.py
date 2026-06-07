from services.gemini_service import generate_response


def handle_fitness_query(query: str):

    prompt = f"""
    You are AURA AI's Fitness Coach.

    Create workout plans and fitness recommendations.

    Focus on:
    - Strength training
    - Fat loss
    - Muscle gain
    - Mobility
    - Recovery

    User Query:
    {query}
    """

    return "[FITNESS AGENT]\n\n" + generate_response(prompt)