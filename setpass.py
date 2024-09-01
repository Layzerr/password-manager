from tkinter import *
from tkinter import messagebox
from nacl import secret
import base64

key_path = "key.txt"
image = "logo.png"
DARK_GREY = "#3C3D37"
WHITE = "#ffffff"

# Checks if the Key.txt is empty, if it isn't The Program will run to Let the User set up Their Encryption Key.


class SetPass:
    def __init__(self):
        self.window = Tk()
        self.window.title("Encryption Key Setup")
        self.window.config(padx=50, pady=50, bg=DARK_GREY)
        self.window.minsize(height=150, width=200)

        self.canvas = Canvas(height=200, width=200, bg=DARK_GREY, highlightthickness=0)
        self.image = PhotoImage(file=image)
        self.canvas.create_image(110, 100, image=self.image)
        self.canvas.grid(row=0, column=0)

        self.byte_key = ""
        self.first_pass()
        self.second_pass()
        self.check_button()
        self.window.mainloop()

    def first_pass(self):
        self.fp_label = Label(text="Enter your encryption Key")
        self.fp_label.config(font=("Arial", 11, "bold"), bg=DARK_GREY, fg=WHITE)
        self.fp_label.grid(row=1, column=0)
        self.fp = Entry(width=45)
        self.fp.grid(row=3, column=0)
        self.instuction = Label(text="It must be 32 Bytes long\ni.e It should "
                                     "contain 32 Letters, \nNumbers and Symbols in Total\nValid Characters are:\n"
                                     "A-Z, a-z, 0-9, Space and Symbols ")
        self.instuction.config(pady=10, bg=DARK_GREY, fg=WHITE)
        self.instuction.grid(row=2, column=0)


    def second_pass(self):
        self.sp_label = Label(text="Confirm your Encryption Key")
        self.sp_label.config(pady=10, font=("Arial", 11, "bold"), bg=DARK_GREY, fg=WHITE)
        self.sp_label.grid(row=4, column=0)
        self.sp = Entry(width=45)
        self.sp.grid(row=5, column=0)

    def check_details(self):
        if len(self.fp.get()) == 32 and len(self.sp.get()) == 32:
            if self.fp.get() == self.sp.get():
                messagebox.showinfo(title="Setup Successful", message="Encryption Key has been Set-Up")
                key = self.sp.get()
                self.byte_key = key.encode('utf-8')
                encrypted_key = self.save_en_key()
                # Converting to base 64 to save to a .txt file
                encrypted_key_base64 = base64.b64encode(encrypted_key).decode('utf-8')
                with open(key_path, mode="w") as file:
                    file.write(encrypted_key_base64)
                self.window.destroy()
            else:
                messagebox.showerror(title="Setup Failed", message="The two Encryption keys don't Match")
        elif len(self.fp.get()) == 0 and len(self.sp.get()) == 0:
            messagebox.showinfo(title="Setup Error", message="Please Enter a Valid Encryption Key")
        else:
            messagebox.showerror(title="Setup Failed", message="The Encryption Key MUST be\nEXACTLY 32 Characters Long")


    def check_button(self):
        self.button = Button(text="Confirm Key", command=self.check_details)
        self.button.grid(row=7, column=0, sticky="S")

    def encrypt(self, key, text):
        box = secret.SecretBox(key)
        encrypted = box.encrypt(text)
        return encrypted

    def decrypt(self, key, encrypted):
        box = secret.SecretBox(key)
        decrypted = box.decrypt(encrypted)
        data = decrypted.decode('utf-8')
        return decrypted

    def save_en_key(self):
        encrypted_key = self.encrypt(self.byte_key, self.byte_key)
        return encrypted_key

