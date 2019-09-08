from django.shortcuts import render
from django.http import HttpResponse
from django.template import context,loader
from mail.models import Emails
from mail.models import Users
import sqlite3
from datetime import date

def index(request):
	return render(request,'index.html')
def register(request):
	return render(request,'register.html')
def registerSave(request):
	email=request.POST["eid"]
	pwd=request.POST["pwd"]
	name=request.POST["unm"]
	gender=request.POST["gen"]
	country=request.POST["cnt"]
	c=Users(emailId=email,password=pwd,name=name,gender=gender,country=country)
	c.save()
	a="<label>Registered</label>"
	resp=HttpResponse(a)
	return(resp)
def login(request):
	return render(request,'login.html')
def loginCheck(request):
	eid=request.POST["eid"]
	pwd=request.POST["pwd"]
	lt=Users.objects.filter(emailId=eid,password=pwd)
	if lt:
		request.session["id"]=eid
		request.session["pw"]=pwd
		b=lt[0].name
		c=b.capitalize()
		return render(request,'home.html',{"uname":c})
	else:
		return render(request,'retry.html')

def composeOpen(request):
	return render(request,'compose.html')
def sendboxOpen(request):
	eid=request.session.get("id")
	inbox=Emails.objects.filter(fromId=eid)
	v="<html lang='en'><head><meta charset='utf-8'/><meta name='viewport' content='width=device-width,initial-scale=1'/><link rel='stylesheet' href='/static/bootstrap.min.css'/><script src='/static/jquery.min.js'></script><script src='/static/bootstrap.min.js'></script></head><body class=bg-success>"
	v+="<br><br><div class='table-responsive'><table class='table table-bordered bg-warning'>"
	v+="<tr><th style='text-align:center'> Email Date</th>"
	v+="<th style='text-align:center'>To</th>"
	v+="<th style='text-align:center'>Subject</th>"
	v+="<th style='text-align:center'>Message</th></tr>"
	for rec in inbox:
		v+="<tr><td align=center>"+str(rec.date)+"</td>"
		v+="<td align=center>"+rec.toId+"</td>"
		v+="<td align=center>"+rec.subject+"</td>"
		v+="<td align=center>"+rec.message+"</td></tr>"
	v+="</table></div>"
	resp=HttpResponse(v)
	return(resp)
def changepasswordOpen(request):	
	return render(request,'changepassword.html')
def composeSave(request):
	toId=request.POST["toeid"]
	fromId=request.session.get("id")
	msg=request.POST["msg"]
	subject=request.POST["subject"]
	curdate=date.today()
	emd=curdate.strftime("%Y-%m-%d")
	a=Emails(date=emd,fromId=fromId,toId=toId,subject=subject,message=msg)
	a.save()
	b="<h1>Email Send</h1>"
	resp=HttpResponse(b)
	return(resp)
def inboxOpen(request):
	eid=request.session.get("id")
	inbox=Emails.objects.filter(toId=eid)
	v="<html lang='en'><head><meta charset='utf-8'/><meta name='viewport' content='width=device-width,initial-scale=1'/><link rel='stylesheet' href='/static/bootstrap.min.css'/><script src='/static/jquery.min.js'></script><script src='/static/bootstrap.min.js'></script></head><body class=bg-success>"
	v+="<br><br><div class='table-responsive'><table class='table table-bordered bg-warning'>"
	v+="<tr><th style='text-align:center'>Email Date</th>"
	v+="<th style='text-align:center'>From</th>"
	v+="<th style='text-align:center'>Subject</th>"
	v+="<th style='text-align:center'>Message</th></tr>"
	for rec in inbox:
		v+="<tr><td align=center>"+str(rec.date)+"</td>"
		v+="<td align=center>"+rec.fromId+"</td>"
		v+="<td align=center>"+rec.subject+"</td>"
		v+="<td align=center>"+rec.message+"</td></tr>"
		
	v+="</table></div>"
	resp=HttpResponse(v)
	return(resp)
def changepassword(request):
	old=request.POST["opwd"]
	new=request.POST["npwd"]
	cnew=request.POST["cnpwd"]
	id=request.session.get("id")
	qs=Users.objects.filter(emailId=id,password=old)
	if new==cnew and qs:
		
		qs[0].password=new
		qs[0].save()
		msg="<h1>Password change<h1>"
	else:
		msg="<h1>Invalid Password<h1>"
	resp=HttpResponse(msg)
	return(resp)

def checkEmail(request):
	id=request.GET["eid"]
	qs=Users.objects.filter(emailId=id)
	if qs:
		msg="false"
	else:
		msg="true"
	resp=HttpResponse(msg)
	return(resp)
