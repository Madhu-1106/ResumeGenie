# ResumeGenie - Your AI Resume Helper ✨

ResumeGenie is a simple AI tool built using Streamlit that helps you improve your resume based on any job description. Just upload your resume, paste the job role, and get tips on how to make your resume a better fit!

## What it can do:

- 📄 Upload your resume (PDF only)
- 📝 Paste the job description
- ✅ Get a Fit Score showing how well your resume matches the job
- ✍️ Get suggestions to improve your resume
- 📘 Get a learning path with certifications to fill skill gaps
- 📥 Download the suggestions as a PDF

## Tools & Libraries Used:

- **Python** – for backend logic
- **Streamlit** – to create the web app interface
- **PyMuPDF** – to read PDF files
- **FPDF** – to generate PDF download
  
## How to Run

1. Clone the project:
   ```bash
   git clone https://github.com/your-username/resumegenie.git
   cd resumegenie
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # for Windows
   # or
   source venv/bin/activate  # for Mac/Linux
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the app:
   ```bash
   streamlit run app.py
   ```

## Project Structure
├── app.py            → Main Streamlit app
├── gpt_utils.py      → Logic for scoring, tips, learning paths
├── resume_parser.py  → Reads the resume PDF
├── export_pdf.py     → Exports suggestions to PDF
├── requirements.txt  → List of libraries needed

## Who Can Use This?

- Students and freshers building their first resume
- Job seekers applying to tech roles
- Anyone looking to improve their resume with AI help

## Made by
Madhu M S  
Feel free to connect on LinkedIn or raise an issue if you need help!

If this helped you, feel free to ⭐ the repo 🙂
