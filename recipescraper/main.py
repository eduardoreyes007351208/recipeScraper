# import libraries and modules for main.pu
from .utils import get_data, pdf_generate
import validators

from fastapi import FastAPI, HTTPException, Response

api = FastAPI()

# GET pdf 
@api.get('/get_pdf')
def get_pdf(url: str):
    # define array to contain data from get_data
    array = []
    
    # check to see the url argument from user is a valid url
    if validators.url(url):
        
        # get values from get_data module
        new_array, file_name, title = get_data(url, array)
        
        if len(new_array) < 4:
            raise HTTPException(status_code=404, detail='Recipe not found')
            
        else:
            pdf_bytes = bytes(pdf_generate(new_array, title))
            return Response(
                content=pdf_bytes,
                media_type='application/pdf',
                headers={'Content-Disposition': f'attachment; filename={file_name}.pdf'}
            )

# define the main functions
def main():
    pass
            
    

if __name__ == "__main__":
    main()
