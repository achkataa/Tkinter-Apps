from Gui_Shop.helpers import clean_screen
from Gui_Shop.canvas import tk
from tkinter import Button, Label
import json
from PIL import Image, ImageTk
import os

base_folder = os.path.dirname(__file__)

def buy_product(button):
    _, product_id = button.cget("text").split()
    product_id = int(product_id)
    current_logged_in_user = None
    with open("db/current_user.txt") as file:
        current_logged_in_user = file.read()

    with open("db/users.txt", "r+") as file:
        users = file.readlines()
        file.seek(0)
        for user in users:
            current_user_as_dict = json.loads(user)
            if current_user_as_dict.get("username") == current_logged_in_user:
                current_user_as_dict["products"].append(product_id)
            file.write(json.dumps(current_user_as_dict))
            file.write("\n")

    with open("db/products.txt", "r+") as file:
        products = file.readlines()
        file.seek(0)
        for product in products:
            current_product_as_dict = json.loads(product)
            if current_product_as_dict["id"] == product_id:
                current_product_as_dict["count"] -= 1
            file.write(json.dumps(current_product_as_dict))
            file.write("\n")

    render_products()


def render_products():
    clean_screen()

    with open("db/products.txt", "r") as file:
        products = file.readlines()
        counter = 0
        for product in products:
            current_product = json.loads(product)
            Label(text=current_product.get("name")).grid(row=0, column=counter)

            image = Image.open(os.path.join(os.path.join(base_folder, "images"), current_product.get("img_path")))
            image = image.resize((100, 100))
            photo = ImageTk.PhotoImage(image)
            img_label = Label(image=photo)
            img_label.image = photo
            img_label.grid(row=1, column=counter)

            button = Button(tk, text=f"Buy {current_product.get('id')}")
            button.configure(command=lambda b=button: buy_product(b))
            button.grid(row=3, column=counter)
            Label(text=f"Count: {current_product.get('count')}").grid(row=2, column=counter)
            counter += 1
