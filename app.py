import io
import os
import tempfile
from PIL import Image, ImageOps, ImageEnhance
import pypdfium2 as pdfium
from flask import Flask, render_template, request, make_response

app = Flask(__name__)

def invert(filepath):
    with tempfile.TemporaryDirectory() as path:
        pdf = pdfium.PdfDocument(filepath)
        n_pages = len(pdf)
        black_and_white_images = []

        for im in range(n_pages):
            pil_image = pdf.get_page(im).render_topil(scale=3, rotation=0, greyscale=False, optimise_mode=pdfium.OptimiseMode.PRINTING,)
            baw = pil_image.convert('RGB').convert('L')
            im_invert = ImageOps.invert(baw)
            enhancer = ImageEnhance.Contrast(im_invert)
            final_image = enhancer.enhance(7.0)
            black_and_white_images.append(final_image)

        # create a BytesIO object to store the output PDF file in memory
        output = io.BytesIO()
         
        black_and_white_images[0].save(output, format='PDF', save_all=True, append_images=black_and_white_images[1:])

    # return the contents of the BytesIO object as bytes
    return output.getvalue()

@app.route('/', methods=['GET', 'POST'])
def home():
    pdf_data = None
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return render_template('home.html', error='No file selected')
        
        file = request.files['file']
        
        # if user does not select file, browser also submit an empty part without filename
        if file.filename == '':
            return render_template('home.html', error='No file selected')
            
        # save file to temporary location
        filename = os.path.join(tempfile.gettempdir(), 'input.pdf')
        file.save(filename)
        
        # invert colors and save output file in memory
        if filename.endswith('.pdf'):
            pdf_data = invert(filename)
        else:
            return render_template('home.html', error='Invalid file type. Please upload a PDF file.')
    
    return render_template('home.html', error=None, pdf_data=pdf_data)

@app.route('/view_pdf')
def view_pdf():
    pdf_data = invert(os.path.join(tempfile.gettempdir(), 'input.pdf'))
    response = make_response(pdf_data)
    response.headers['Content-Type'] = 'application/pdf'
    return response

@app.route('/download_pdf')
def download_pdf():
    pdf_data = invert(os.path.join(tempfile.gettempdir(), 'input.pdf'))
    response = make_response(pdf_data)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=inverted.pdf'
    return response

if __name__ == '__main__':
    app.run(debug=True)
