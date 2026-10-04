import random
import tkinter as tk

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

    headline = f"Breaking News: {subject} related to {action} uses {obj} {place}!"
    result_label.config(text=headline)


# Tkinter App
root = tk.Tk()
root.title("Fake News Generator (Satire)")
root.geometry("600x300")

title_label = tk.Label(
    root, text="📰 Fake News Generator (Satirical)", font=("Arial", 16, "bold")
)
title_label.pack(pady=10)

result_label = tk.Label(
    root,
    text="Click the button to generate a fake news headline",
    wraplength=550,
    justify="center",
    font=("Arial", 12),
)
result_label.pack(pady=20)

generate_button = tk.Button(
    root,
    text="Generate Fake News",
    command=generate_fake_news,
    font=("Arial", 12),
    padx=20,
    pady=10,
)
generate_button.pack(pady=10)

root.mainloop()
