from flask import Flask, request, redirect, render_template, session
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
mysql = MySQLConnector(app,'emaildb')
@app.route('/')
def index():
    query = "SELECT * FROM users"
    emails = mysql.query_db(query)
    return render_template('index.html', users_emails=emails)
        

@app.route('/wrong')
def wrong():
    output = "Wrong input"
    return render_template("index.html")


@app.route('/emails', methods=['POST'])
def create():
    # Write query as a string. Notice how we have multiple values
    # we want to insert into our query.

    if re.search(r"\b.+@.+\..+\b", request.form['user_email']):
        query = "INSERT INTO users (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
        # We'll then create a dictionary of data from the POST data received.
        data = {

        'email': request.form['user_email']
        }
        # Run query, with dictionary values injected into the query.
        mysql.query_db(query, data)
        return redirect('/')
    else:
        return redirect("/wrong")
           

    




app.run(debug=True)