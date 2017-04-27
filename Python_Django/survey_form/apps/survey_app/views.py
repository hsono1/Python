from django.shortcuts import render, redirect

# Create your views here.


def index(request):
	return render(request, "survey_app/index.html")


def process(request):
	if request.method == 'POST':
		request.session['user'] = request.POST['user_name']
		request.session['location'] = request.POST['location']
		request.session['language'] = request.POST['language']
		request.session['comment'] = request.POST['comment']
		return redirect('/result')
	else:
		return redirect('/')

def result(request):
	user = request.session['user']
	location = request.session['location']
	language = request.session['language']
	comment = request.session['comment']
	show = { 'user' : user, 'location' : location , 'comment': comment, 'language' : language }
	return render(request, "survey_app/result.html", show)
