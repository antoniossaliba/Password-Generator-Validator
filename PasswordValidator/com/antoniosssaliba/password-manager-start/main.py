from tkinter import *
import random as rnd
import json

def generatePassword():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*"
    generated_password = str()
    for i in range(26):
        random_character = characters[rnd.randint(0, len(characters) - 1)]
        generated_password += random_character
    password_entry.delete(0, END)
    password_entry.insert(END, generated_password)

def add_to_file():
    added_successfully_label.config(text="")
    missing_website_label.config(text="")
    missing_email_username_label.config(text="")
    missing_password_label.config(text="")
    new_data = {
        website_entry.get(): {
            "email": email_username_entry.get(),
            "password": password_entry.get()
        }
    }
    website_is_empty = False
    email_username_is_empty = False
    password_is_empty = False
    if website_entry.get() == "" or website_entry.get() == "Missing website name":
        website_is_empty = True
        missing_website_label.config(text="Website name missing!", fg="red")
        website_entry.delete(0, END)
        website_entry.insert(END, "Missing website name")
    if email_username_entry.get() == "" or email_username_entry.get() == "Missing username/password":
        email_username_is_empty = True
        missing_email_username_label.config(text="Missing email/username!", fg="red")
        email_username_entry.delete(0, END)
        email_username_entry.insert(END, "Missing username/password")
    if password_entry.get() == "" or password_entry.get() == "Missing password":
        password_is_empty = True
        missing_password_label.config(text="Missing password!", fg="red")
        password_entry.delete(0, END)
        password_entry.insert(END, "Missing password")
    if not website_is_empty and not email_username_is_empty and not password_is_empty:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=10)
        except:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=10)
        website_entry.delete(0, END)
        email_username_entry.delete(0, END)
        password_entry.delete(0, END)
        added_successfully_label.config(text="Data saved successfully!", fg="green")
    else:
        added_successfully_label.config(text="Make sure to fill all entries!", fg="red")

def search_for_password():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            try:
                email = data[website_entry.get()]["email"]
                password = data[website_entry.get()]["password"]
                added_successfully_label.config(text="")
                missing_website_label.config(text="Website searched for was found!", fg="green")
                missing_email_username_label.config(text="Username/Email found!", fg="green")
                email_username_entry.delete(0, END)
                email_username_entry.insert(END, email)
                missing_password_label.config(text="Password found!", fg="green")
                password_entry.delete(0, END)
                password_entry.insert(END, password)
            except KeyError:
                missing_website_label.config(text="Website searched for does not exist!", fg="red")
                missing_email_username_label.config(text="Username/Email not found!", fg="red")
                email_username_entry.delete(0, END)
                missing_password_label.config(text="Password found!", fg="red")
                password_entry.delete(0, END)
                added_successfully_label.config(text="")
    except FileNotFoundError:
        missing_website_label.config(text="Database not accessible!", fg="red")

window = Tk()
window.title("Password Generator/Validator")
window.config(width=500, height=500)
window.maxsize(500, 500)
window.minsize(500, 500)

canvas = Canvas()
image = PhotoImage(file="logo.png")
canvas.create_image(200, 189, image=image)
canvas.place(x=50, y=-40)

website_keyword_label = Label(text="Website:", font=("Courier", 10, "bold"))
website_keyword_label.place(x=30, y=260)

email_username_keywords_label = Label(text="Email/Username:", font=("Courier", 10, "bold"))
email_username_keywords_label.place(x=30, y=310)

password_keyword_label = Label(text="Password:", font=("Courier", 10, "bold"))
password_keyword_label.place(x=30, y=360)

website_entry = Entry()
website_entry.config(width=35)
website_entry.place(x=200, y=260)

email_username_entry = Entry()
email_username_entry.config(width=35)
email_username_entry.place(x=200, y=310)

password_entry = Entry()
password_entry.config(width=35)
password_entry.place(x=200, y=360)

generate_password_button = Button(text="Generate Password", width=21, font=("Courier", 8, "bold"), command=generatePassword)
generate_password_button.place(x=200, y=410)

add_button = Button(text="Add", width=21, font=("Courier", 8, "bold"), command=add_to_file)
add_button.place(x=200, y=440)

search_button = Button(text="Search", font=("Courier", 8, "bold"), width=21, command=search_for_password)
search_button.place(x=30, y=410)

missing_website_label = Label(text="", font=("Courier", 10, "bold"), fg="red")
missing_website_label.place(x=200, y=280)

missing_email_username_label = Label(text="", font=("Courier", 10, "bold"), fg="red")
missing_email_username_label.place(x=200, y=330)

missing_password_label = Label(text="", font=("Courier", 10, "bold"), fg="red")
missing_password_label.place(x=200, y=380)

added_successfully_label = Label(text="", font=("Courier", 10, "bold"))
added_successfully_label.place(x=200, y=470)

window.mainloop()