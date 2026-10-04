import tkinter as tk
from tkinter import messagebox
import database


def refresh_list():
    product_list.delete(0, tk.END)
    for row in database.get_products():
        product_list.insert(tk.END, row)


def add_product():
    name = entry_name.get()
    price = entry_price.get()
    quantity = entry_quantity.get()

    if name == "" or price == "" or quantity == "":
        messagebox.showerror("Error", "All fields are required")
        return

    database.add_product(name, float(price), int(quantity))
    refresh_list()
    clear_entries()


def delete_product():
    selected = product_list.get(tk.ACTIVE)
    if selected:
        database.delete_product(selected[0])
        refresh_list()


def update_product():
    selected = product_list.get(tk.ACTIVE)
    if selected:
        database.update_product(
            selected[0],
            entry_name.get(),
            float(entry_price.get()),
            int(entry_quantity.get()),
        )
        refresh_list()
        clear_entries()


def clear_entries():
    entry_name.delete(0, tk.END)
    entry_price.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)


# GUI Setup
root = tk.Tk()
root.title("Shop Management System")
root.geometry("500x400")

tk.Label(root, text="Product Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Price").pack()
entry_price = tk.Entry(root)
entry_price.pack()

tk.Label(root, text="Quantity").pack()
entry_quantity = tk.Entry(root)
entry_quantity.pack()

tk.Button(root, text="Add Product", command=add_product).pack(pady=5)
tk.Button(root, text="Update Product", command=update_product).pack(pady=5)
tk.Button(root, text="Delete Product", command=delete_product).pack(pady=5)

product_list = tk.Listbox(root)
product_list.pack(fill=tk.BOTH, expand=True)

refresh_list()

root.mainloop()
