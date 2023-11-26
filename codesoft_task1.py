import tkinter as tk

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.tasks = []

        # Create the user interface
        self.task_entry = tk.Entry(root)
        self.task_entry.pack()

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(root)
        self.task_listbox.pack()

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.task_listbox.delete(selected_index)
            del self.tasks[selected_index[0]]

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
