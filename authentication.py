import json
from tkinter import Button, Entry, Label
from Gui_Shop.canvas import tk
from Gui_Shop.helpers import clean_screen
from Gui_Shop.products import render_products


def login(username, password):
    with open("db/user_credentials.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            try:
                usname, pword = line[:-1].split(", ")
            except:
                continue

            if username == usname and pword == password:
                with open("db/current_user.txt", "w") as current_user_file:
                    current_user_file.write(username)
                render_products()
                return

        render_login(erros=True)

def render_login(erros=None):
    clean_screen()
    username = Entry(tk)
    username.grid(row=0, column=0)
    password = Entry(tk)
    password.grid(row=1, column=0)
    Button(tk, text="Enter", command=lambda: login(username=username.get(), password=password.get())).grid(row=2, column=0)

    if erros:
        Label(tk, text="Invalid username or password").grid(row=3, column=0)



def register(**user):
    user.update({"products": []})
    with open("db/users.txt", "a") as file:
        file.write(json.dumps(user))
        file.write("\n")

    with open("db/user_credentials.txt", "a") as file:
        file.write(f"{user.get('username')}, {user.get('password')}")
        file.write("\n")

def render_register():
    clean_screen()
    username = Entry(tk)
    username.grid(row=0, column=0)
    password = Entry(tk, show="*")
    password.grid(row=1, column=0)
    first_name = Entry(tk)
    first_name.grid(row=2, column=0)
    last_name = Entry(tk)
    last_name.grid(row=3, column=0)
    Button(tk, text="Enter", command=lambda: register(username=username.get(), password=password.get(), first_name=first_name.get(), last_name=last_name.get())).grid(row=4, column=0)


def render_main_enter_screen():
    Button(tk, text="Login", bg="blue", fg="white", command=render_login).grid(row=0, column=0)
    Button(tk, text="Register", bg="red", fg="white", command=render_register).grid(row=0, column=1)