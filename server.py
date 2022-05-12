from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('index.html')


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)



'''@app.route("/<username>/<int:post_id")
def namenum(username=None, post_id=None):
    return render_template('index.html', name=username, post_id)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/blog")
def blog():
    return "<p>Here are my thoughts on blogs</p>"'''

