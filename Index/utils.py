from django.shortcuts import HttpResponse
from django.template.loader import get_template, render_to_string

from fpdf import FPDF, HTMLMixin


class HtmlPdf(FPDF, HTMLMixin):
    pass


def print_pdf(request):
    pdf = HtmlPdf()
    pdf.add_page()
    pdf.write_html(render_to_string('index_output.html'))

    response = HttpResponse(pdf.output(dest='S').encode('latin-1'))
    response['Content-Type'] = 'application/pdf'

    return response
