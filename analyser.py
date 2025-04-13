def analyze_profile(data):
    passion = data.get('passion', '').lower()
    tech_stack = [tech.lower() for tech in data.get('tech_stack', [])]

    strengths = []
    outdated = []
    suggested = []
    roadmap = []

    # Detect strengths and outdated tech
    for tech in tech_stack:
        if tech in ['python', 'django', 'react', 'html', 'css', 'javascript', 'flask', 'node.js', 'fastapi']:
            strengths.append(tech.title())
        elif tech in ['php', 'jquery', 'asp.net']:
            outdated.append(tech.title())

    # Suggestions for outdated tech
    if 'php' in tech_stack or 'jquery' in tech_stack or 'asp.net' in tech_stack:
        suggested.extend(['FastAPI', 'Next.js', 'Tailwind CSS'])

    # Define multiple tech-specific roadmaps
    roadmaps = {
        "frontend": [
            "1. Master HTML, CSS, JavaScript fundamentals.",
            "2. Learn modern frameworks like React and Tailwind CSS.",
            "3. Build interactive projects (portfolios, dashboards, etc.).",
            "4. Explore state management with Redux or Context API.",
            "5. Get familiar with responsive design and accessibility.",
            "6. Contribute to frontend open source projects."
        ],
        "backend": [
            "1. Deepen Python skills and OOP concepts.",
            "2. Learn Django REST Framework for APIs.",
            "3. Integrate databases like PostgreSQL and Redis.",
            "4. Study authentication, JWT, and deployment practices.",
            "5. Build full-stack apps with Django + React.",
            "6. Learn DevOps basics for production deployment."
        ],
        "cybersecurity": [
            "1. Learn core security concepts (CIA triad, threat modeling).",
            "2. Practice using tools like Wireshark, Burp Suite, and Nmap.",
            "3. Get familiar with Linux, networking, and OS fundamentals.",
            "4. Earn certifications like CompTIA Security+ or CEH.",
            "5. Build a GitHub repo of solved CTF challenges.",
            "6. Apply for security internships or bug bounty platforms."
        ],
        "data_science": [
            "1. Learn Python for Data Science (NumPy, Pandas).",
            "2. Master data visualization (Matplotlib, Seaborn).",
            "3. Practice on real-world datasets (Kaggle, UCI).",
            "4. Learn ML concepts and Scikit-learn.",
            "5. Build projects: predictions, clustering, recommender systems.",
            "6. Explore TensorFlow, PyTorch for deep learning."
        ],
        "devops": [
            "1. Learn Linux shell scripting and system basics.",
            "2. Understand Git, version control, and CI/CD pipelines.",
            "3. Learn Docker and containerization.",
            "4. Explore Kubernetes and orchestration tools.",
            "5. Get hands-on with AWS, Azure, or GCP.",
            "6. Setup logging, monitoring, and alerting systems.",
            "7. Earn certifications like AWS Certified DevOps Engineer."
        ],
        "mobile": [
            "1. Choose your stack: Flutter, React Native, Kotlin, or Swift.",
            "2. Learn UI/UX principles for mobile apps.",
            "3. Build simple apps like to-do, weather, or calculator.",
            "4. Handle local storage, state, and networking.",
            "5. Publish your first app on Play Store or App Store.",
            "6. Learn animations and native APIs.",
            "7. Practice testing and debugging on simulators/emulators."
        ],
        "blockchain": [
            "1. Learn basic blockchain and Ethereum fundamentals.",
            "2. Write and deploy smart contracts with Solidity.",
            "3. Use tools like Remix, Hardhat, or Truffle.",
            "4. Build DApps using Web3.js or Ethers.js.",
            "5. Learn Metamask, Polygon, and testnets.",
            "6. Understand gas optimization and contract security.",
            "7. Contribute to DAOs or open-source blockchain projects."
        ],
        "ai_research": [
            "1. Learn Python + Math (Linear Algebra, Stats, Calc).",
            "2. Master ML theory: regression, SVM, trees, clustering.",
            "3. Deep dive into deep learning with PyTorch or TensorFlow.",
            "4. Read top AI papers (ArXiv, Google Scholar).",
            "5. Reproduce research papers using GitHub code.",
            "6. Learn about transformer models (BERT, GPT).",
            "7. Contribute to open-source AI repos or write your own."
        ],
        "game_dev": [
            "1. Choose a game engine: Unity (C#) or Unreal (C++).",
            "2. Learn 2D/3D game mechanics and physics.",
            "3. Practice level design and animation basics.",
            "4. Build small games like platformers or puzzles.",
            "5. Study game loops, assets, and audio integration.",
            "6. Participate in game jams like Ludum Dare.",
            "7. Publish games on itch.io or Steam for feedback."
        ]
    }

    # Match passion or tech keywords to roadmap
    for key in roadmaps:
        if key in passion:
            roadmap = roadmaps[key]
            break
    else:
        if 'react' in tech_stack:
            roadmap = roadmaps['frontend']
        elif 'django' in tech_stack or 'node.js' in tech_stack or 'fastapi' in tech_stack:
            roadmap = roadmaps['backend']
        elif 'solidity' in tech_stack or 'blockchain' in passion:
            roadmap = roadmaps['blockchain']
        elif 'pytorch' in tech_stack or 'tensorflow' in tech_stack:
            roadmap = roadmaps['ai_research']
        elif 'flutter' in tech_stack or 'kotlin' in tech_stack:
            roadmap = roadmaps['mobile']
        elif not roadmap:
            roadmap = [
                "1. Identify your interest area more specifically.",
                "2. Explore online resources and communities.",
                "3. Take a beginner-friendly course to get started.",
                "4. Build small practice projects in that direction.",
                "5. Connect with professionals in that field.",
                "6. Apply learnings to internships or freelance gigs."
            ]

    return {
        'summary': 'Analyzed based on your input profile.',
        'strengths': strengths,
        'outdated': outdated,
        'suggested': suggested,
        'roadmap': roadmap
    }
