import tkinter as tk
from tkinter import messagebox
import os

tasks = []
FILE_NAME = "tasks.txt"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                tasks.append(line.strip())

# Save tasks to file
def save_tasks():
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")
    messagebox.showinfo("Saved", "Tasks saved successfully!")

# Update the listbox
def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

def add_task():
    task = entry_task.get().strip()
    if task:
        tasks.append(task)
        update_listbox()
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        tasks.pop(selected)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def update_task():
    try:
        selected = listbox.curselection()[0]
        new_task = entry_task.get().strip()
        if new_task:
            tasks[selected] = new_task
            update_listbox()
            entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter new task text.")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update.")

# Window setup
root = tk.Tk()
root.title("To-Do List App")
root.geometry("420x480")
root.config(bg="#e1f5fe")

# Widgets
frame = tk.Frame(root, bg="#e1f5fe")
frame.pack(pady=10)

entry_task = tk.Entry(frame, width=25, font=("Arial", 14))
entry_task.grid(row=0, column=0, padx=5)

btn_add = tk.Button(frame, text="Add", command=add_task, bg="#4caf50", fg="white")
btn_add.grid(row=0, column=1, padx=5)

btn_update = tk.Button(frame, text="Update", command=update_task, bg="#2196f3", fg="white")
btn_update.grid(row=0, column=2, padx=5)

btn_delete = tk.Button(frame, text="Delete", command=delete_task, bg="#f44336", fg="white")
btn_delete.grid(row=0, column=3, padx=5)

listbox = tk.Listbox(root, width=40, height=15, font=("Arial", 12), selectbackground="#a5d6a7")
listbox.pack(pady=10)

btn_save = tk.Button(root, text="Save Tasks", command=save_tasks, bg="#ff9800", fg="white", font=("Arial", 12))
btn_save.pack(pady=5)

# Load saved tasks at start
load_tasks()
update_listbox()

# Start GUI
root.mainloop()
