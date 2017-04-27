from flask import Flask, render_template, redirect, request, flash, session
from mysqlconnection import MySQLConnector
import re
from flask.ext.bcrypt import Bcrypt



app = Flask(__name__)
app.secret_key = "mysecretkey_dojo"
mysql = MySQLConnector(app, "mydb")
bcrypt = Bcrypt(app)



@app.route("/")
def index():
	return render_template("index.html")


@app.route("/login", methods=["post"])
def login():
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    if EMAIL_REGEX.match(request.form['email']):
        query1 = "SELECT * FROM users WHERE email = '{}'".format(request.form['email'])
        query2 = mysql.query_db(query1)
        if query2:
	        for element in query2:
				session['user_id'] = element['id']
				if bcrypt.check_password_hash( element['password'], request.form['pw']):
					return redirect('/messages')
				else:
					flash("Wrong password")
        else:
			pw_hash = bcrypt.generate_password_hash(request.form['pw'])
			query = "INSERT INTO users (email, password, created_at, updated_at) VALUES (:email,:pw, NOW(), NOW());"
			data = {"email":request.form['email'], "pw":pw_hash}
			if 'user_id' not in session:
				for element in query2:
					session['user_id'] = element['id']
			return redirect('/messages')
    else:
        flash("This is not a valid email!")
    return redirect("/")	


@app.route("/messages")
def success():
	print session.get('user_id')
	return render_template("messages.html")

	

# @app.route("/addMessage", methods=["post"])
# def addMessage():
#     EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
#     if EMAIL_REGEX.match(request.form['email']):
#         query1 = "SELECT * FROM users WHERE email = '{}'".format(request.form['email'])
#         query2 = mysql.query_db(query1)
#         if query2:
# 	        for element in query2:
# 				if bcrypt.check_password_hash( element['password'], request.form['pw']):
# 					return redirect('/success')
# 				else:
# 					flash("Wrong password")
#         else:
# 			pw_hash = bcrypt.generate_password_hash(request.form['pw'])
# 			query = "INSERT INTO users (email, password, created_at, updated_at) VALUES (:email,:pw, NOW(), NOW());"
# 			data = {"email":request.form['email'], "pw":pw_hash}
# 			mynewid = mysql.query_db(query, data)
# 			session['user_login'] = True
# 			return redirect('/messages')
#     else:
#         flash("This is not a valid email!")
#     return redirect("/addMessage")	















app.run(debug=True)
