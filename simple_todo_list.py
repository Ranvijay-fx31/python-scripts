tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Added task: {task}")

def remove_task(index):
    if 0 <= index < len(tasks):
        print(f"Removed task: {tasks.pop(index)}")
    else:
        print("Invalid index")

def list_tasks():
    print("\nTo-Do List:")
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task}")

if __name__ == "__main__":
    add_task("Learn Python")
    add_task("Build a project")
    list_tasks()
    remove_task(0)
    list_tasks()
