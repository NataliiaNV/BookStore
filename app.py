from flask import Flask, render_template, flash, request, redirect, url_for


# create a Flask instance
app = Flask(__name__)

app.config['SECRET_KEY'] = 'my secret key'

# create a route decorator
@app.route('/')
def index():
    flash('Welcome to our website')
    return render_template('home.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500