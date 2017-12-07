

from flask import Flask, render_template
import random


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    animals = ["cat", "dog", "panda", "MiraeN"]
    msg = random.choice(animals)
    return render_template("about.html", msg=msg)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
