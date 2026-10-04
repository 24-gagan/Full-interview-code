from flask import Flask, render_template, request
import random

app = Flask(__name__)

subjects = [
    "Virat",
    "Sachin",
    "Rohit",
    "Dhoni",
    "Jadeja",
    "Ganguly",
    "Shah Rukh",
    "Sunny",
    "Diljit",
    "Modi",
]

actions = ["cricket", "bollywood", "politics"]

objects = [
    "a time machine",
    "free Wi-Fi for life",
    "a magical phone app",
    "a flying bicycle",
    "an invisible umbrella",
    "a robot teacher",
    "a smart dustbin",
]

places = [
    "in Delhi",
    "at the railway station",
    "in a classroom",
    "at a tea stall",
    "during lunch break",
]


def generate_fake_news():
    subject = random.choice(subjects)
    action = random.choice(actions)
    obj = random.choice(objects)
    place = random.choice(places)
    return f"Breaking News: {subject} related to {action} uses {obj} {place}!"


@app.route("/", methods=["GET", "POST"])
def home():
    headline = None
    if request.method == "POST":
        headline = generate_fake_news()
    return render_template("index.html", headline=headline)


if __name__ == "__main__":
    app.run(debug=True)
