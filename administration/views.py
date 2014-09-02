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


#login for pproces in mobile 
def adminstrationMobo(request):
	allUsers = User.objects.all()
	if request.POST:
		
		form = request.POST
		
		usernameList = form.getlist('username_mobile')
		passwordList = form.getlist('password_mobile')
		
		tester = "not_match"
		
		if usernameList == "" or passwordList == "":
			
			context = {}
			return render(request, 'login.html',context)
		
		
		for user in allUsers:
			if user.username == usernameList[0] and user.password == passwordList[0] :
				tester = "match"
				break
				
		if tester == "not_match":
			
			warning = "Either password or username is incorrrect"
			context = {'warning':warning}
			return render(request, 'login.html',context)
				
		else:
			
			loginUser = User.objects.get(username = usernameList[0])
			loginUser.login_status = "login"
			loginUser.save()
			allMessages = CompanyMessage.objects.all()
			newMessages = CompanyMessage.objects.filter(message_status = "unread")
			allmessagescount = len(allMessages)
			newmessagecount = len(newMessages)
			
			
			context = {'newmessagecount':newmessagecount,'allmessagescount':allmessagescount,'loginUser':loginUser,}
			return render(request, 'administration.html',context)
	else:
		context = {}
		return render(request, 'login.html',context)
		
		




#login for pproces in other devices
def adminstration(request):
	allUsers = User.objects.all()
	if request.POST:
		
		form = request.POST
		
		usernameList = form.getlist('username')
		passwordList = form.getlist('password')
		
		tester = 0	
			
		for user in allUsers:
			if user.username == usernameList[0] and user.password == passwordList[0] :
				tester = 1
				break
				
		if tester == 0:
			warning = "Either password or username is incorrrect"
			
			context = {'warning':warning}		
			return render(request, 'login.html',context)
				
		else:
			
			loginUser = User.objects.get(username = usernameList[0])
			loginUser.login_status = "login"
			loginUser.save()
			
			allMessages = CompanyMessage.objects.all()
			newMessages = CompanyMessage.objects.filter(message_status = "unread")
			allmessagescount = len(allMessages)
			newmessagecount = len(newMessages)
			
			
			context = {'newmessagecount':newmessagecount,'allmessagescount':allmessagescount,'loginUser':loginUser,}
			return render(request, 'administration.html',context)

	else:
		context = {}
		return render(request, 'login.html',context)

#logout process
def logout(request,user_id):
	
	logoutUser = User.objects.get(id = user_id)
	logoutUser.login_status = "logout"
	logoutUser.save()
	
	return HttpResponseRedirect('/')
