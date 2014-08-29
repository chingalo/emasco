from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, render
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
import json 
from django.core.mail import send_mail
from random import randrange
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

from portfolio.models import *


#view for single portfolio
def singlePortfolio(request, portfolio_id):
	
	portfolio = Portfolio.objects.get(id = portfolio_id)
	slides = Gallery.objects.filter(portfolio = portfolio)
	
	context = {'portfolio':portfolio,'slides':slides}
	return render(request,'singlePortfolio.html',context)

