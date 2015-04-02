from django.http import HttpResponse
from django.shortcuts import render
from reportlab.pdfgen import canvas

def home(request):
    return render(request, 'app/home.html')


def py_df(request):
    #create the HttpResponse object with pdf headers
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="pyDF.pdf"'

    p = canvas.Canvas(response)

    p.drawString(10, 10, "Hello world")

    p.showPage()
    p.save()

    return response