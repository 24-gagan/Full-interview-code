todo=[]

while True:
    print("1.Add 2.View 3.Remove 4.quit ")
    choice=input("enter the choice")

    if choice=="1":
        task=input("enter the task")
        todo.append(task)
        print("task added")

    elif choice=="2":
        for i,t in enumerate(todo,1):
            print(i,t)

    elif choice=="3":
        num=int(input("enter the number"))
        todo.pop(num-1)
        print("task removed")

    elif choice=="4":
        break

    else:
        print("invalid choice")