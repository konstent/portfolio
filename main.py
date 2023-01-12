from flask import Flask, render_template, url_for, redirect, request, flash
from flask_wtf import FlaskForm

app = Flask(__name__)
app.secret_key = 'mysecretkey'

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/thanks', methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        website = request.form.get('website')
        address = request.form.get('address')
        subject = request.form.get('subject')
        message = request.form.get('message')
        flash('Your Data is Submitted')
        return '<h1>Your data is submitted</h1>'
    return render_template('home.html')

if __name__ == '__main__':
    app.run()
