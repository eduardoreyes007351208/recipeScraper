# import libraries needed for module
from pathlib import Path
from fpdf import FPDF

# define function/module and define parameters 'arr' and 'file_name'
def pdf_generate(arr, title):
    
    # get the path of the font
    font_path = Path(__file__).parent.parent / 'fonts' / 'DejaVuSansCondensed.ttf' 
    # create pdf object
    pdf = FPDF()
    # set pdf margins
    pdf.set_left_margin(12)
    pdf.set_top_margin(20)  
    pdf.set_right_margin(12)
    pdf.set_auto_page_break(True, margin=20)
    # new pdf page 
    pdf.add_page() 
    # add and set pdf font size
    pdf.add_font('DejaVu', '', str(font_path), uni=True)
    pdf.set_font('DejaVu', size=24)
    # pdf title
    pdf.cell(pdf.epw, None, title.title(), align='C')
    pdf.ln(10)
    pdf.set_font('DejaVu', size=12)
    
    # write the ingredients and instructions cells
    for val in arr: 
        if val == 'Ingredients:' or val == 'Instructions:':
            pdf.set_font_size(size=18)
        else:
            pdf.set_font_size(size=12)
        pdf.multi_cell(pdf.epw, 8, val)
        pdf.ln(1)
        
    # output the pdf as bytes for fastapi  
    pdf_bytes = pdf.output(dest='S')
        
    return pdf_bytes