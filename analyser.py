def analyze_profile(data):
    from transformers import pipeline
    generator = pipeline("text-generation", model="distilgpt2")

    context = (
        f"User with {data['experience']} experience, skills in {data['tech_stack']}, "
        f"passion: {data['passion']}, answered: {data['ai_answers']}. "
        "Analyze their strengths, weaknesses, and suggest a 3-step career roadmap."
    )

    result = generator(context, max_length=300, num_return_sequences=1)[0]['generated_text']
    lines = result.split('\n')
    roadmap = [line for line in lines if line.strip().startswith("1.") or line.strip().startswith("-")]

    return {
        'summary': result,
        'strengths': [],
        'outdated': [],
        'suggested': [],
        'roadmap': roadmap[:3] if roadmap else [
            "1. Reassess your core strengths and align them with current roles.",
            "2. Learn a modern stack such as React or Python.",
            "3. Work on small projects or freelance to build experience."
        ]
    }
