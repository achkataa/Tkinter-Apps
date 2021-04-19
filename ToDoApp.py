from tkinter.ttk import *
from tkinter import *
from tkcalendar import DateEntry
from tkinter.scrolledtext import *
import json

all_tasks_to_write = []


def get_all_tasks_from_file():
    with open("db.txt", "r") as file:
        try:
            existing_tasks = json.load(file)
        except json.decoder.JSONDecodeError:
            existing_tasks = []
    return existing_tasks

def write_tasks_to_file(all_tasks, existing_tasks=None):
    with open("db.txt", "r+") as file:
        if not existing_tasks:
            existing_tasks = get_all_tasks_from_file()
        file.seek(0)
        file.truncate()
        all_tasks_to_write.extend(existing_tasks)
        json.dump(all_tasks_to_write, file)

def clear_view(tk):
    for s in tk.grid_slaves():
        s.destroy()

def delete_task(tk, value):
    existing_tasks = get_all_tasks_from_file()
    existing_tasks.remove(eval(value))
    write_tasks_to_file(all_tasks_to_write, existing_tasks)

def render_list_task_view(tk):
    clear_view(tk)
    box = Combobox(tk, width=100)
    existing_tasks = get_all_tasks_from_file()

    box["values"] = existing_tasks
    box.grid(row=0, column=0)
    Button(tk, text="Delete", bg="red", command=lambda: delete_task(tk, box.get())).grid(row=1, column=0, pady=20)

def create_task(**kwargs):
    all_tasks_to_write.append(kwargs)

def render_create_task_view(tk):
    clear_view(tk)
    Label(tk, text="Enter your task name: ").grid(row=0, column=0, padx=20, pady=20)
    task_name = Entry(tk)
    task_name.grid(row=0, column=1, padx=20, pady=20)
    Label(tk, text="Due Date").grid(row=1, column=0, padx=20, pady=20)
    date = DateEntry(tk)
    date.grid(row=1, column=1)
    Label(tk, text="Description: ").grid(row=2, column=0, padx=20, pady=20)
    description = ScrolledText(tk, width=20, height=10)
    description.grid(row=2, column=1)
    Label(tk, text="Select Priority: ").grid(row=3, column=0, padx=20, pady=20)
    select_priority_num = IntVar()
    Radiobutton(tk, text="Low", value=1, variable=select_priority_num).grid(row=3, column=1, padx=20, pady=20)
    Radiobutton(tk, text="Mid", value=2, variable=select_priority_num).grid(row=3, column=2, padx=20, pady=20)
    Radiobutton(tk, text="High", value=3, variable=select_priority_num).grid(row=3, column=3, padx=20, pady=20)
    Label(tk, text="Check if completed: ").grid(row=4, column=0, padx=20, pady=20)
    is_completed = BooleanVar()
    Checkbutton(tk, text="Checked", variable=is_completed).grid(row=4, column=1, padx=20, pady=20)
    Button(tk, text="Create Tasks", bg="red", fg="white", command=lambda: create_task(name=task_name.get(), date=date.get(), description=description.get("1.0", END), priority=select_priority_num.get(), is_complete=is_completed.get())).grid(row=5, column=0, padx=20, pady=50)


def render_main_view(tk):
    Button(tk, text="List Tasks", bg="blue", fg="white", command=lambda: render_list_task_view(tk)).grid(row=0, column=0, padx=150, pady=200)
    Button(tk, text="Create Tasks", bg="red", fg="white", command=lambda: render_create_task_view(tk)).grid(row=0, column=1, padx=100, pady=200)

tk = Tk()
tk.geometry("700x500")
render_main_view(tk)

tk.mainloop()

write_tasks_to_file(all_tasks_to_write)
