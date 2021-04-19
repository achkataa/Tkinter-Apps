from tkinter import *

root = Tk()
root.title("Simple Calculator")

entry = Entry(root, width = 35, borderwidth = 5)
entry.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)



def click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))

def clear():
    entry.delete(0, END)

def plus():
    first_number = entry.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    entry.delete(0, END)




def equals():
    second_number = entry.get()
    entry.delete(0, END)

    if math == "addition":
        global history_add
        history_add = f"{f_num} + {second_number}"
        entry.insert(0, f_num + int(second_number))
    if math == "subtraction":
        global history_subtract
        history_subtract = f"{f_num} - {second_number}"
        entry.insert(0, f_num - int(second_number))
    if math == "multiplication":
        global history_multiply
        history_multiply = f"{f_num} * {second_number}"
        entry.insert(0, f_num * int(second_number))
    if math == "divison":
        global history_divide
        history_divide = f"{f_num} / {second_number}"
        entry.insert(0, f_num / int(second_number))


def subtract():
    first_number = entry.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    entry.delete(0, END)

def multiply():
    first_number = entry.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    entry.delete(0, END)

def divide():
    first_number = entry.get()
    global f_num
    global math
    math = "divison"
    f_num = int(first_number)
    entry.delete(0, END)

def history():
    if math == "addition":
        label_add = Label(root, text = f"Add: {history_add}")
        label_add.grid(row = 1, column = 3)
    if math == "subtraction":
        label_subtract = Label(root, text = f"Subtract: {history_subtract}")
        label_subtract.grid(row = 2, column = 3)
    if math == "multiplication":
        label_subtract = Label(root, text = f"Multiply: {history_multiply}")
        label_subtract.grid(row = 3, column = 3)
    if math == "divison":
        label_subtract = Label(root, text = f"Divide: {history_divide}")
        label_subtract.grid(row = 4, column = 3)






#define buttons
button1 = Button(root, text = "1", padx = 40, pady = 20, command =lambda: click(1))
button2 = Button(root, text = "2", padx = 40, pady = 20, command =lambda: click(2))
button3 = Button(root, text = "3", padx = 40, pady = 20, command =lambda: click(3))
button4 = Button(root, text = "4", padx = 40, pady = 20, command =lambda: click(4))
button5 = Button(root, text = "5", padx = 40, pady = 20, command =lambda: click(5))
button6 = Button(root, text = "6", padx = 40, pady = 20, command =lambda: click(6))
button7 = Button(root, text = "7", padx = 40, pady = 20, command =lambda: click(7))
button8 = Button(root, text = "8", padx = 40, pady = 20, command =lambda: click(8))
button9 = Button(root, text = "9", padx = 40, pady = 20, command =lambda: click(9))
button0 = Button(root, text = "0", padx = 40, pady = 20, command =lambda: click(0))

button_plus = Button(root, text = "+", padx = 39, pady = 20, command = plus)
button_equals = Button(root, text = "=", padx = 86, pady = 20, command = equals)
button_clear = Button(root, text = "Clear", padx = 77, pady = 20, command = clear)

button_subtract = Button(root, text = "-", padx = 41, pady = 20, command = subtract)
button_multiply = Button(root, text = "*", padx = 40, pady = 20, command = multiply)
button_divide = Button(root, text = "/", padx = 40, pady = 20, command = divide)

history_button = Button(root, text = "History", padx = 79, pady = 20, command = history)


#add buttons to the screen
button1.grid(row = 3, column = 0)
button2.grid(row = 3, column = 1)
button3.grid(row = 3, column = 2)

button4.grid(row = 2, column = 0)
button5.grid(row = 2, column = 1)
button6.grid(row = 2, column = 2)

button7.grid(row = 1, column = 0)
button8.grid(row = 1, column = 1)
button9.grid(row = 1, column = 2)

button0.grid(row = 4, column = 0)
button_clear.grid(row = 4, column = 1, columnspan = 2)
button_plus.grid(row = 5, column = 0)
button_equals.grid(row = 5, column = 1, columnspan = 2)

button_subtract.grid(row = 6, column = 0)
button_multiply.grid(row = 6, column = 1)
button_divide.grid(row = 6, column = 2)

history_button.grid(row = 0, column = 3)




root.mainloop()
