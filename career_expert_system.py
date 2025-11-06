import streamlit as st

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Future Finder: Career AI",
    page_icon="🔮",
    layout="wide"
)

# -------------------------------
# Custom CSS Styling (Modern Minimalist Design)
# -------------------------------
st.markdown("""
    <style>
    /* Global Background and Text */
    body {
        background-color: #f7f9f9; /* Light Cream Background */
        color: #1a1a1a; /* Dark Text */
        font-family: 'Inter', sans-serif;
    }
    
    /* Header/Title Styling */
    .main-title {
        background: #004d40; /* Deep Dark Teal/Green */
        color: white;
        padding: 2rem;
        text-align: center;
        border-radius: 5px;
        margin-bottom: 2rem;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
    }
    .main-title h1 {
        font-size: 2.5rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
    }
    .main-title p {
        font-size: 1.1rem;
        font-weight: 300;
    }
    
    /* Content Section Styling (Cards) */
    .section {
        background-color: white;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05), 0 8px 16px rgba(0,0,0,0.05); /* Soft, noticeable shadow */
        margin-bottom: 1.5rem;
        border-left: 5px solid #009688; /* Accent Line */
    }
    .section h3 {
        color: #004d40; /* Dark Teal for subheadings */
        border-bottom: 2px solid #e0f2f1;
        padding-bottom: 0.5rem;
        margin-bottom: 1rem;
    }
    
    /* Input/Button Styling */
    .stButton>button {
        background: #ff7043; /* Bright Orange/Coral Accent Color */
        color: white;
        border: none;
        padding: 0.8rem 1.5rem;
        border-radius: 5px;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
        box-shadow: 0 4px #e65100;
        transition: all 0.2s ease;
    }
    .stButton>button:hover {
        background: #e65100; /* Darker orange on hover */
        box-shadow: 0 2px #e65100;
        transform: translateY(2px);
    }
    
    /* Sidebar Input Styling */
    .stSelectbox, .stMultiSelect, .stNumberInput {
        padding-bottom: 15px;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #555;
        margin-top: 40px;
        font-size: 0.8em;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------------------
# Header
# -------------------------------
st.markdown("""
<div class="main-title">
    <h1>🔮 Future Finder: Career AI</h1>
    <p>Intelligent guidance for your next professional chapter</p>
</div>
""", unsafe_allow_html=True)

# -------------------------------
# Layout Columns
# -------------------------------
col_input, col_output = st.columns([1, 2])

# -------------------------------
# Sidebar Inputs (Left Panel)
# -------------------------------
with col_input:
    st.markdown("<div class='section'><h3>✍️ Tell Us About You</h3>", unsafe_allow_html=True)

    age = st.number_input("Current Age", min_value=15, max_value=65, value=22)
    stream = st.selectbox("Highest Academic Stream/Major", ["STEM (Science/Tech/Eng)", "Business/Finance (Commerce)", "Humanities/Arts/Law", "Other/Mixed Background"])
    interest = st.selectbox("Primary Interest Domain", ["Technology/Data", "Creative & Design", "Financial & Business Strategy", "Healthcare & Life Sciences", "Public Sector & Social Impact", "Education & Research"])
    skills = st.multiselect("Your Top 3-5 Skills", ["Communication", "Coding/Programming", "Leadership/Management", "Creative Thinking", "Data Analysis", "Design/Aesthetics", "Writing/Content", "Financial Modeling", "Problem Solving"])
    goal = st.selectbox("What is your main career driver?", ["High Earning Potential", "Work-Life Balance & Flexibility", "Intellectual Challenge/Research", "Making a Social/Environmental Impact"])

    st.markdown("</div>", unsafe_allow_html=True)
    st.write("") # Add some space
    generate = st.button("🚀 Analyze My Future Path")

# -------------------------------
# Expert System Logic (Slightly enhanced)
# -------------------------------
def recommend_career(stream, interest, skills, goal, age):
    
    # 1. Base Options determined by Stream and Interest
    career_map = {
        ("STEM (Science/Tech/Eng)", "Technology/Data"): ["AI Specialist", "Cloud Architect", "Data Scientist", "Software Developer"],
        ("STEM (Science/Tech/Eng)", "Healthcare & Life Sciences"): ["Biotech Researcher", "Physician/Surgeon", "Pharmacologist", "Biomedical Engineer"],
        ("Business/Finance (Commerce)", "Financial & Business Strategy"): ["Financial Analyst", "Investment Banker", "Chartered Accountant", "Management Consultant"],
        ("Business/Finance (Commerce)", "Technology/Data"): ["Product Manager", "FinTech Specialist", "Business Analyst"],
        ("Humanities/Arts/Law", "Creative & Design"): ["UX/UI Designer", "Content Strategist", "Filmmaker", "Digital Artist"],
        ("Humanities/Arts/Law", "Public Sector & Social Impact"): ["Civil Services Officer", "Corporate Lawyer", "Non-Profit Manager", "Policy Analyst"],
    }
    
    default_options = ["Entrepreneur", "Project Manager", "Consultant"]
    career_options = career_map.get((stream, interest), default_options)
    
    # 2. Skill-based refinement (Simple Scoring)
    # Give weight to options matching specific skills
    if "Coding/Programming" in skills:
        if "Software Developer" not in career_options: career_options.insert(0, "Software Developer")
    if "Leadership/Management" in skills:
        if "Management Consultant" not in career_options: career_options.insert(0, "Management Consultant")
    if "Financial Modeling" in skills:
        if "Financial Analyst" not in career_options: career_options.insert(0, "Financial Analyst")
    
    # 3. Goal-based Tips and Recommendations
    
    if goal == "High Earning Potential":
        focus = "High-Growth Industries (Tech/Finance)"
        tips = [
            "💰 Focus on high-demand, specialized skills like AI/ML or M&A analysis.",
            "🎓 Pursue advanced degrees (MBA, Masters) from top-tier institutions.",
            "🌐 Prioritize roles in metropolitan hubs where compensation is highest."
        ]
    elif goal == "Work-Life Balance & Flexibility":
        focus = "Flexible & Remote Roles"
        tips = [
            "🧘 Seek careers known for good balance, often in mid-sized firms or certain freelance fields.",
            "💻 Look for remote-first or four-day work week opportunities.",
            "🛡️ Develop skills that allow for location independence (e.g., specific coding, writing, or design). "
        ]
    elif goal == "Intellectual Challenge/Research":
        focus = "Advanced Research & Niche Expertise"
        tips = [
            "🔬 Dedicate yourself to continuous learning; a PhD or deep specialization is highly valuable.",
            "📚 Publish your findings and collaborate with global research teams.",
            "📈 Consider roles in R&D departments of major corporations or academia."
        ]
    else: # Social/Environmental Impact
        focus = "Mission-Driven Organizations"
        tips = [
            "🌍 Volunteer or intern at non-profits, government bodies, or B-Corps to build experience.",
            "🤝 Network with change-makers and policy experts in your desired sector.",
            "❤️ Look for roles in areas like renewable energy, urban planning, or public health."
        ]

    recommendation = f"Based on your **{stream}** background and primary interest in **{interest}**, we recommend focusing on **{focus}**."

    # Age specific advice
    if age < 25:
        recommendation += " Since you are early in your career, prioritize internships and skill acquisition."
    elif age >= 35:
        recommendation += " Given your experience level, consider a managerial role or leveraging your expertise for a career pivot."

    return recommendation, list(set(career_options)), tips # Use set to remove duplicates

# -------------------------------
# Output Panel (Right Side)
# -------------------------------
with col_output:
    if generate:
        recommendation, career_options, tips = recommend_career(stream, interest, skills, goal, age)

        st.markdown("<div class='section'>", unsafe_allow_html=True)
        st.subheader("💡 Your Personalized Career Focus")
        st.markdown(f"**{recommendation}**")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='section'>", unsafe_allow_html=True)
        st.subheader("🎯 Top Suggested Career Paths")
        
        # Calculate how many columns to use, max of 4 columns for readability
        num_cols = min(len(career_options), 4) 
        cols = st.columns(num_cols)
        
        for i, c in enumerate(career_options):
             # Use a card design for better visual appeal
             cols[i % num_cols].markdown(f"""
                <div style="background-color: #e0f2f1; padding: 15px; border-radius: 5px; text-align: center; border: 1px solid #004d40;">
                    <p style="color: #004d40; font-weight: 600; margin: 0;">{c}</p>
                </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='section'>", unsafe_allow_html=True)
        st.subheader("🚀 Actionable Success Tips")
        for tip in tips:
            st.markdown(f"**-** {tip}")
        st.markdown("</div>", unsafe_allow_html=True)

    else:
        st.info("⬅️ Ready to explore your future? Fill out your profile and click **Analyze My Future Path** to get tailored guidance.")

# -------------------------------
# Footer
# -------------------------------
st.markdown("<div class='footer'>Future Finder AI | Confidential Guidance System</div>", unsafe_allow_html=True)