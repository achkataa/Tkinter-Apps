from tkinter import *
import tkinter.messagebox as tsmg
import smtplib
root = Tk()
root.geometry("500x500")

def clear_view(tk):
    for s in tk.grid_slaves():
        s.destroy()

def send_email(mail):
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login("achkatabachkata@gmail.com", "achkatabachkadosta")
        subject = "Achkata Airlines"
        body = "Thank you for working we us.It's been a pleasure.We hope you have a great holiday"

        msg = f"Subject: {subject}\n\n{body}"

        smtp.sendmail("achkatabachkata@gmail.com", f"{mail}", msg)

def show_ticket(tk, name, surname, email):
    tsmg.showinfo("Achkata Airlines", f"So, we are booking your flight to {var.get()}\nWe wish you a happy journey.Thanks for booking with us\nName: {name}\nSurname: {surname}\nEmail: {email}\nYou will receive further information on your email")
    send_email(email)



def book_tickets(tk, country):
    clear_view(tk)
    Label(root, text="First Name", font="lucidia 15 bold").grid(row=0, column=0, padx=20, pady=20)
    name = Entry(tk)
    name.grid(row=0, column=1, padx=20, pady=20)
    Label(root, text="Surname", font="lucidia 15 bold").grid(row=1, column=0, padx=20, pady=20)
    surname = Entry(tk)
    surname.grid(row=1, column=1, padx=20, pady=20)
    Label(root, text="Email", font="lucidia 15 bold").grid(row=2, column=0, padx=20, pady=20)
    email = Entry(tk)
    email.grid(row=2, column=1, padx=20, pady=20)
    Label(root, text="How would you like to pay:", font="lucidia 15 bold").grid(row=3, column=0, padx=20, pady=20)
    pay = StringVar
    Checkbutton(tk, text="Card", variable=pay).grid(row=4, column=0, padx=20, pady=20)
    Checkbutton(tk, text="Cash", variable=pay).grid(row=4, column=1, padx=20, pady=20)
    Button(root, text="Send Request", bg="blue", fg="white",command=lambda: show_ticket(tk, name=name.get(), surname=surname.get(), email=email.get())).grid(row=6, column=1, padx=70, pady=20)
    Button(root, text="Home Page", bg="red", fg="white",command=lambda: render_main_view(tk)).grid(row=6, column=0, padx=70, pady=20)



var = StringVar()

def render_main_view(tk):
    clear_view(tk)
    Label(root, text="Where do you want to travel", font="lucidia 19 bold").grid(row=0, column=1, padx=70, pady=20)
    new_var = var.set("nonewhere")
    Radiobutton(root, text="Australia", value="Australia", variable=var).grid(row=1, column=1, padx=70, pady=20)
    Radiobutton(root, text="Germany", value="Germany", variable=var).grid(row=2, column=1, padx=70, pady=20)
    Radiobutton(root, text="China", value="China", variable=var).grid(row=3, column=1, padx=70, pady=20)
    Radiobutton(root, text="Italy", value="Italy", variable=var).grid(row=4, column=1, padx=70, pady=20)
    Radiobutton(root, text="England", value="England", variable=var).grid(row=5, column=1, padx=70, pady=20)
    Button(root, text="Book your tickets", bg="blue", fg="white", command=lambda: book_tickets(tk, country=var.get())).grid(row=6, column=1, padx=70, pady=20)



render_main_view(root)


mainloop()
