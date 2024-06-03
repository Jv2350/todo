import json


class TodoList:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file)

    def add_task(self, task, priority="Medium"):
        task_entry = {"task": task, "completed": False, "priority": priority}
        self.tasks.append(task_entry)
        self.save_tasks()

    def view_tasks(self):
        for idx, task in enumerate(self.tasks, start=1):
            status = "✓" if task["completed"] else "✗"
            print(f"{idx}. {task['task']} [{status}]")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            del self.tasks[task_number - 1]
            self.save_tasks()

    def complete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            self.save_tasks()

    def edit_task(self, task_number, new_task):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["task"] = new_task
            self.save_tasks()


def print_menu():
    print("\nTo-Do List Menu")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Complete task")
    print("5. Exit")
    print("6. Edit")


def main():
    todo_list = TodoList()
    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter a new task: ")
            priority = input("Enter priority (High, Medium, Low): ")
            todo_list.add_task(task, priority)

        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            task_number = int(input("Enter the task number to delete: "))
            todo_list.delete_task(task_number)
        elif choice == "4":
            task_number = int(input("Enter the task number to mark as complete: "))
            todo_list.complete_task(task_number)
        elif choice == "5":
            break
        elif choice == "6":
            task_number = int(input("Enter the task number to edit: "))
            new_task = input("Enter the new task description: ")
            todo_list.edit_task(task_number, new_task)
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
