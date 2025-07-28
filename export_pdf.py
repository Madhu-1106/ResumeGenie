from fpdf import FPDF

def export_to_pdf(text, output_path="improved_resume.pdf"):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for line in text.split("\n"):
        pdf.multi_cell(0, 10, line)

    pdf.output(output_path)
    return output_path