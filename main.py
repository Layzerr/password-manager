from setpass import SetPass
from login import login_validation

# Importing Functionality

# ---------------------------- AUTHENTICATION MECHANISM ------------------------------- #


key_path = "key.txt"

with open(key_path, "r") as file:
    key = file.read().strip()
    if key:
        login_validation()
    else:
        sp = SetPass()

# Check if there is a Key already Present, if yes than it proceeds to the Login page, if not than you have to
# Set an encryption key



