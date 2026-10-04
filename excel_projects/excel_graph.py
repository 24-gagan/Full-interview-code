import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("input.xlsx")  # jo Excel maine tumhe diya tha

plt.bar(df["Name"], df["Age"])
plt.xlabel("Name")
plt.ylabel("Age")
plt.title("Age of Employees")

plt.show()
