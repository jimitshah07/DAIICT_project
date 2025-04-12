from django.shortcuts import render
from .utils.career_data import career_map, career_responses,career_details
from .forms import SkillTestForm
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from weasyprint import HTML
from django.template.loader import render_to_string
from django.http import HttpResponse
career_map = {
    "programming": "Software Developer",
    "data": "Data Scientist",
    "marketing": "Digital Marketer",
    "design": "UI/UX Designer",
    "management": "Product Manager",
    "finance": "Financial Analyst",
    "hr": "Human Resources Manager",
    "sales": "Sales Representative",
    "education": "Teacher",
    "healthcare": "Registered Nurse",
}

career_responses = {
    "Software Developer": "You can start by learning Python, Django, and Git. Build projects and practice coding interviews. Explore data structures and algorithms.",
    "Data Scientist": "You should focus on Python, Statistics, Pandas, and Machine Learning. Projects and Kaggle help a lot. Deep learning frameworks like TensorFlow and PyTorch are also valuable.",
    "Digital Marketer": "Learn about SEO, SEM, content strategy, social media marketing, and analytics tools like Google Analytics. Understanding customer behavior is key.",
    "UI/UX Designer": "Start with Figma, Adobe XD, design thinking, usability principles, and user research methodologies. Build a strong portfolio.",
    "Product Manager": "Understand agile, roadmapping, stakeholder communication, market research, and tools like Jira or Trello. Focus on understanding user needs and business goals.",
    "Financial Analyst": "Develop skills in financial modeling, forecasting, valuation, and understanding financial statements. Learn tools like Excel and potentially statistical software.",
    "Human Resources Manager": "Learn about talent acquisition, employee relations, compensation and benefits, HR policies, and employment law.",
    "Sales Representative": "Focus on communication, negotiation, product knowledge, customer relationship management (CRM) tools, and understanding sales cycles.",
    "Teacher": "Develop strong communication, curriculum development, classroom management, and student assessment skills. Obtain relevant certifications.",
    "Registered Nurse": "Focus on anatomy, physiology, patient care, medication administration, and emergency response. Obtain nursing licenses and certifications.",
}

career_details = {
    "Data Scientist": {
        "skills": ['Python', 'Pandas', 'Scikit-learn', 'Statistics', 'Machine Learning', 'Deep Learning', 'SQL'],
        "interview_questions": [
            'What is overfitting?',
            'Difference between supervised and unsupervised learning?',
            'Explain a confusion matrix.',
            'What is a p-value?',
            'How would you handle missing data?',
            'Explain the bias-variance tradeoff.',
            'Describe different evaluation metrics for classification and regression.'
        ],
        "aptitude_tests": [
            {'question': 'Mean of [2, 4, 6] is?', 'options': ['4', '5', '6'], 'correct_answer': '4'},
            {'question': 'Output of 2**3?', 'options': ['6', '8', '9'], 'correct_answer': '8'},
            {'question': 'Median of [1, 5, 2, 8, 3] is?', 'options': ['2', '3', '5'], 'correct_answer': '3'}
        ],
        "resume_template": "Skills: Python, Pandas, Scikit-learn, Machine Learning\nProjects: Sales Predictor (Regression), Customer Churn Prediction (Classification)\nExperience: Data Co - Junior Analyst (1 year), Research Assistant (6 months)\nEducation: Master's in Data Science\nCertifications: Google Data Analytics Professional Certificate",
        "typical_salary_range": "$80,000 - $150,000 USD per year",
        "career_pathway": ["Data Analyst", "Senior Data Scientist", "Lead Data Scientist", "Director of Data Science"],
        "related_resources": ["Kaggle", "Coursera (Data Science Specialization)", "Towards Data Science (Medium)"],
        "job_outlook": "Excellent - high demand and growth"
    },
    "Software Developer": {
        "skills": ["Python", "Django", "Git", "JavaScript", "React", "SQL"],
        "interview_questions": ["Explain OOP.", "What is a REST API?", "Difference between list and tuple?", "What is Git used for?", "Explain the concept of asynchronous programming.", "What are design patterns?"],
        "aptitude_tests": [
            {"question": "5 + 3 =", "options": ["7", "8", "9"], "correct_answer": "8"},
            {"question": "Result of 10 // 3?", "options": ["3", "3.3", "4"], "correct_answer": "3"},
            {"question": "What is the output of len('hello')?", "options": ["4", "5", "6"], "correct_answer": "5"}
        ],
        "resume_template": "Skills: Python, Django, JavaScript, React, Git\nProjects: Blog App (Full-stack), E-commerce Platform (Frontend)\nExperience: Dev Co - Intern (1 year), Freelance Web Developer (6 months)\nEducation: Bachelor's in Computer Science\nCertifications: AWS Certified Developer - Associate",
        "typical_salary_range": "$70,000 - $140,000 USD per year",
        "career_pathway": ["Junior Developer", "Mid-Level Developer", "Senior Developer", "Tech Lead", "Engineering Manager"],
        "related_resources": ["LeetCode", "freeCodeCamp", "Stack Overflow"],
        "job_outlook": "Excellent - consistently high demand"
    },
    "Financial Analyst": {
        "skills": ["Financial Modeling", "Valuation", "Forecasting", "Excel", "Financial Statements Analysis", "Bloomberg Terminal (Optional)"],
        "interview_questions": ["Walk me through a DCF.", "What are the three main financial statements?", "How do you value a company?", "Explain the concept of WACC.", "What is beta in finance?"],
        "aptitude_tests": [
            {"question": "What is 10% of 500?", "options": ["40", "50", "60"], "correct_answer": "50"},
            {"question": "If revenue grows by 5% annually, what will be the revenue in year 3 if year 1 revenue is $100?", "options": ["$110.25", "$115.76", "$121.55"], "correct_answer": "$115.76"}
        ],
        "resume_template": "Skills: Financial Modeling, Valuation, Forecasting, Excel\nExperience: Finance Firm - Analyst Intern (1 year)\nEducation: Bachelor's in Finance\nCertifications: CFA Level 1 (Pursuing)",
        "typical_salary_range": "$65,000 - $120,000 USD per year",
        "career_pathway": ["Junior Analyst", "Analyst", "Senior Analyst", "Portfolio Manager", "Investment Banker"],
        "related_resources": ["Investopedia", "Wall Street Prep", "CFA Institute"],
        "job_outlook": "Good - stable demand in the financial sector"
    },
    "Human Resources Manager": {
        "skills": ["Talent Acquisition", "Employee Relations", "Compensation & Benefits", "HR Policies", "Employment Law", "Performance Management"],
        "interview_questions": ["Describe your experience with conflict resolution.", "How do you handle a difficult employee?", "What are your strategies for talent acquisition?", "Explain key employment laws.", "How do you develop a compensation strategy?"],
        "aptitude_tests": [
            {"question": "Which of the following is NOT a function of HR?", "options": ["Recruitment", "Marketing", "Training"], "correct_answer": "Marketing"},
            {"question": "What does 'EEO' stand for?", "options": ["Equal Employment Opportunity", "Employee Engagement Outcome", "Executive Ethical Obligation"], "correct_answer": "Equal Employment Opportunity"}
        ],
        "resume_template": "Skills: Talent Acquisition, Employee Relations, HR Policies\nExperience: HR Dept - HR Coordinator (2 years)\nEducation: Bachelor's in Human Resources\nCertifications: SHRM-CP",
        "typical_salary_range": "$70,000 - $130,000 USD per year",
        "career_pathway": ["HR Generalist", "HR Manager", "HR Director", "VP of Human Resources"],
        "related_resources": ["SHRM (Society for Human Resource Management)", "HR Dive"],
        "job_outlook": "Good - essential role in all organizations"
    },
    "Sales Representative": {
        "skills": ["Communication", "Negotiation", "Product Knowledge", "CRM Software", "Lead Generation", "Closing Deals"],
        "interview_questions": ["Tell me about a time you closed a difficult sale.", "How do you handle rejection?", "What is your sales process?", "How do you build rapport with clients?", "Why are you interested in sales?"],
        "aptitude_tests": [
            {"question": "If a product costs $20 and has a 20% discount, what is the sale price?", "options": ["$15", "$16", "$18"], "correct_answer": "$16"},
            {"question": "A salesperson makes a 5% commission on a $1000 sale. What is their commission?", "options": ["$40", "$50", "$60"], "correct_answer": "$50"}
        ],
        "resume_template": "Skills: Communication, Negotiation, CRM (Salesforce)\nExperience: Retail Co - Sales Associate (1.5 years)\nEducation: Bachelor's in Business Administration",
        "typical_salary_range": "$40,000 - $100,000+ USD per year (base + commission)",
        "career_pathway": ["Sales Representative", "Senior Sales Representative", "Sales Manager", "Director of Sales"],
        "related_resources": ["HubSpot Sales Blog", "Sales Hacker"],
        "job_outlook": "Good - always demand for effective sales professionals"
    },
    "Teacher": {
        "skills": ["Communication", "Curriculum Development", "Classroom Management", "Student Assessment", "Patience", "Empathy"],
        "interview_questions": ["What is your teaching philosophy?", "How do you handle disruptive students?", "How do you assess student learning?", "How do you differentiate instruction?", "Why did you decide to become a teacher?"],
        "aptitude_tests": [
            {"question": "Which of the following is a primary goal of education?", "options": ["Entertainment", "Knowledge Acquisition", "Socialization"], "correct_answer": "Knowledge Acquisition"},
            {"question": "What is a key element of effective classroom management?", "options": ["Strict punishment", "Clear expectations", "Ignoring misbehavior"], "correct_answer": "Clear expectations"}
        ],
        "resume_template": "Skills: Curriculum Development, Classroom Management, Student Assessment\nExperience: School Name - Student Teacher (1 year)\nEducation: Bachelor's in Education\nCertifications: State Teaching License",
        "typical_salary_range": "$40,000 - $80,000 USD per year (varies by location and experience)",
        "career_pathway": ["Teacher", "Senior Teacher", "Department Head", "Principal", "Curriculum Developer"],
        "related_resources": ["Edutopia", "ASCD (Association for Supervision and Curriculum Development)"],
        "job_outlook": "Stable - consistent need for educators"
    },
    "Registered Nurse": {
        "skills": ["Patient Care", "Medication Administration", "Vital Signs Monitoring", "Electronic Health Records (EHR)", "Communication", "Critical Thinking"],
        "interview_questions": ["Why did you choose nursing as a career?", "How do you handle stressful situations?", "Describe a time you made a mistake in patient care.", "How do you ensure patient safety?", "What are your strengths as a nurse?"],
        "aptitude_tests": [
            {"question": "What is the normal range for adult blood pressure?", "options": ["90/60 to 120/80", "140/90 to 160/100", "120/100 to 140/120"], "correct_answer": "90/60 to 120/80"},
            {"question": "What is the abbreviation for 'by mouth' when administering medication?", "options": ["IV", "IM", "PO"], "correct_answer": "PO"}
        ],
        "resume_template": "Skills: Patient Care, Medication Administration, EHR (Epic)\nExperience: Hospital Name - Nursing Assistant (1 year)\nEducation: Bachelor of Science in Nursing (BSN)\nCertifications: Registered Nurse (RN) License",
        "typical_salary_range": "$60,000 - $100,000+ USD per year (varies by location and specialization)",
        "career_pathway": ["Staff Nurse", "Charge Nurse", "Nurse Practitioner", "Nurse Manager"],
        "related_resources": ["American Nurses Association (ANA)", "Nursing Times"],
        "job_outlook": "Excellent - high demand in the healthcare industry"
    }
}

def chatbot_view(request):
    context = {}
    if request.method == "POST":
        user_input = request.POST.get("message", "").lower()
        detected_career = None

        for keyword, career in career_map.items():
            if keyword in user_input:
                detected_career = career
                break

        if detected_career:
            response = career_responses.get(detected_career, "Here are some tips to get started.")
            details = career_details.get(detected_career, {})
            context = {
                "career_name": detected_career,
                "response": response,
                "skills": details.get("skills", []),
                "interview_questions": details.get("interview_questions", []),
                "aptitude_tests": details.get("aptitude_tests", []),
                "resume_template": details.get("resume_template", "")
            }
        else:
            context["response"] = "Sorry, I couldn't understand your interest. Try saying something like 'I like programming' or 'I want to get into data science'."
    import pprint
    pprint.pprint(context)
    return render(request, "chatbot.html", context)

def generate_resume_pdf(request):
    if request.method == "POST":
        template_name = request.POST.get("template")
        user_data = {
            "name": request.POST.get("name"),
            "email": request.POST.get("email"),
            "skills": request.POST.get("skills"),
            "experience": request.POST.get("experience"),
        }
        html = render_to_string(f"resumes/{template_name}.html", user_data)
        pdf_file = HTML(string=html).write_pdf()
        response = HttpResponse(pdf_file, content_type="application/pdf")
        response["Content-Disposition"] = "attachment; filename=resume.pdf"
        return response

TEMPLATE_CHOICES = [
    {"id": "template1", "name": "Modern", "image": "/static/resume_previews/model.png"},
    {"id": "template2", "name": "Classic", "image": "/static/resume_previews/class.png"},
    {"id": "template3", "name": "Minimalist", "image": "/static/resume_previews/minimalist.png"},
    {"id": "template4", "name": "Elegant", "image": "/static/resume_previews/elegant.png"},
    {"id": "template5", "name": "Bold", "image": "/static/resume_previews/bol.png"},
]

def resume_form_view(request):
    if request.method == "POST":
        data = {
            "name": request.POST.get("name"),
            "email": request.POST.get("email"),
            "phone": request.POST.get("phone"),
            "summary": request.POST.get("summary"),
            "linkedin": request.POST.get("linkedin"),
            "github": request.POST.get("github"),
            "skills": request.POST.get("skills").split(','),
            "experience": request.POST.get("experience").split(','),
        }
        template_id = request.POST.get("template")

        # Match with the selected template
        valid_ids = [t["id"] for t in TEMPLATE_CHOICES]
        if template_id not in valid_ids:
            return HttpResponse("Invalid template selected", status=400)

        html = render_to_string(f"resumes/{template_id}.html", data)
        pdf = HTML(string=html).write_pdf()

        response = HttpResponse(pdf, content_type="application/pdf")
        response["Content-Disposition"] = "attachment; filename=resume.pdf"
        return response

    return render(request, "resume_form.html", {"templates": TEMPLATE_CHOICES})


# def generate_resume_pdf(request):
#     if request.method == "POST":
#         html = render_to_string("resume_template.html", {"user_data": request.POST})
#         pdf_file = HTML(string=html).write_pdf()
#         response = HttpResponse(pdf_file, content_type="application/pdf")
#         response["Content-Disposition"] = "attachment; filename=resume.pdf"
#         return response
#     return HttpResponse("Only POST method is allowed.")

def skill_llm(user_input):
    return f"(LLM Response) Based on your input: {user_input}, you may be good at Python or Data Analysis."

def career_llm(user_input):
    return f"(LLM Response) A great path for you could be Full-Stack Web Development or Data Science."

def resume_llm(user_input):
    return f"(LLM Response) Here's a suggested resume structure tailored to: {user_input}."


def smart_advice_view(request):
    if request.method == "POST":
        user_input = request.POST.get("message")
        skill_result = skill_llm.analyze(user_input)
        career_options = career_llm.recommend(skill_result)
        resume_tips = resume_llm.suggest(career_options[0])
        return JsonResponse({
            "skills": skill_result,
            "careers": career_options,
            "resume_tips": resume_tips,
        })


def download_resume_pdf(request, career):
    resume = resume_templates.get(career)
    if not resume:
        return HttpResponse("Invalid career", status=404)

    template = get_template("resume_pdf.html")
    html = template.render({"career": career, "resume": resume})

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{career}_resume.pdf"'

    pisa.CreatePDF(html, dest=response)
    return response


def skill_test_view(request):
    career = None
    resume = None
    form = SkillTestForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        interest = form.cleaned_data['interest'].lower()
        detected = None
        for keyword, c in career_map.items():
            if keyword in interest:
                detected = c
                break
        if detected:
              #career = detected 
            career = request.POST.get('career_name')  # or however you're passing the detected career
            details = career_details.get(career, {})
            resume = details.get('resume_template', 'No resume found.')

    return render(request, "skill_test.html", {"form": form, "career": career, "resume": resume})

# Modify chatbot_view in views.py
# def chatbot_view(request):
#     response = None
#     if request.method == "POST":
#         user_input = request.POST.get("message", "").lower()
#         detected = None
#         for keyword, career in career_map.items():
#             if keyword in user_input:
#                 detected = career
#                 break
#         if detected:
#             response = career_responses.get(detected)
#         else:
#             response = "You can ask about careers like software development, data science, design, marketing, or management. I’ll give you guidance based on that!"
#     return render(request, "chatbot.html", {"response": response})

def resource_view(request):
    resume_templates = {
        "Software Engineer": "/static/resumes/software_engineer_template.pdf",
        "Data Scientist": "/static/resumes/data_scientist_template.pdf",
        "Product Manager": "/static/resumes/product_manager_template.pdf",
    }

    sample_questions = {
        "Software Engineer": [
            "What is polymorphism in OOP?",
            "Explain the difference between TCP and UDP.",
            "Describe a RESTful API."
        ],
        "Data Scientist": [
            "What is the difference between supervised and unsupervised learning?",
            "Explain how a decision tree works.",
            "What is p-value?"
        ],
        "Product Manager": [
            "How do you prioritize features?",
            "Describe a time you resolved a conflict between stakeholders.",
            "What’s your approach to writing user stories?"
        ],
    }

    career = request.GET.get("career", "Software Engineer")
    resume_url = resume_templates.get(career)
    questions = sample_questions.get(career, [])

    return render(request, "resources.html", {
        "career": career,
        "resume_url": resume_url,
        "questions": questions,
        "career_list": resume_templates.keys(),
    })


def resources_view(request):
    sample_questions = {
        "Software Developer": [
            "What is the difference between a list and a tuple in Python?",
            "Explain the MVC architecture.",
            "What is a REST API?"
        ],
        "Data Scientist": [
            "How do you handle missing data?",
            "What is the difference between classification and regression?",
            "Explain overfitting and underfitting."
        ],
        "UI/UX Designer": [
            "How do you approach user research?",
            "What tools do you use for prototyping?",
            "Explain the concept of accessibility in design."
        ],
        "Product Manager": [
            "How do you prioritize features?",
            "Describe your experience working with cross-functional teams.",
            "What’s your approach to managing product roadmap?"
        ],
        "Digital Marketer": [
            "What KPIs do you track for a campaign?",
            "How do you run A/B testing?",
            "Explain the concept of CTR and CPC."
        ]
    }
    return render(request, "resources.html", {
        "resume_templates": resume_templates,
        "sample_questions": sample_questions,
    })
