from flask import Flask, render_template
from utils.download_world import download_world
from utils.world_parser import world
# app = Flask(__name__)

# @app.route("/")
# def index():
#     return render_template("index.html")


# app.run()

x = world()

print(x[25:30])