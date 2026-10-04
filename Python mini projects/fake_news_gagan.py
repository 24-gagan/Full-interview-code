import random

subjects = [
    "virat",
    "sachin",
    "rohit",
    "dhoni",
    "jadeja",
    "ganguli",
    "shahrukh",
    "jimmi",
    "sunny",
    "diljeet",
    "modi",
]
actions = ["cricket", "bollywood", "politicion"]
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


def fake_news():
    subject = random.choice(subjects)
    object = random.choice(objects)
    action = random.choice(actions)
    place = random.choice(places)
    headline = f"Breaking News {subject} {object} {action} {place}"
    return headline


for i in range(5):
    print(fake_news())
