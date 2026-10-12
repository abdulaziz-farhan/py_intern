import json, os

file = "tasks.json"
tasks = json.load(open(file)) if os.path.exists(file) else []

while True:
    c = input("1.Add 2.List 3.Done 4.Delete 5.Exit: ")
    if c == "1":
        tasks.append({"task":input("Task: "), "done":False})
    elif c == "2":
        for i,t in enumerate(tasks,1):
            print(i, t["task"], "Done" if t["done"] else "Pending")
    elif c in ("3","4"):
        try:
            i = int(input("Task number: "))-1
            if c == "3": tasks[i]["done"] = True
            else: tasks.pop(i)
        except (ValueError, IndexError):
            print("Invalid task number")
    elif c == "5":
        break
    else:
        print("Invalid choice")
    with open(file,"w") as f:
        json.dump(tasks,f)