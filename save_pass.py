import os.path
from tkinter import *
from tkinter import messagebox, scrolledtext
from random import choice, shuffle
import pyperclip
from nacl import secret
import base64

# Password Generation and Storage mechanism.

DARK_GREY = "#3C3D37"
WHITE = "#ffffff"


def password_saver(given_key):

    # Takes Key(Set by the User) as the Input(in byte form). The Parameter is provided my the Login Function's Output

    byte_key = given_key


    # ---------------------------- PASSWORD GENERATOR ------------------------------- #

    def gen_pass():
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                   't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                   'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        letters_list = [choice(letters) for _ in range(int(letters_slider.get()))]
        symbols_list = [choice(numbers) for _ in range(int(numbers_slider.get()))]
        numbers_list = [choice(symbols) for _ in range(int(symbols_slider.get()))]

        password_list = letters_list + symbols_list + numbers_list

        shuffle(password_list)

        password = "".join(password_list)

        pass_entry.delete(0, END)
        pass_entry.insert(0, password)
        pyperclip.copy(password)

    # ---------------------------- SAVE PASSWORD ------------------------------- #

    def encrypt(key, text):
        # This encrypt functions works to Encrypt the Info string before passing the output
        box = secret.SecretBox(key)
        encrypted = box.encrypt(text)
        return encrypted

    def decrypt(key, encrypted):
        # This decrypt function works to Decrypt the data from the file so that it can be read
        box = secret.SecretBox(key)
        decrypted = box.decrypt(encrypted)
        data = decrypted.decode('utf-8')
        return data

    def save_info():
        """Check what the User has input in the fields and then stores it in an info string"""
        website = website_entry.get()
        email = e_u_entry.get()
        password = pass_entry.get()
        info = f"{website} | {email} | {password}\n"

        if len(website) == 0 or len(password) == 0 or len(email) == 0:
            messagebox.showinfo(title="Error", message="Please don't leave any of the fields empty!")
        else:
            is_good = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail:"
                                                                    f" {email}\nPassword: {password} \nIs it ok to save?")
            if is_good:
                # Encrypt that Data
                byte_info = info.encode('utf-8')
                encrypted_info = encrypt(byte_key, byte_info)
                encrypted_info_b64 = base64.b64encode(encrypted_info).decode('utf-8')

                with open('pass.txt', mode="a") as file:
                    print(encrypted_info_b64, file=file)

                # Clearing all the fields and settings sliders value to Zero
                website_entry.delete(0, END)
                pass_entry.delete(0, END)
                letters_slider.set(8)
                numbers_slider.set(2)
                symbols_slider.set(2)

    # Decrypting the data

    def decrypt_txt():
        total_p = ""
        path = "pass.txt"
        if os.path.exists(path) and os.path.getsize(path) > 0:
            with open("pass.txt", mode="r") as data_file:
                for line in data_file:
                    byte_type_content = base64.b64decode(line)
                    decrypted_data = decrypt(byte_key, byte_type_content)
                    total_p += f"{decrypted_data}\n"

            # Creating a new window to Display all the Data after it has been Decrypted.
            root = Tk()
            root.title("Password Viewer")

            text_widget = scrolledtext.ScrolledText(root, wrap=WORD, height=20, width=85)
            text_widget.pack(padx=10, pady=10)

            text_widget.insert(END, total_p)

            root.mainloop()
        else:
            messagebox.showerror(title="Value Error", message="There are currently no Saved Passwords, Generate and "
                                                              "Save Password to see them here")


    # ---------------------------- UI SETUP ------------------------------- #

    window = Tk()
    window.title("Password Manager")
    window.config(padx=50, pady=50, bg=DARK_GREY)

    canvas = Canvas(height=200, width=200, bg=DARK_GREY, highlightthickness=0)
    image = PhotoImage(file="logo.png")
    canvas.create_image(115, 100, image=image)
    canvas.grid(row=0, column=1, sticky="WN")

    # Labels
    website_label = Label(text="Website:  ", bg=DARK_GREY, fg=WHITE)
    website_label.grid(row=1, column=0, sticky="E")
    e_u_label = Label(text="Email/Username:  ", bg=DARK_GREY, fg=WHITE)
    e_u_label.grid(row=2, column=0, sticky="E")
    pass_label = Label(text="Password:  ", bg=DARK_GREY, fg=WHITE)
    pass_label.grid(row=3, column=0, sticky="E")
    para_label = Label(text="Parameters: ", pady=10, font=("Arial", 12, "bold"), bg=DARK_GREY, fg=WHITE)
    para_label.grid(row=5, column=1, sticky="W")
    letters_label = Label(text="No. of Letters --> ", bg=DARK_GREY, fg=WHITE)
    letters_label.grid(row=6, column=0, sticky="ES")
    numbers_label = Label(text="No. of Numbers --> ", bg=DARK_GREY, fg=WHITE )
    numbers_label.grid(row=7, column=0, sticky="ES")
    symbols_label = Label(text="No. of Symbols --> ", bg=DARK_GREY, fg=WHITE )
    symbols_label.grid(row=8, column=0, sticky="ES")

    # Entries

    website_entry = Entry()
    website_entry.grid(row=1, column=1, sticky="EW")
    website_entry.focus()
    e_u_entry = Entry()
    e_u_entry.grid(row=2, column=1, sticky="EW")
    e_u_entry.insert(0, "your-email@gmail.com")
    # You can insert your Email here so that you don't have to type it out everytime. If you use multiple Emails. Then
    # You can simply remove this line of code
    pass_entry = Entry(width=40)
    pass_entry.grid(row=3, column=1, sticky="W")

    # Buttons

    gen_pass_button = Button(text="Generate Password", command=gen_pass)
    gen_pass_button.grid(row=3, column=1, sticky="E")
    add_button = Button(text="Add", width=36, command=save_info)
    add_button.grid(row=4, column=1, sticky="EW")
    view_pass_button = Button(text="View Passwords", command=decrypt_txt)
    view_pass_button.grid(row=5, column=1, sticky="EN")

    # Sliders

    letters_slider = Scale(from_=0, to=20, orient="horizontal", length=300, sliderlength=16, showvalue=True, bg=DARK_GREY, fg=WHITE)
    letters_slider.set(8)
    letters_slider.grid(row=6, column=1)
    numbers_slider = Scale(from_=0, to=10, orient="horizontal", length=175, sliderlength=16, showvalue=True, bg=DARK_GREY, fg=WHITE)
    numbers_slider.set(2)
    numbers_slider.grid(row=7, column=1, sticky="W")
    symbols_slider = Scale(from_=0, to=10, orient="horizontal", length=175, sliderlength=16, showvalue=True, bg=DARK_GREY, fg=WHITE)
    symbols_slider.set(2)
    symbols_slider.grid(row=8, column=1, sticky="W")

    window.mainloop()
