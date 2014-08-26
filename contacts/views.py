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

from contacts.models import *

def contactMessage(request):
	
	form = request.POST
	 
	name = form.getlist('fullName')
	email = form.getlist('email')
	mobilenumber = form.getlist('mobilenumber')
	subjectsent= form.getlist('subject')
	messagesent= form.getlist('message')
	
	message = CompanyMessage()	
	message.fullname = name[0]
	message.email = email[0]
	message.mobile_number = mobilenumber[0]
	message.subject = subjectsent[0]
	message.message = messagesent[0]
	message.save()
	
	#send emails
	recipient_list = []
	recipient_list.append("profschingalo@gmail.com")
	from_email = ""
	send_mail("NEW MESSSAGE IN EMASCO TZ","Hi\n"+message.fullname +" has send message",from_email,recipient_list,fail_silently=False)
	
	
	return HttpResponseRedirect("/")
