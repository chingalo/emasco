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
from contacts.models import *

def contactMessage(request):
	
	form = request.POST
	 
	name = form.getlist('fullName')
	email = form.getlist('email')
	mobilenumber = form.getlist('mobilenumber')
	subjectsent = form.getlist('subject')
	messagesent = form.getlist('message')
	occupation = form.getlist('occupation')
	sex = form.getlist('sex')
	
	message = CompanyMessage()	
	message.fullname = name[0]
	message.email = email[0]
	message.mobile_number = mobilenumber[0]
	message.subject = subjectsent[0]
	message.message = messagesent[0]
	message.occupation = occupation[0]
	message.sender_sex = sex[0]
	message.save()
	
	#send emails
	recipient_list = []
	recipient_list.append("profschingalo@gmail.com")
	from_email = ""
	send_mail("NEW MESSSAGE IN EMASCO TZ","Hi\n"+message.fullname +" has send message",from_email,recipient_list,fail_silently=False)
	
	
	return HttpResponseRedirect("/")





#view all messages 
def allMessages(request,user_id):
	
	loginUser = User.objects.get(id = user_id)
	
	allMessages = CompanyMessage.objects.all()
	newMessages = CompanyMessage.objects.filter(message_status = "unread").order_by('-date')
	oldmessages = CompanyMessage.objects.filter(message_status = "read").order_by('-date')
	allmessagescount = len(allMessages)
	newmessagecount = len(newMessages)
	
	context = {'newMessages':newMessages,'oldmessages':oldmessages,'allmessagescount':allmessagescount,'newmessagecount':newmessagecount,'loginUser':loginUser,'status':"all"}
	return render(request, 'message.html', context)





#all unread messages
def newMessages(request,user_id):
	
	loginUser = User.objects.get(id = user_id)
	
	allMessages = CompanyMessage.objects.all()
	newMessages = CompanyMessage.objects.filter(message_status = "unread").order_by('-date')
	allmessagescount = len(allMessages)
	newmessagecount = len(newMessages)
	
	context = {'allmessagescount':allmessagescount,'newmessagecount':newmessagecount,'loginUser':loginUser,'status':"unread",'new_messages':newMessages}
	return render(request, 'message.html', context)





#single message 

def message(request,message_id,user_id):
	loginUser = User.objects.get(id = user_id)
	message = CompanyMessage.objects.get(id = message_id)
	message.message_status = "read"
	message.save()
	
	allMessages = CompanyMessage.objects.all()
	newMessages = CompanyMessage.objects.filter(message_status = "unread")
	allmessagescount = len(allMessages)
	newmessagecount = len(newMessages)
	
	context = {'allmessagescount':allmessagescount,'newmessagecount':newmessagecount,'loginUser':loginUser,'message':message}
	return render(request,'singleMessage.html',context)
	
	
	
	


