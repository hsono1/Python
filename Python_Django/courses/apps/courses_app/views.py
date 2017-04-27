from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index(request):
	context = { 'course' : Course.objects.all() }
	return render(request, "courses_app/index.html", context)


def success(request):
	Course.objects.create(course_name= request.POST['course_name'], course_desc= request.POST['course_desc'])
	return redirect ("/")

def remove(request, id):
	Course.objects.filter(id=id).delete()
	return redirect ("/")