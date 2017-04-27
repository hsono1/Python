from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key= "my_secret_key"



@app.route("/")

def index():
	
	if 'count' not in session:
		session['count'] = 1
	else:
		session['count'] += 1
	return render_template("index.html")

@app.route('/plus2')

def plus2():

	
	session['count'] += 2
	return redirect("/")

@app.route('/reset')

def reset():
	session.clear()
	return redirect("/")





app.run(debug=True)