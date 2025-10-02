# import libraries needed for module
from pathlib import Path
from fpdf import FPDF

# define function/module and define parameters 'arr' and 'file_name'
def write_data(arr, file_name):
    
    font_path = Path(__file__).parent.parent / 'fonts' / 'Futura.ttf' 
    pdf = FPDF()
    pdf.set_left_margin(12)
    pdf.set_top_margin(20)  
    pdf.set_right_margin(12)
    pdf.set_auto_page_break(True) 
    pdf.add_page() 
    pdf.add_font('Futura', '', str(font_path))
    pdf.set_font('Futura', size=24)
    pdf.cell(pdf.epw, 24, file_name.replace('_', ' ').capitalize())
    pdf.set_font('Futura', size=12)
    for val in arr: 
        pdf.multi_cell(pdf.epw, 8, val, align='L')
        pdf.ln(1)
    pdf_bytes = pdf.output(dest='S')
        
    return pdf_bytes