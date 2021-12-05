from flask import Flask, render_template


# create a Flask instance
app = Flask(__name__)

# create a route decorator

@app.route('/')
def index():
    return '<h1> Hello World!</h1>'


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500