tasks = []

def add_task(task):
    tasks.append(task)
    print("Added task: {}".format(task))  # Changed f-string to .format() as f-strings were introduced in Python 3.6

def remove_task(index):
    if 0 <= index < len(tasks):
        print("Removed task: {}".format(tasks.pop(index)))  # Changed f-string to .format()
    else:
        print("Invalid index")

def list_tasks():
    print("\nTo-Do List:")
    for i, task in enumerate(tasks):
        print("{}. {}".format(i + 1, task))  # Changed f-string to .format()

if __name__ == "__main__":
    add_task("Learn Python")
    add_task("Build a project")
    list_tasks()
    remove_task(0)
    list_tasks()