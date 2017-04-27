from django.shortcuts import render
from datetime import datetime

def index(request):

	show = { 'date' : datetime.now() }
	return render(request, "timedisplay/index.html", show)




# Create your views here.
