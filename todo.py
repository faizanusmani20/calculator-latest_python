tasks =[]


while True:

    print("\n 1.Add Task")
    print("2.View Task")

    choice=int(input("Enter the choice: "))

    if choice == 1:
        task=input("Enter task: ")
        tasks.append(task)

    elif choice == 2:
        for i, tasks in enumerate(task,start=1):
            print(i,task)
