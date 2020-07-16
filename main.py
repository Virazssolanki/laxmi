from flask import render_template, url_for

from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/gallery')
def gallery():
    return render_template('gallary.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/course')
def course():
    return render_template('course.html')

@app.route('/arts')
def arts():
    return render_template('arts.html')

@app.route('/commerce')
def commerce():
    return render_template('commerce.html')

@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == "__main__":
    app.run(debug=True)

