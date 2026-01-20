from fpdf import FPDF
import os

def create_single_pdf(folder, img_path, name):
    """Wraps a single image into a single-page PDF."""
    if not os.path.exists(img_path):
        return None
        
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", "B", 12)
    pdf.cell(0, 10, f"Screenshot: {name}", ln=True)
    
    # Scale image to fit page width
    pdf.image(img_path, x=10, y=20, w=190)
    
    pdf_filename = f"{name}.pdf"
    pdf_path = os.path.join(folder, pdf_filename)
    pdf.output(pdf_path)
    return pdf_path

def create_pdf_report(url, folder, full_page_img, screenshots):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    pdf.add_page()
    pdf.set_font("helvetica", "B", 20)
    pdf.cell(0, 20, "Website Crawl Report", ln=True, align="C")
    
    pdf.set_font("helvetica", "", 12)
    pdf.set_text_color(0, 102, 204)
    pdf.cell(0, 10, f"Target: {url}", ln=True, align="C")
    
    if os.path.exists(full_page_img):
        pdf.add_page()
        pdf.set_font("helvetica", "B", 14)
        pdf.cell(0, 10, "Full Page View", ln=True)
        pdf.image(full_page_img, x=10, w=190)

    for item in screenshots:
        paths = item["path"]
        if isinstance(paths, list):
            for label, img_path in paths:
                if os.path.exists(img_path):
                    pdf.add_page()
                    pdf.set_font("helvetica", "B", 12)
                    pdf.cell(0, 10, f"Element: {item['type']} - {label.upper()}", ln=True)
                    pdf.image(img_path, x=10, w=190)
        elif isinstance(paths, str) and os.path.exists(paths):
            pdf.add_page()
            pdf.image(paths, x=10, w=190)

    pdf_output_path = os.path.join(folder, "report.pdf")
    pdf.output(pdf_output_path)
    return pdf_output_path