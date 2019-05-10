from flask import render_template, url_for

from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/galary')
def galary():
    return render_template('galary.html')
	
@app.route('/menu')
def menu():
    return render_template('menu.html')
	
if __name__ == "__main__":
    app.run(debug=True)