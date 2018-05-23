# import Flask
from flask import Flask, render_template, redirect, request, session, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = "ThisIsSecret!"

@app.route('/')
def index():
  return render_template("index.html")
@app.route('/process', methods=['POST'])
def submit():
  session['first_name'] = request.form['first_name']
  session['last_name'] = request.form['last_name']
  session['email'] = request.form['email']
  session['username'] = request.form['username']
  session['city'] = request.form['city']
  session['state'] = request.form['state']
  session['zip'] = request.form['zip']
  
  if len(request.form['email']) < 1:
    flash("Email cannot be blank!")
  # else if email doesn't match regular expression display an "invalid email address" message
  else:
      flash("Success!")
  return redirect('/')

@app.route('/contact')
def contact():
  return render_template('contact.html')



app.run(debug=True)