from transformers import pipeline

# Create a text generation pipeline using the distilgpt2 model
generator = pipeline("text-generation", model="distilgpt2")

def generate_followup_questions(experience, tech_stack, passion):
    prompt = (
        f"A user is unsure about their career. They have {experience} years of experience, "
        f"know {tech_stack}, and are passionate about {passion}. "
        "Generate 3 thoughtful, open-ended questions to better understand their ideal career path."
    )

    result = generator(prompt, max_length=200, num_return_sequences=1)[0]['generated_text']
    lines = result.strip().split('\n')
    questions = [line.strip("1234567890. ") for line in lines if '?' in line]

    if len(questions) < 3:
        questions += [
            "What type of problems do you enjoy solving?",
            "Would you prefer working with people or with technology?",
            "Do you enjoy structured environments or creative freedom?"
        ]
    return questions[:3]
