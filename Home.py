import streamlit as st 
from PIL import Image

st.set_page_config(layout="wide", page_title="Arindam | Portfolio", page_icon="assets/Profile_icon.png")

# --- Load Images ---
profile_image = Image.open("assets/profile.jpg")

# --- CSS Styling ---
st.markdown("""
<style>
.navbar {
    display: flex;
    justify-content: center;
    gap: 2rem;
    padding: 1rem 0;
    background-color: #f5f5f5;
    position: sticky;
    top: 0;
    z-index: 999;
    border-bottom: 1px solid #eaeaea;
}
.navbar a {
    text-decoration: none;
    font-weight: bold;
    color: black;
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
</style>

<div class="navbar">
    <a href="#home">Home</a>
    <a href="#about">About Me</a>
    <a href="#projects">Projects</a>
    <a href="#certifications">Certifications</a>
    <a href="#contact">Contact</a>
</div>
""", unsafe_allow_html=True)

# --- Home ---
st.markdown('<div id="home"></div>', unsafe_allow_html=True)

# Centered profile picture with styling
st.markdown("""
    <style>
        .centered-image img {
            display: block;
            margin-left: auto;
            margin-right: auto;
            border-radius: 20px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="centered-image">', unsafe_allow_html=True)
st.image(profile_image, width=150)
st.markdown('</div>', unsafe_allow_html=True)

# Centered headings
st.markdown("<h1 class='center'>Hey! I'm Arindam Maji 👋</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='center'>Data Engineer | Full Stack Developer</h3>", unsafe_allow_html=True)

# --- About Me ---
st.markdown('<div id="about"></div>', unsafe_allow_html=True)
st.subheader("About Me")
st.write("""
I'm Arindam Maji, a Computer Science undergrad from LPU with a CGPA of 8.20.

💻 I work on full-stack web development using the MERN stack, backend systems in Go and FastAPI, and love data engineering with Spark, Kafka, and AWS.  
📊 I also explore data analysis in Python (Pandas, NumPy, Seaborn) and dashboarding with Tableau.
""")
st.info("Languages: Python, C++, R, Java")
st.info("Education: B.Tech in Computer Science, LPU")

# --- Projects ---
st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
st.subheader("Projects")

with st.expander("✈️ Flight Data Pipeline – Real-Time ETL & Dashboard"):
    st.write("""
- **Tech Stack:** Python, Apache Kafka, AWS S3, Spark, Tableau  
- Built a real-time pipeline for flight & weather data, stored in S3 and analyzed with Spark and Tableau.
""")
    st.markdown("[🔗 GitHub Repo](https://github.com/arindam-maji/Flight_Data_Pipeline_Project.git)", unsafe_allow_html=True)

with st.expander("🧠 Customer Segmentation – Clustering in Python"):
    st.write("""
- Used K-Means clustering to group customers for marketing insights.  
- **Tech Stack:** Pandas, Seaborn, Scikit-learn
""")
    st.markdown("[🔗 GitHub Repo](https://github.com/arindam-maji/Customer_Segementation_Project.git)", unsafe_allow_html=True)

with st.expander("📊 Excel Dashboard – Interactive Visuals"):
    st.write("Created a dashboard with slicers, pivot tables, and charts to analyze company KPIs.")
    st.image("assets/certifications/python_cipherschools.jpg", width=300)

with st.expander("🚗 Toll Plaza Management in C"):
    st.write("Toll billing system with vehicle type tracking, billing rates, and reporting.")
    st.markdown("[🔗 GitHub Repo](https://github.com/arindam-maji/Toll_Plaza_Management)", unsafe_allow_html=True)

# --- Certifications ---
st.markdown('<div id="certifications"></div>', unsafe_allow_html=True)
st.subheader("Certifications")

certs = [
    ("IBM DevOps & Software Engineering", "assets/certifications/Devops_ibm.jpeg", "https://shorturl.at/jDRQv"),
    ("Data Analysis with Tableau", "assets/certifications/tableau_coursera.jpeg", "https://shorturl.at/83qJF"),
    ("Cloud Computing (NPTEL)", "assets/certifications/cloud_nptel.png", "https://shorturl.at/WSBqT"),
    ("Python, Data Science & ML", "assets/certifications/python_cipherschools.jpg", "https://shorturl.at/ah47U"),
]

cols = st.columns(4)
for col, (title, path, url) in zip(cols, certs):
    with col:
        st.image(path, caption=title, use_container_width=True)
        st.markdown(f"[🔗 View Certificate]({url})", unsafe_allow_html=True)

# --- Contact ---
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
st.subheader("📬 Contact Me")
with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    submit = st.form_submit_button("Send")
    if submit:
        st.success("Thanks for reaching out! I’ll get back to you soon.")
