import tkinter as tk
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


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.todo_list = TodoList()
        self.create_widgets()

    def create_widgets(self):
        self.task_entry = tk.Entry(self.root, width=50)
        self.task_entry.pack(pady=10)
        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)
        self.tasks_frame = tk.Frame(self.root)
        self.tasks_frame.pack(pady=10)
        self.update_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.todo_list.add_task(task)
            self.task_entry.delete(0, tk.END)
            self.update_tasks()

    def update_tasks(self):
        for widget in self.tasks_frame.winfo_children():
            widget.destroy()
        for idx, task in enumerate(self.todo_list.tasks, start=1):
            task_str = (
                f"{idx}. {task['task']} - {'Done' if task['completed'] else 'Not Done'}"
            )
            tk.Label(self.tasks_frame, text=task_str).pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
