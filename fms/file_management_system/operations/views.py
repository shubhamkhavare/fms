import os, uuid, tempfile, img2pdf
from rest_framework.views import APIView 
from django.http import HttpResponse
from django.shortcuts import render
from docx2pdf import convert
from .utils import update_user_count


class PdfLoverPage(APIView):

    def get(self, request):

        return render(request, 'operations/pdf_lover.html')

class ConvertImageToPdf(APIView):

    def get(self, request):
        return render(request, 'operations/image_to_pdf.html')

    def post(self, request):
        try:
            if 'file' not in request.FILES:
                return HttpResponse("Error: No files uploaded.", status=400)
            
            update_user_count(mode='image_to_pdf')
            
            image_files = request.FILES.getlist('file')

            with tempfile.NamedTemporaryFile(delete=False) as temp_pdf_file:
                pdf_data = img2pdf.convert([image.file for image in image_files])
                temp_pdf_file.write(pdf_data)

            with open(temp_pdf_file.name, "rb") as pdf_file:
                response = HttpResponse(pdf_file.read(), content_type='application/pdf')
                response['Content-Disposition'] = 'attachment; filename="output.pdf"'
                return response

        except Exception as e:
            return HttpResponse(f"An error occurred: {str(e)}", status=500)


class ConvertWordToPdf(APIView):

    def get(self, request):
        return render(request, 'operations/word_to_pdf.html')

    def post(self, request):    
        try:

            if 'file' not in request.FILES:
                return HttpResponse("Error: No files uploaded.", status=400)
            
            update_user_count(mode='word_to_pdf')

            word_file = request.FILES['file']
            word_file_name = str(uuid.uuid4()) + '.docx'

            with tempfile.TemporaryDirectory() as temp_dir:
                target_file_path = os.path.join(temp_dir, word_file_name)
                pdf_file_path = os.path.splitext(target_file_path)[0] + '.pdf'

                with open(target_file_path, 'wb') as destination:
                    for chunk in word_file.chunks():
                        destination.write(chunk)

                convert(target_file_path)

                with open(pdf_file_path, 'rb') as pdf_file:
                    pdf_content = pdf_file.read()

            response = HttpResponse(pdf_content, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{os.path.splitext(word_file.name)[0]}.pdf"'
            return response 

        except Exception as e:
            return HttpResponse(f"An error occurred: {str(e)}", status=500)

