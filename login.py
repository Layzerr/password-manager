import base64
from tkinter import *
from tkinter import messagebox
from nacl import secret, exceptions
from save_pass import password_saver

image = "logo.png"
DARK_GREY = "#3C3D37"
WHITE = "#ffffff"


def login_validation():

    def decrypt(key, encrypted):
        # If Both the Keys are same, The decryption Process will complete and Open the Password Entry and Saving
        # Mechanism, otherwise it will show an Error using the MessageBox
        try:
            box = secret.SecretBox(key)
            decrypted = box.decrypt(encrypted)
            messagebox.showinfo(title="Identification Successful", message="Your Encryption Key is correct and your "
                                                                           "Identification has been Completed")

            window.destroy()
            password_saver(given_key=decrypted)

        except exceptions.CryptoError:
            retry = messagebox.askretrycancel(title="Verification Failed", message="Your Identify could not be Verified. "
                                                                           "Please Ensure that the Encryption Key "
                                                                           "Entered is the one used during Setup")
            if retry:
                pass
            else:
                window.destroy()




    def return_entry():
        user_given_key = en_entry.get()
        if len(user_given_key) == 0:
            messagebox.showerror(title="Invalid Entry", message="Please Enter a Valid Encryption Key! ")
        elif len(user_given_key) < 32 or len(user_given_key) > 32:
            messagebox.showerror(title="Invalid Entry", message="Please ensure that The Encryption Key "
                                                                "is EXACTLY 32 Characters Long")
        else:
            confirmation = messagebox.askokcancel(title="Confirmation", message=f"Do You Confirm that: "
                                                                                f"\n{user_given_key}\n"
                                                                                f"Is Your Encryption Key?")
            if confirmation:

                # Check if the Key matches

                with open("key.txt", mode="r") as file:
                    # Decrypt the Stored Key to Bytes using the User Provided Key in Bytes, Then pass the Both the Keys
                    # To the Decrypt Function

                    stored_key = file.read()
                    store_en_key = base64.b64decode(stored_key)
                user_given_byte_key = user_given_key.encode('utf-8')
                decrypt(user_given_byte_key, store_en_key)
            else:
                pass


    black = "#000000"
    off_white = "#FEFAE0"

    window = Tk()
    window.title("Login Window")
    window.minsize(height=150, width=350)
    window.config(padx=50, pady=50, bg=DARK_GREY)

    canvas = Canvas(height=200, width=200, bg=DARK_GREY, highlightthickness=0)
    image = PhotoImage(file="logo.png")
    canvas.create_image(135, 100, image=image)
    canvas.grid(row=0, column=1, sticky="WN")

    # Label
    g_label = Label(text="Please Enter Your Encryption Key")
    g_label.config(pady=10, font=("Arial", 9, "bold"), bg=DARK_GREY, fg=WHITE)
    g_label.grid(row=1, column=1)
    n_label = Label(text="NOTE: ", bg=DARK_GREY, fg=WHITE)
    n_label.config(pady=5, font=("Arial", 8, 'bold'))
    n_label.grid(row=4, column=1)
    info_label = Label(text="It is 32 Bytes long\ni.e It "
                            "contains 32 Letters, \nNumbers and Symbols in Total\nValid Characters are:\n"
                            "A-Z, a-z, 0-9, Space and Symbols ")
    info_label.config(bg=DARK_GREY, fg=WHITE)
    info_label.grid(row=5, column=1)

    # Entry
    en_entry = Entry(width=45)
    en_entry.grid(row=2, column=1)

    # Button to confirm
    button = Button(text="Confirm", command=return_entry)
    button.grid(row=3, column=1)

    window.mainloop()


