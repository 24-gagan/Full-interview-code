import os

with open("gagan.txt", "w") as f:
    f.write(("My name is gagan"))
    f.write("I am hardworking")
    f.write("I know the code")
    f.write("I am good at coding")
    f.write("Dont mess with me")
with open("gagan.txt", "r") as f:
    print(f.read())
with open("gagan.txt", "a") as f:
    f.write("This line for append")
    print(f)
if os.path.exists("gagan.txt"):
    os.rename("gagan.txt", "singh.txt")
    print("rename success")
else:
    print("rename not successfull")

os.mkdir("old_folder")
