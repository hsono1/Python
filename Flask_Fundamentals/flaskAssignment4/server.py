from flask import Flask, request, session, render_template, redirect
import random

app = Flask(__name__)
app.secret_key = "mysecretkey"

@app.route("/")

def index():

	
	if 'guess_number' not in session:
		session['guess_number'] = random.randrange(0,101)
	return render_template("index.html")


@app.route("/guess", methods=["post"])

def guess():
	print "made it here", request.form['number']
	session['user_number'] = int(request.form["number"])

	if session['user_number'] < session['guess_number']:
			session['guess'] = "too_low" 
			session['txt'] = "You guess low"
	elif session['user_number'] > session['guess_number']:
			session['guess'] = "too_high"
			session['txt'] = "You guess high"
	else:
			session['guess'] = "right"
			session['txt'] = "You guess right"

	

	return redirect("/")



app.run(debug = True)