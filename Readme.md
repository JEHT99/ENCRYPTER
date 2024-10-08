# What it is
This applicattion is a local password manager focused on crypt and decrypt your passwords from different websites trought a ***token***.

# How to use it
1. If is your first time using the app, you have to generate your ***AES key*** clicking their option by following next steps: ***Options>Generate Key***.
    * By default, the key is generated in your current path.
    * Ensure to saved it in a safe place & don't lose it.
1. When you start the app, it shows all your saved data.
    * If you double click any record, it must be showed your password, as long as a valid ***AES key*** has been uploaded.
1. To enable ***Create new record***, ***Edit record***, ***Delete record*** & ***Decrypt Password*** options, upload your key (***Options>Load Key***).
1. Finally, complete each form to apply any changes.

# System requirements
This application has been tested on:
1. Python 3.11.2.
1. Microsoft Windows 11.

### Dependencies
```
 > pip install tk
 > pip install customtkinter
 > pip install cryptography
```

# How to run the application
Just execute ***main.py*** or run it from the current folder from the command line.
```
ENCRYPTER> python main.py
```
