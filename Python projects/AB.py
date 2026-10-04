with open("ria.txt","r") as f:
    content=f.read()
    print(content)

with open("ria.txt","w") as f:
    f.write("my name is gagan")
