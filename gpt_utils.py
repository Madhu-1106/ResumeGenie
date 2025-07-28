def analyze_resume_against_job(resume_text, job_description):
    resume_lower = resume_text.lower()
    jd_lower = job_description.lower()

    skills = [
        "python", "java", "sql", "aws", "gcp", "azure", "docker", "kubernetes",
        "linux", "git", "jenkins", "terraform", "ci/cd", "machine learning",
        "devops", "bash", "scripting", "cloud", "github", "ansible"
    ]

    matching_skills = [skill for skill in skills if skill in resume_lower and skill in jd_lower]
    missing_skills = [skill for skill in skills if skill in jd_lower and skill not in resume_lower]

    match_score = int((len(matching_skills) / len(skills)) * 100)

    return f"""
**Fit Score:** {match_score}/100  
**Matching Skills:** {', '.join(matching_skills) if matching_skills else 'None'}  
**Gaps:** {', '.join(missing_skills) if missing_skills else 'None'}  
**Suggestions:** Consider including: {', '.join(missing_skills)} in your resume to align better with the job description.
"""


def suggest_resume_improvements(resume_text, job_description):
    resume_lower = resume_text.lower()
    jd_lower = job_description.lower()

    skills = [
        "python", "java", "sql", "aws", "gcp", "azure", "docker", "kubernetes",
        "linux", "git", "jenkins", "terraform", "ci/cd", "machine learning",
        "devops", "bash", "scripting", "cloud", "github", "ansible"
    ]

    missing_skills = [skill for skill in skills if skill in jd_lower and skill not in resume_lower]
    suggestions = []

    if missing_skills:
        suggestions.append(f"- Include missing technical skills: {', '.join(missing_skills)}")
    if "metrics" not in resume_lower:
        suggestions.append("- Quantify your achievements using numbers or results.")
    if "team" not in resume_lower:
        suggestions.append("- Mention teamwork or cross-functional collaboration.")
    if "lead" not in resume_lower and "manager" in jd_lower:
        suggestions.append("- Highlight any leadership or mentoring experience.")

    if not suggestions:
        suggestions.append("- Your resume seems well aligned. Focus on formatting and tailoring.")

    return "\n".join(suggestions)


def suggest_learning_path(resume_text, job_description):
    resume_lower = resume_text.lower()
    jd_lower = job_description.lower()

    skills = {
        "docker": "Docker Essentials Certification (LinkedIn Learning)",
        "kubernetes": "Kubernetes for Developers (Udemy)",
        "aws": "AWS Certified Solutions Architect – Associate",
        "gcp": "Google Associate Cloud Engineer",
        "ci/cd": "CI/CD Pipelines with Jenkins (Coursera)",
        "terraform": "Terraform Associate Certification (HashiCorp)",
        "linux": "Linux Fundamentals (edX)",
    }

    matched_skills = [skill for skill in skills if skill in resume_lower and skill in jd_lower]
    missing_skills = [skill for skill in skills if skill in jd_lower and skill not in resume_lower]
    match_score = int((len(matched_skills) / len(skills)) * 100)

    if match_score >= 70:
        return "✅ You're already well-aligned with this job role. Consider fine-tuning your portfolio and gaining project experience."

    cert_recommendations = [f"- {skills[skill]}" for skill in missing_skills]

    return f"""
📌 **Skill Gaps Identified:**
{', '.join(missing_skills) if missing_skills else 'None'}

🎓 **Recommended Certifications:**
{chr(10).join(cert_recommendations)}

🗺️ **Suggested Learning Path:**
1. Start with beginner-friendly online courses on platforms like Coursera or Udemy.
2. Practice hands-on using cloud sandboxes and container labs.
3. Build a project using {', '.join(missing_skills[:2])} and host it on GitHub.
4. Add these skills and links to your updated resume.
"""
