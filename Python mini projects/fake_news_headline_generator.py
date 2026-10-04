import random

subjects = [
    "Local Cat",
    "Tech Startup",
    "Village Boy",
    "AI Robot",
    "College Student",
    "Street Dog",
    "Office Manager",
    "School Teacher",
]

actions = [
    "discovers",
    "accidentally creates",
    "wins",
    "loses",
    "invents",
    "breaks",
    "challenges",
    "questions",
]

objects = [
    "a time machine",
    "free Wi-Fi for life",
    "a secret shortcut to success",
    "a magical phone app",
    "a flying bicycle",
    "an invisible umbrella",
    "a robot teacher",
    "a smart dustbin",
]

places = [
    "in Delhi",
    "in a small town",
    "inside an office",
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
    headline = f"Breaking News: {subject} {action} {obj} {place}!"
    return headline


for i in range(5):
    print(generate_fake_news())
