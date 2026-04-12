import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai

# -----------------------------
# LOAD ENV
# -----------------------------
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

# -----------------------------
# UI
# -----------------------------
st.set_page_config(page_title="AI Immigration Assistant", layout="wide")
st.title("🛂 AI Immigration Assistance Agent")
st.caption("Get visa guidance and immigration insights instantly")

# -----------------------------
# INPUTS
# -----------------------------
country = st.selectbox("🌍 Select Country", [
    "USA", "Canada", "UK", "Australia", "Germany"
])

visa_type = st.selectbox("📄 Visa Type", [
    "Student Visa", "Work Visa", "Tourist Visa"
])

st.subheader("👤 Your Profile")

education = st.text_input("Education")
experience = st.text_input("Work Experience")
budget = st.text_input("Budget")

# -----------------------------
# GENERATE INFO
# -----------------------------
if st.button("🔍 Get Immigration Guidance"):

    with st.spinner("🧠 Analyzing..."):

        prompt = f"""
        Provide immigration guidance for:

        Country: {country}
        Visa Type: {visa_type}
        Education: {education}
        Experience: {experience}
        Budget: {budget}

        Include:
        - Requirements
        - Eligibility
        - Documents needed
        - Processing time
        - Estimated cost
        - Advice based on profile
        """

        response = model.generate_content(prompt)

        st.subheader("📋 Immigration Guidance")
        st.write(response.text)

# -----------------------------
# FAQ SECTION
# -----------------------------
st.subheader("❓ Ask a Question")

question = st.text_input("Type your immigration question")

if st.button("💬 Get Answer"):
    if question.strip():
        prompt = f"""
        Answer this immigration question clearly:

        {question}
        """

        response = model.generate_content(prompt)
        st.write(response.text)

# -----------------------------
# DISCLAIMER
# -----------------------------
st.warning("⚠️ This tool provides general information only and is not legal advice.")