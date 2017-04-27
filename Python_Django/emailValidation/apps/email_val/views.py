from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Email

# Create your views here.
def index(request):
	return render(request, "email_val/index.html")

def validate(request):
	emails = Email.objects.emailValidation(request.POST)
	if emails[0] == True:
		return redirect("/success")
	else:
		for message in emails[1]:
			messages.error(request, message)
		return redirect("/")

def success(request):
	emails = Email.objects.all()
	context = { 'emails': emails}
	return render(request, "email_val/success.html", context)

def remove(request, id):
	Email.objects.filter(id=id).delete()
	return redirect('/success')