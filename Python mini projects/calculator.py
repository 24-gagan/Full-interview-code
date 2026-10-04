import tkinter as tk


def add_numbers():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result_label.config(text=f"Result: {num1 + num2}")


# Window setup
root = tk.Tk()
root.title("Simple Calculator")

# Widgets
entry1 = tk.Entry(root)
entry1.pack()

entry2 = tk.Entry(root)
entry2.pack()

add_button = tk.Button(root, text="Add", command=add_numbers)
add_button.pack()

result_label = tk.Label(root, text="Result: ")
result_label.pack()

root.mainloop()
