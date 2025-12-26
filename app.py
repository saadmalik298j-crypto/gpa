import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="College Placement Readiness Checker",
    page_icon="🎓",
    layout="centered"
)

# SEO Verification
st.markdown(
    """
    <script>
    var meta = document.createElement("meta");
    meta.name = "google-site-verification";
    meta.content = "6ip2TLa4btNdf6cXB4mz7C8Urj3A2oE2DLhwd3kPj0k";
    document.getElementsByTagName("head")[0].appendChild(meta);
    </script>
    """,
    unsafe_allow_html=True
)

# Custom CSS for better aesthetics
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #007bff;
        color: white;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# 1. Intro Section
st.title("🎓 College Placement Readiness Checker")
st.markdown("""
Getting placed in your dream company requires a mix of strong academics, technical skills, and practical experience. 
This tool helps you evaluate where you stand today. 

It's also essential to [check and understand your CGPA](https://cgpahub.com) accurately, as it often acts as the first filter for most companies.
""")

st.divider()

# 2. Input Fields
st.header("Step 1: Your Profile")

col1, col2 = st.columns(2)

with col1:
    cgpa = st.number_input("Your CGPA (out of 10)", min_value=0.0, max_value=10.0, value=7.5, step=0.1)
    projects = st.number_input("Number of Projects Completed", min_value=0, max_value=20, value=2)

with col2:
    skill_level = st.select_slider(
        "Self-rated Technical Skill Level",
        options=["Beginner", "Intermediate", "Advanced"],
        value="Intermediate"
    )

st.divider()

# 3. Logic & Results
st.header("Step 2: Readiness Status")

if st.button("Check My Readiness"):
    # Scoring Logic
    # CGPA Score
    if cgpa >= 8.5: cgpa_score = 3
    elif cgpa >= 7.0: cgpa_score = 2
    else: cgpa_score = 1
    
    # Skill Score
    skill_map = {"Beginner": 1, "Intermediate": 2, "Advanced": 3}
    skill_score = skill_map[skill_level]
    
    # Project Score
    if projects >= 3: project_score = 3
    elif projects >= 1: project_score = 2
    else: project_score = 1
    
    total_score = cgpa_score + skill_score + project_score
    
    # Categorization
    if total_score >= 8:
        status = "Ready"
        color = "green"
        message = "🚀 You are in fantastic shape! Keep polishing your interview skills."
    elif total_score >= 5:
        status = "Intermediate"
        color = "orange"
        message = "📈 You have a solid foundation, but there's room for improvement."
    else:
        status = "Beginner"
        color = "red"
        message = "🌱 You are just starting out. Focus on building core skills and projects."
        
    st.subheader(f"Status: :{color}[{status}]")
    st.info(message)
    
    # 4. Tips Section (Conditional)
    st.divider()
    st.header("Step 3: Improvement Tips")
    
    tips = {
        "Ready": [
            "Start practicing LeetCode (Medium/Hard) regularly.",
            "Refine your behaviorial interview answers (STAR method).",
            "Get your resume reviewed by seniors or professionals."
        ],
        "Intermediate": [
            "Build one 'Capstone' project that solves a real-world problem.",
            "Focus on Data Structures and Algorithms (DSA) basics.",
            "Aim to increase your CGPA if possible in upcoming semesters."
        ],
        "Beginner": [
            "Pick one core language (Python/Java/C++) and master it.",
            "Start your first mini-project (e.g., a Todo app or Personal Site).",
            "Be consistent with your college lectures to maintain a baseline CGPA."
        ]
    }
    
    for tip in tips[status]:
        st.write(f"- {tip}")

# 5. Resources & Chill Zone
st.divider()
st.header("Step 4: Resources & Balance")
st.markdown("""
Maintaining a healthy work-life balance is crucial during placement season. 
- For extra study materials and guides, visit these [useful links](https://shadowfight2.site/useful-links).
- Remember to take short breaks to recharge. Some students enjoy a quick [gaming session](https://hungrysharkevolutionmod.com) to stay fresh and avoid burnout.
""")

# 6. Disclaimer
st.divider()
st.caption("Disclaimer: This tool is for informational purposes only. Placement success depends on various factors including market conditions, communication skills, and individual company requirements.")
