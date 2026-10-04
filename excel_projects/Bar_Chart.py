import matplotlib.pyplot as plt

names = ["A", "B", "C", "D"]
marks = [70, 85, 60, 90]
plt.bar(names, marks)
plt.xlabel("Student")
plt.ylabel("Marks")
plt.title("Marks Bar Graph")
plt.show()
