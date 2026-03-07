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

# Custom CSS
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
    internships = st.number_input("Number of Internships / Industry Experience", min_value=0, max_value=10, value=0)

with col2:
    skill_level = st.select_slider(
        "Self-rated Technical Skill Level",
        options=["Beginner", "Intermediate", "Advanced"],
        value="Intermediate"
    )
    backlogs = st.radio(
        "Do you have any active backlogs/arrears?",
        options=["No", "Yes"],
        index=0
    )

# CGPA zero warning
if cgpa == 0.0:
    st.warning("⚠️ CGPA is set to 0.0. Please enter your actual CGPA before checking readiness.")

st.divider()

# 3. Logic & Results
st.header("Step 2: Readiness Status")

if st.button("Check My Readiness"):

    # Block if active backlogs
    if backlogs == "Yes":
        st.error("🚫 Many companies filter out candidates with active backlogs. Clear your arrears before applying. You can still build your skills in the meantime!")
    else:
        # CGPA Score (max 3)
        if cgpa >= 8.5:
            cgpa_score = 3
        elif cgpa >= 7.0:
            cgpa_score = 2
        else:
            cgpa_score = 1

        # Skill Score (max 3)
        skill_map = {"Beginner": 1, "Intermediate": 2, "Advanced": 3}
        skill_score = skill_map[skill_level]

        # Project Score (max 3)
        if projects >= 3:
            project_score = 3
        elif projects >= 1:
            project_score = 2
        else:
            project_score = 1

        # Internship Score (max 2)
        if internships >= 2:
            internship_score = 2
        elif internships == 1:
            internship_score = 1
        else:
            internship_score = 0

        total_score = cgpa_score + skill_score + project_score + internship_score
        max_score = 11  # 3 + 3 + 3 + 2

        # Categorization based on percentage of max score
        pct = total_score / max_score

        if pct >= 0.75:
            status = "Ready"
            color = "green"
            message = "🚀 You are in fantastic shape! Keep polishing your interview skills."
        elif pct >= 0.45:
            status = "Intermediate"
            color = "orange"
            message = "📈 You have a solid foundation, but there's room for improvement."
        else:
            status = "Beginner"
            color = "red"
            message = "🌱 You are just starting out. Focus on building core skills and projects."

        st.subheader(f"Status: :{color}[{status}]")
        st.info(message)

        # Score breakdown
        with st.expander("📊 Score Breakdown"):
            st.write(f"- **CGPA Score:** {cgpa_score}/3")
            st.write(f"- **Technical Skill Score:** {skill_score}/3")
            st.write(f"- **Project Score:** {project_score}/3")
            st.write(f"- **Internship Score:** {internship_score}/2")
            st.write(f"- **Total: {total_score}/{max_score}**")

        # 4. Tips Section
        st.divider()
        st.header("Step 3: Improvement Tips")

        tips = {
            "Ready": [
                "Start practicing LeetCode (Medium/Hard) regularly.",
                "Refine your behavioural interview answers using the STAR method.",
                "Get your resume reviewed by seniors or professionals.",
                "Apply for pre-placement opportunities and hackathons."
            ],
            "Intermediate": [
                "Build one 'Capstone' project that solves a real-world problem.",
                "Focus on Data Structures and Algorithms (DSA) basics.",
                "Aim to increase your CGPA if possible in upcoming semesters.",
                "Try to secure at least one internship for industry exposure."
            ],
            "Beginner": [
                "Pick one core language (Python/Java/C++) and master it.",
                "Start your first mini-project (e.g., a Todo app or Personal Site).",
                "Be consistent with college lectures to maintain a baseline CGPA.",
                "Explore free online courses on platforms like NPTEL or Coursera."
            ]
        }

        for tip in tips[status]:
            st.write(f"- {tip}")

# 5. Resources
st.divider()
st.header("Step 4: Resources")
st.markdown("""
Maintaining a healthy work-life balance is crucial during placement season.
- For extra study materials and guides, visit [CGPA Hub](https://cgpahub.com).
- Explore free DSA practice on [LeetCode](https://leetcode.com) and [GeeksforGeeks](https://geeksforgeeks.org).
- Build your professional profile on [LinkedIn](https://linkedin.com) and contribute to [GitHub](https://github.com).
- Remember to take short breaks, exercise, and get enough sleep to stay sharp.
""")

st.divider()

# 6. GPA Calculators Hub
st.markdown(
    """
    <h2 style="text-align:center;color:#1f2937;margin-bottom:15px;">📊 GPA Calculators Hub</h2>
    <p style="text-align:center;color:#4b5563;font-size:16px;line-height:1.6;margin-bottom:25px;">
    Quickly calculate grades for school, higher secondary, and university using our accurate GPA calculators.
    </p>
    """,
    unsafe_allow_html=True
)

calculators = [
    {"name": "SSC GPA Calculator",    "url": "https://cgpahub.com/tools/ssc-gpa-calculator",    "desc": "Quickly convert board grades into GPA.",                    "color": "#3b82f6"},
    {"name": "HSC GPA Calculator",    "url": "https://cgpahub.com/tools/hsc-gpa-calculator",    "desc": "Estimate higher secondary GPA accurately.",               "color": "#dc2626"},
    {"name": "SGPA Calculator",       "url": "https://cgpahub.com/tools/sgpa-calculator",       "desc": "Convert semester grades into GPA.",                       "color": "#059669"},
    {"name": "UOG GPA Calculator",    "url": "https://cgpahub.com/tools/uog-gpa-calculator",    "desc": "University of Gujrat GPA calculator.",                    "color": "#f97316"},
    {"name": "UofT GPA Calculator",   "url": "https://cgpahub.com/tools/uoft-gpa-calculator",   "desc": "Convert University of Toronto grades into GPA.",          "color": "#be185d"},
    {"name": "Purdue GPA Calculator", "url": "https://cgpahub.com/tools/purdue-gpa-calculator", "desc": "Estimate GPA for Purdue University courses.",             "color": "#2563eb"},
    {"name": "ASU GPA Calculator",    "url": "https://cgpahub.com/tools/asu-gpa-calculator",    "desc": "Arizona State University GPA calculator.",               "color": "#7c3aed"},
    {"name": "UF GPA Calculator",     "url": "https://cgpahub.com/tools/uf-gpa-calculator",     "desc": "University of Florida GPA estimation tool.",             "color": "#b45309"},
]

cols = st.columns(2)
for idx, calc in enumerate(calculators):
    col = cols[idx % 2]
    col.markdown(
        f"""
        <div style="background:#ffffff;padding:15px;border-radius:10px;border-left:5px solid {calc['color']};margin-bottom:15px;box-shadow:0 2px 6px rgba(0,0,0,0.05);">
            <h4 style="color:{calc['color']};margin-bottom:5px;">{calc['name']}</h4>
            <p style="color:#374151;margin-bottom:8px;font-size:14px;">{calc['desc']}</p>
            <a href="{calc['url']}" target="_blank" style="text-decoration:none;font-weight:600;color:#2563eb;">Open Calculator</a>
        </div>
        """,
        unsafe_allow_html=True
    )
