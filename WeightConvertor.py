from tkinter import *

root = Tk()
root.geometry("560x200")

def erase_enter_field():
    entry.delete(0, END)


def convert_from_kg():
    gram = f"{float(value.get()) * 1000:.2f}"
    pound = f"{float(value.get()) * 2.20462:.2f}"
    ounce = f"{float(value.get()) * 35.274:.2f}"

    text_grams.delete("1.0", END)
    text_grams.insert(END, gram)

    text_pounds.delete("1.0", END)
    text_pounds.insert(END, pound)

    text_ounce.delete("1.0", END)
    text_ounce.insert(END, ounce)

    erase_enter_field()





Label(root, text="Enter the weight in kg:", font="lucidia 12 bold").grid(row=0, column=0, padx=10, pady=10)
value = StringVar()
entry = Entry(root, textvariable=value)
entry.grid(row=0, column=1)
Label(root, text="Grams", font="lucidia 12 bold").grid(row=1, column=0, padx=10, pady=10)
text_grams = Text(root, height=1, width=20)
text_grams.grid(row=2, column=0,)
Label(root, text="Pounds", font="lucidia 12 bold").grid(row=1, column=1, padx=10, pady=10)
text_pounds = Text(root, height=1, width=20)
text_pounds.grid(row=2, column=1,)
Label(root, text="Ounce", font="lucidia 12 bold").grid(row=1, column=2, padx=10, pady=10)
text_ounce = Text(root,  height=1, width=20)
text_ounce.grid(row=2, column=2, padx=15)
Button(root, text="Convert", height=1, width=9, bg="blue", fg="white", command=convert_from_kg).grid(row=0, column=2, padx=10, pady=10)



mainloop()

