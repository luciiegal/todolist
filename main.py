import os
import pyfiglet
import readchar

class Task:
    def __init__(self, text):
        self.text = text
        self.validate = False
    
    def validate_task(self):
        self.validate = True
        return self
    
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task added: {task.text}, validate: {task.validate}")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
            return
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task.text}, validate: {task.validate}")

    def remove_task(self, index):
        if index - 1 < len(self.tasks):
            removed_task = self.tasks.pop(index - 1)
            print(f"Removed task: {removed_task.text}")
        else:
            print("Invalid task number.")

    def validate_task_by_index(self, index):
        if index - 1 < len(self.tasks):
            validate_task = self.tasks[index - 1].validate_task()
            print(f"The task: '{validate_task.text}' has been validated")
        else:
            print("Invalid task number.")

def welcome_page():
    clear_screen()
    title = pyfiglet.figlet_format("TO DO LIST APP", font="starwars")
    print(title)
    print("-- Open Source by Lucie Gallois --\n\nPress any key to continue")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    todo_list = ToDoList()
    welcome_page()
    readchar.readkey()  # To proceed from welcome page
    clear_screen()

    options = ["Add a task", "Remove a task", "Validate a task", "Exit"]
    current_option = 0

    while True:
        clear_screen()
        print("-- Current Tasks --\n")
        todo_list.view_tasks()

        print("\nTo-Do List Application")
        for index, option in enumerate(options):
            prefix = ">> " if index == current_option else "   "
            print(f"{prefix}{option}")

        key = readchar.readkey()
        if key == readchar.key.UP and current_option > 0:
            current_option -= 1
        elif key == readchar.key.DOWN and current_option < len(options) - 1:
            current_option += 1
        elif key == readchar.key.ENTER:
            if current_option == 0:
                clear_screen()
                task_text = input("Enter a task: ")
                todo_list.add_task(Task(task_text))
                readchar.readkey()
            elif current_option == 1:
                clear_screen()
                todo_list.view_tasks()
                try:
                    index = int(input("\nEnter task number to remove: "))
                    todo_list.remove_task(index)
                except ValueError:
                    print("Please enter a valid number.")
                readchar.readkey()
            elif current_option == 2:
                clear_screen()
                todo_list.view_tasks()
                try:
                    index = int(input("\nEnter the number of the task you've accomplished: "))
                    todo_list.validate_task_by_index(index)
                except ValueError:
                    print("Please enter a valid number.")
                readchar.readkey()
            elif current_option == 3:
                print("Exiting the application.")
                break

if __name__ == "__main__":
    main()