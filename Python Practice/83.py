with open("example.txt","w")as file:
    file.write("Hello world")
with open("example.txt","r")as file:
    print(file.read())
with open("example.txt","a") as file:
    file.write("appending more content")
with open("example.txt","r") as file:
    print(file.read())
with open("example.txt","r")as file:
    lines=file.readline()
    print(lines)