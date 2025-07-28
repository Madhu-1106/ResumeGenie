import streamlit as st
from resume_parser import extract_text_from_pdf
from gpt_utils import analyze_resume_against_job, suggest_resume_improvements, suggest_learning_path
from export_pdf import export_to_pdf
import tempfile

st.set_page_config(page_title="GenAI Resume Coach", layout="wide")
st.title("🧠 GenAI Resume Coach")
st.markdown("Upload your resume and paste a job description. I’ll help you tailor your resume to the job!")

uploaded_file = st.file_uploader("📄 Upload your resume (PDF)", type=["pdf"])
job_description = st.text_area("📝 Paste the job description here", height=200)

if uploaded_file and job_description:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        resume_text = extract_text_from_pdf(tmp_file.name)

    if st.button("🔍 Analyze Resume"):
        with st.spinner("Analyzing with GenAI..."):
            result = analyze_resume_against_job(resume_text, job_description)
        st.markdown("### 📊 Match Analysis:")
        st.markdown(result)

    if st.button("✍️ Suggest Improvements"):
        with st.spinner("Generating improvements..."):
            suggestions = suggest_resume_improvements(resume_text, job_description)
        st.markdown("### ✨ Suggestions to Improve Your Resume:")
        st.markdown(suggestions)

        pdf_path = export_to_pdf(suggestions, output_path="improved_resume.pdf")
        with open(pdf_path, "rb") as f:
            st.download_button("⬇️ Download Improved Resume as PDF", f, file_name="Improved_Resume.pdf")
    
    if st.button("📚 Recommend Learning Path"):
        with st.spinner("Generating upskilling roadmap..."):
            learning_path = suggest_learning_path(resume_text, job_description)
        st.markdown("### 📘 Personalized Learning Path & Certifications:")
        st.markdown(learning_path)


