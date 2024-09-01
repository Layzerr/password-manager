# Password Manager
This is a secure and user-friendly Password Manager application built using Python. The project is designed to store and manage passwords locally, ensuring that your sensitive information is encrypted and easily accessible whenever you need it.

## Features
- Encryption: All passwords are encrypted using the Salsa20 encryption algorithm provided by the PyNaCl library, ensuring your data is secure.
- User Authentication: The app includes a login system to protect access to your password vault.
- Intuitive Interface: Simple and easy-to-use graphical interface built with Tkinter.
- Local Storage: Passwords are stored locally on your machine in an encrypted format.
- Cross-Platform: Works on Windows, macOS, and Linux.

## Demo

## Getting Started
### Prerequisites:
- Python 3.6+
- Required Python libraries: PyNaCl, Tkinter, Pandas

## Installtion
### Easy Way:
The most straightforward way is to install the program using the provided .exe file, which is installed just like a normal program without needing to touch the command prompt.

### Hard Way:
If you want Set-up the program for yourself you can use the following commands:
#### Steps:
1. Clone this repository:
```
git clone https://github.com/Layzerr/password-manager.git
cd password-manager
```
2. Install the Required Dependencies:
```
pip install -r requirements.txt
```
3. Run The Application
```
python main.py
```
#### Building the Executable:
To build the application into a standalone executable:

1. Ensure PyInstaller is installed:
```
pip install pyinstaller
```
2. Run the following command:
```
pyinstaller --onefile --windowed main.py
```
The executable will be created in the dist folder. Move to the Main Folder and you are Done.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For any inquiries or suggestions, feel free to contact me at aryanahmad.anabat@gmail.com



