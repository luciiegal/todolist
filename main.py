import os
import pyfiglet

# We implement a task class to manage the validation of a task
class Task:
    def __init__(self,text):
        self.text=text
        self.validate=False
    
    def validate_task(self):
        self.validate=True
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

    def validate(self,index):
        if index - 1 < len(self.tasks):
            validate_task=self.tasks[index-1].validate_task()
            print(f"The task: '{validate_task.text}' has been validated")
        else:
            print("Invalid task number.")
def main():
    todo_list = ToDoList()

    welcome_page()
    input()
    clear_screen()

    while True:
        clear_screen()
        print("-- Current Tasks --\n")
        todo_list.view_tasks()
        print("\nTo-Do List Application")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. Validate a task")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            clear_screen()
            print("-- Add a task -- \n")
            text = input("Enter a task: ")
            task=Task(text)
            todo_list.add_task(task)
            input("\nPress enter to continue")
        elif choice == '2':
            try:
                clear_screen()
                print("-- Remove a task -- \n")
                print("Current Tasks: ")
                todo_list.view_tasks()
                index = int(input("\nEnter task number to remove: "))
                todo_list.remove_task(index)
                input("\nPress enter to continue")
            except ValueError:
                print("Please enter a valid number.")
                input("\nPress enter to continue")
        elif choice == '3':
            try:
                clear_screen()
                print("-- Validate a task --\n")
                print("Current Tasks: ")
                todo_list.view_tasks()
                index = int(input("\nEnter the number of the task you've accomplished: "))
                todo_list.validate(index)
                input("\nPress enter to continue")
            except ValueError:
                print("Please enter a valid number.")
                input("\nPress enter to continue")
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Press enter to try again.")
            input()

def welcome_page():
    clear_screen()
    #print("Welcome to the To Do list application\n\nCreated by Lucie Gallois\n\nPress enter to start")
    pyfiglet_obj=pyfiglet.Figlet(font="bubble",width=130)
    title=pyfiglet_obj.renderText("TO DO LIST APP")
    print(title)
    print("-- Open Source by Lucie Gallois --\n\nPress enter to continue")

def clear_screen():
    if os.name=='nt':
        _=os.system('cls')

if __name__ == "__main__":
    main()

