tasks=[]
while True:
    mode=int(input("1:add task 2:read tasks 3:exit:"))
    if mode==1:
         task=input("Add a task:")
         tasks.append(task)
    elif mode==2:
        print(tasks)
        print("Total tasks:",len(tasks))
    elif mode==3:
        print("Goodbye!")
        break
    else :
        print("Invalid number!")
