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
from emascouser.models import *


#home pagae for emasco
def home(request):
	
	context = {}
	return render(request,'home.html',context)




#services offered by emasco	
def services(request):
	
	context = {}
	return render(request,'services.html',context)	




#emasco's portfolio
def portfolio(request):	
	
	
	context = {}
	return render(request,'portfolio.html',context)




#emasco mission and vission
def missionAndVision(request):
	
	context = {}
	return render(request,'missionandvision.html',context)




#emasco core team	
def coreTeam(request):
	coreteams = User.objects.all()
	
	context = {'coreteams':coreteams}
	return render(request,'coreteam.html',context)	


#emasco contact us page
def contactUs(request):
	
	context = {}
	return render(request,'contactus.html',context)
