print("\nHell0 !!\n")
print("Welcome to my task:01 Simple To-Do-List\n")
print("Let's get started....\n")

def display_todo_list(todo_list):
    print("To-Do List:")
    for index, task in enumerate(todo_list, start=1):
        print(f"{index}. {task}")
    print()

def add_task(todo_list, task):
    todo_list.append(task)
    print(f"Task '{task}' added to the to-do list.")
    print()


def remove_task(todo_list, task_index):
    if 1 <= task_index <= len(todo_list):
        removed_task = todo_list.pop(task_index - 1)
        print(f"Task '{removed_task}' removed from the to-do list.")
    else:
        print("Invalid task index. Please enter a valid index.")
    print()

def main():
    todo_list = []

    while True:
        print("1. Display To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Quit\n")

        choice = input("Enter your choice (1-4): \n")

        if choice == "1":
            display_todo_list(todo_list)
        elif choice == "2":
            task = input("Enter the task: ")
            add_task(todo_list, task)
        elif choice == "3":
            task_index = int(input("\nEnter the index of the task to remove: "))
            remove_task(todo_list, task_index)
        elif choice == "4":
            print("\nExiting the to-do list application.")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
print("\nHope this was useful to you!! \n\nThank you :)\n\n")