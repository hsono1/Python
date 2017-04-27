from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = 'ThisisSecret'
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/users', methods=['POST'])
def create_user():
   print "Got Post Info"
   # we'll talk about the following two lines after we learn a little more
   # about forms
   session['name'] = request.form['name']
   session['email'] = request.form['email']
   return redirect('/show')

@app.route('/show', methods=['post'])
def show_user():
  	return render_template('user.html', name=session['name'], email=session['email'])





app.run(debug=True) # run our server
