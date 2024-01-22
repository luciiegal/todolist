import os

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task added: {task}")
        clear_screen()

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
            return
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")
        

    def remove_task(self, index):
        if index - 1 < len(self.tasks):
            removed_task = self.tasks.pop(index - 1)
            print(f"Removed task: {removed_task}")
            clear_screen()
        else:
            print("Invalid task number.")

def main():
    todo_list = ToDoList()

    welcome_page()
    input()
    clear_screen()

    while True:
        print("\nTo-Do List Application")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter a task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            try:
                index = int(input("Enter task number to remove: "))
                todo_list.remove_task(index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

def welcome_page():
    print("Welcome to the To Do list application\n\nCreated by Lucie Gallois\n\nPress enter to start")

def clear_screen():
    if os.name=='nt':
        _=os.system('cls')

if __name__ == "__main__":
    main()

