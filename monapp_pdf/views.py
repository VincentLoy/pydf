from django.http import HttpResponse
from django.shortcuts import render
from reportlab.pdfgen import canvas

from django import http
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
import xhtml2pdf.pisa as pisa
try:
    import StringIO
    StringIO = StringIO.StringIO
except Exception:
    from io import StringIO
import cgi

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

#extract from xhtml2pdf sources
def index(request):

    html = open('monapp_pdf/templates/app/home.html').read()

    return render(request, 'app/index.html', {'html' : html})

def download(request):
    if request.POST:
        result = StringIO()
        pdf = pisa.CreatePDF(
            StringIO(request.POST["data"]),
            result
            )
        #==============README===================
        #Django < 1.7 is content_type is mimetype
        #========================================
        if not pdf.err:
            return http.HttpResponse(
                result.getvalue(),
                content_type='application/pdf')

    return http.HttpResponse('We had some errors')

def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    result = StringIO()
    pdf = pisa.pisaDocument(StringIO( "{0}".format(html) ), result)
    if not pdf.err:
        #==============README===================
        #Django < 1.7 is content_type is mimetype
        #========================================
        return http.HttpResponse(result.getvalue(), content_type='application/pdf')
    return http.HttpResponse('We had some errors<pre>%s</pre>' % cgi.escape(html))

def ezpdf_sample(request):
    blog_entries = []
    for i in range(1,10):
        blog_entries.append({
            'id': i,
            'title':'Playing with pisa 3.0.16 and dJango Template Engine',
            'body':'This is a simple example..'
            })
    return render_to_pdf('entries.html',{
        'pagesize':'A4',
        'title':'My amazing blog',
        'blog_entries':blog_entries})