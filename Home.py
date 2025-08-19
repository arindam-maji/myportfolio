import streamlit as st
import streamlit.components.v1 as components  # <-- Add this line
from PIL import Image

st.set_page_config(layout="wide", page_title="Barnali | Portfolio", page_icon="assets/Profile_icon.png")

# --- Load Images ---
profile_image = Image.open("assets/profile.jpg")

# --- CSS Styling ---
st.markdown("""
<style>
body {
    background-color: #121212;
    color: #fff;
    font-family: Arial, sans-serif;
}
.navbar {
    display: flex;
    justify-content: center;
    gap: 2rem;
    padding: 1rem 0;
    background-color: #1c1c1c;
    position: sticky;
    top: 0;
    z-index: 999;
    border-bottom: 1px solid #444;
}
.navbar a {
    text-decoration: none;
    font-weight: bold;
    color: #fff;
    padding: 0.5rem;
}
.navbar a:hover {
    color: #6c63ff;
}
.center {
    text-align: center;
}
.cert-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
    margin-top: 2rem;
}
.cert-card img {
    width: 100%;
    max-width: 250px;
    border-radius: 15px;
    transition: 0.3s ease;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}
.cert-card img:hover {
    transform: scale(1.03);
}
.cert-card {
    text-align: center;
}

@keyframes slideIn {
    0% { opacity: 0; transform: translateY(30px); }
    100% { opacity: 1; transform: translateY(0); }
}

.animated {
    animation: slideIn 1s ease-out;
}

.tech-logos img {
    width: 50px;
    margin: 10px;
    transition: transform 0.3s ease-in-out;
}

.tech-logos img:hover {
    transform: scale(1.2);
}
</style>

<div class="navbar">
    <a href="#home">Home</a>
    <a href="#about">About Me</a>
    <a href="#experience">Experience</a>
    <a href="#projects">Projects</a>
    <a href="#certifications">Certifications</a>
    <a href="#activities">Extra Curricular Activities</a>
    <a href="#contact">Contact</a>
</div>
""", unsafe_allow_html=True)

# --- Home ---
st.markdown('<div id="home"></div>', unsafe_allow_html=True)

st.subheader("👋 Welcome!")

profile_cols = st.columns([1, 2, 1])
with profile_cols[1]:
    st.image(profile_image, width=150, caption="Barnali Manna")

st.markdown("<h1 class='center animated'>Hey! I'm Barnali Manna 👋</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='center animated'>🌟 Data Analyst | B.Tech CSE Student | Explorer of Data-Driven Insights</h3>", unsafe_allow_html=True)

# --- About Me ---
st.markdown('<div id="about"></div>', unsafe_allow_html=True)
st.subheader("About Me")
st.write("""
I'm Barnali Manna, a Computer Science undergrad from Brainwire University with a CGPA of 8.74.
         
💻 I'm passionate about transforming raw data into meaningful insights that drive impactful decisions. With skills in R, Excel, Tableau, Python, and SQL, I focus on solving real-world problems and creating innovative, data-centric solutions.
📊 I also explore data analysis in Python (Pandas, NumPy, Seaborn) and dashboarding with Tableau.
""")
# --- Education ---
st.markdown("### 🎓 Education")
st.markdown("""
**Brainware University**  
📍 West Bengal, India  
**B.Tech in Computer Science & Engineering**  
CGPA: 8.70 / 10  
📅 *2022 – 2026*
""")
skills = {
    "Programming Languages": "Python, C, SQL",
    "Data Analysis Tools": "Excel, Pandas, NumPy",
    "Data Visualization": "PowerBI, Matplotlib, Seaborn",
    "Databases": "MySQL",
    "Machine Learning": "Scikit-Learn",
    "FullStack": "HTML, CSS, JavaScript, Node, React, Express"
}
for title, items in skills.items():
    st.info(f"{title}: {items}")

# --- Technology Stack ---
st.subheader("💻 Technologies I Use")
tech_stack = [
    ("Python", "assets/logos/python.jpeg"),
    ("PowerBI", "assets/logos/powerbi.png"),
    ("GitHub", "assets/logos/git.png"),
    ("VSCode", "assets/logos/vscode.png")
]
logo_cols = st.columns(len(tech_stack))
for col, (tech, logo_path) in zip(logo_cols, tech_stack):
    with col:
        st.image(logo_path, caption=tech, width=60)

# --- Experience ---
# st.markdown('<div id="experience"></div>', unsafe_allow_html=True)
# st.subheader("💼 Experience")

# with st.expander("🏕️ Summer Training"):
#     st.write("""
# - **Organization:** CipherSchools  
# - **Role:** Intern - Python, Data Science and Machine Learning integrated  
# - **Duration:** June 2024 - July 2024  
# - **Overview:**  
#     - Learned Data preprocessing, cleaning, and data analysis.  
#     - Learned about machine learning models and their practical applications.  
#     - Collaborated with a team of 2 to build a dashboard for customer segmentation.
# """)
#     st.markdown("[🔗 Project Report](https://github.com/arindam-maji/Customer_Segmentation_Project/blob/2887fae7017e066cda8acaeaf671aed313c36d58/Insights_Report.pdf)", unsafe_allow_html=True)

# with st.expander("🌱 Community Development Project"):
#     st.write("""
# - **Project:** Smart Irrigation for Rural Development  
# - **Organization:** Nimbark Math Seva Samiti Trust, West Bengal  
# - **Overview:**  
#     - Arranged direct medical assistance in tribal areas.  
#     - Distributed free medicines  
#     - Worked on organization's website for donations.
# """)
#     st.write("📸 Here's a glimpse of the work:")
#     community_images = [
#         ("Community Work 1", "assets/experience/community_project1.jpg"),
#         ("Community Work 2", "assets/experience/community_project2.jpg"),
#     ]
#     comm_cols = st.columns(len(community_images))
#     for col, (caption, path) in zip(comm_cols, community_images):
#         with col:
#             st.image(path, caption=caption, use_container_width=True)
#     st.markdown("[🔗 Learn More](https://nmsst.co.in/contact-us)", unsafe_allow_html=True)

# --- Projects ---
st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
st.subheader("Projects")

projects = [
    (" BMI - Calculator", "- **Tech Stack:** Python, Apache Kafka, AWS S3, Spark, Tableau  \n- Built a real-time pipeline for flight & weather data, stored in S3 and analyzed with Spark and Tableau.", "https://tkltincb1syh8x7dyybwjq.on.drv.tw/www.bmicalculator.com/"),
    (" House PricingSite – Clustering in Python", "- Used K-Means clustering to group customers for marketing insights.  \n- **Tech Stack:** Pandas, Seaborn, Scikit-learn", "https://tkltincb1syh8x7dyybwjq.on.drv.tw/www.house-price-prediction.com/"),
    (" Motorola MobileSales Dashboard – Interactive Visuals", "Created a dashboard with slicers, pivot tables, and charts to analyze company KPIs.", "https://app.powerbi.com/groups/me/reports/5da5f500-0b26-4afb-86c9-ea24a2464c8d/8552c77386d8085392cc?experience=power-bi"),
]

for title, desc, link in projects:
    with st.expander(title):
        st.write(desc)
        if "BMI - Calculator" in title:
            st.image("assets/projects/BMI_calculator.png", use_container_width=True)
        st.markdown(f"[🔗 GitHub Repo]({link})", unsafe_allow_html=True)

# --- Certifications ---
st.markdown('<div id="certifications"></div>', unsafe_allow_html=True)
st.subheader("Certifications")
certs = [
    ("30-days-PowerBi-course", "assets/certifications/30-days-PowerBi-course.jpg"),
    ("Fundamentals_of_DSA_in_C", "assets/certifications/Fundamentals_of_DSA_in_C.jpg"),
    ("Introduction to Machine Learning", "assets/certifications/Introduction_to_Machine_Learning.jpg"),
    ("SQL Fundamentals in 90 Minutes", "assets/certifications/SQL_Fundamentals_in_90_Minutes.jpg"),
    ("PowerBi_Project", "assets/certifications/PowerBi_Project.jpg")
]
cert_cols = st.columns(4)
for col, (title, path, url) in zip(cert_cols, certs):
    with col:
        st.image(path, caption=title, use_container_width=True)
        st.markdown(f"[🔗 View Certificate]({url})", unsafe_allow_html=True)

# --- Extracurricular Activities ---
st.markdown('<div id="activities"></div>', unsafe_allow_html=True)
st.subheader("🎨 Extracurricular Activities")
with st.expander("📸 College Events"):
    st.write("Here are some glimpses from the vibrant college events I've participated in:")

    college_events = [
        ("College event", "assets/extracurricular/college_event1.jpg"),
        ("College Women's Cricket", "assets/extracurricular/college_event2.jpg"),
        ("Mrs Fresher", "assets/extracurricular/college_event3.jpg"),
    ]

    event_cols = st.columns(len(college_events))
    for col, (caption, path) in zip(event_cols, college_events):
        with col:
            st.image(path, caption=caption, use_container_width=True)

# with st.expander("🖌️ My Artworks"):
#     st.write("Outside of tech, I love expressing myself through art. Here are a few pieces I've made:")
#     artworks = [
#         ("Sunset Oil Painting", "assets/extracurricular/art1.jpg"),
#         ("Watercolor", "assets/extracurricular/art2.jpg"),
#         ("Portrait", "assets/extracurricular/art3.png"),
#     ]
#     art_cols = st.columns(len(artworks))
#     for col, (caption, path) in zip(art_cols, artworks):
#         with col:
#             st.image(path, caption=caption, use_container_width=True)
# --- Resume ---
# --- Resume ---
st.markdown("### 📄 My Resume")

resume_file_path = "assets/barnali.pdf"

# Download Button
with open(resume_file_path, "rb") as file:
    resume_bytes = file.read()

st.download_button(
    label="📥 Download Resume",
    data=resume_bytes,
    file_name="barnali.pdf",
    mime="application/pdf",
)

# # Resume Image Preview
# st.markdown("#### 👀 Resume Preview")
# st.image("assets/resume.png", use_container_width=True)
# --- Video CV Section ---
# st.markdown("## 🎥 Video CV")

# # Embed video from Google Drive
# drive_video_id = "YOUR_VIDEO_ID"  # Replace with your actual video ID
# drive_embed_link = f"https://drive.google.com/file/d/{drive_video_id}/preview"

# components.html(
#     f"""
#     <iframe src="{drive_embed_link}" width="100%" height="480" allow="autoplay"></iframe>
#     """,
#     height=500,
# )
# --- Contact ---
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
st.subheader("📬 Contact Me")

contact_info = {
    "Email": "mannabarnali294@gmail.com",
    "LinkedIn": "[linkedin.com/barnali-manna](https://www.linkedin.com/in/barnali-manna/)",
    "GitHub": "[github.com/Barnalimanna](https://github.com/Barnalimanna)",
}
for platform, link in contact_info.items():
    st.markdown(f"**{platform}:** {link}")

with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    submit = st.form_submit_button("Send")
    if submit:
        st.success("Thanks for reaching out! I’ll get back to you soon.")