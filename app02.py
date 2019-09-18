from flask import Flask, render_template
from data import Articles


app02 = Flask(__name__)
Articles = Articles()

@app02.route('/')
def index():
    return render_template('index.html')

@app02.route('/about')
def about():
    return render_template('about.html')

@app02.route('/articles')
def articles():
    return render_template('articles.html', articles=Articles)

if __name__ == '__main__':
    app02.run(debug=True)