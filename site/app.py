from flask import Flask, render_template, request
from kyujipy import KyujitaiConverter
import kyujipy

converter = KyujitaiConverter()
app = Flask(__name__)


@app.route("/home")
@app.route("/")
def index():
    items = ["item2","your mum","python"]
    return render_template("index.html")

@app.route("/about/<username>")
def about_page(username):
    return "<h1>This is the about page of, {} </h1>".format(username)

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = converter.shinjitai_to_kyujitai(text)
    return render_template("index.html",processed_text=processed_text)