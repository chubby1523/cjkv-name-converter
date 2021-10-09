from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
    items = ["item2","your mum","python"]
    return render_template("index.html",items=items)

@app.route("/about/<username>")
def about_page(username):
    return "<h1>This is the about page of, {} </h1>".format(username)
