from flask import Flask, redirect, url_for
from time import sleep

app = Flask(__name__)

@app.route("/")
def home():
    sleep(5)
    return redirect(url_for("after_click"))

@app.route("/after_click")
def after_click():
    return "Button Clicked"
app.run()