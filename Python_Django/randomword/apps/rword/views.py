from django.shortcuts import render, redirect
import random, string
# Create your views here.


def index(request):
	if 'count' and 'num' not in request.session:
		request.session['count'] = 1
		request.session['num'] = 1
	return render(request, "rword/index.html")


def success(request):
	if request.method == 'POST':
		request.session['variable'] = random_Word(14)
		if request.session['count'] == request.session['num']:
			request.session['num'] = -3
		else:
			request.session['count'] = request.session['count'] + 1
		return redirect("/")


def random_Word(size, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))