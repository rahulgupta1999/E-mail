from django.db import models
class Users(models.Model):
	emailId=models.CharField(max_length=50,primary_key=True)
	password=models.CharField(max_length=50)
	name=models.CharField(max_length=50)
	gender=models.CharField(max_length=50)
	country=models.CharField(max_length=50)
class Emails(models.Model):
	date=models.DateField()
	fromId=models.CharField(max_length=50)
	toId=models.CharField(max_length=50)
	subject=models.CharField(max_length=50)
	message=models.CharField(max_length=5000)
#python manage.py makemigrations