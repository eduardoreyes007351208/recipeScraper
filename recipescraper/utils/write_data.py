# import libraries needed for module
from pathlib import Path
from fpdf import FPDF

# define function/module and define parameters 'arr' and 'file_name'
def write_data(arr, title):
    
    font_path = Path(__file__).parent.parent / 'fonts' / 'Futura.ttf' 
    pdf = FPDF()
    pdf.set_left_margin(12)
    pdf.set_top_margin(20)  
    pdf.set_right_margin(12)
    pdf.set_auto_page_break(True, margin=20) 
    pdf.add_page() 
    pdf.add_font('Futura', '', str(font_path))
    pdf.set_font('Futura', size=24)
    pdf.cell(pdf.epw, None, title.title(), align='C')
    pdf.ln(10)
    pdf.set_font('Futura', size=12)
    
    for val in arr: 
        if val == 'Ingredients:' or val == 'Instructions:':
            pdf.set_font_size(size=18)
        else:
            pdf.set_font_size(size=12)
        pdf.multi_cell(pdf.epw, 8, val)
        pdf.ln(1)
        
            
    pdf_bytes = pdf.output(dest='S')
        
    return pdf_bytes