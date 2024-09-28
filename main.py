import tkinter as tk
import customtkinter
from dataBase import DataBase
from crypto import generate_key, read_key
import re
#////////////////////////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////////////////////////
myDB = DataBase()
keyPath = ""
#////////////////////////////////////////////////////////////////////////////////////////////////////
def showMessage(option: int):
    if option == 0:
        tk.messagebox.showinfo(title="Success",
                               message="Operation have been completed")
        return

    if option == 1:
        tk.messagebox.showerror(title="Error",
                                message="Operation failed, try it again")
        return
    
    if option == 2:
        tk.messagebox.showerror(title="Error",
                                message="Wrong key")
        return
    
    return
#////////////////////////////////////////////////////////////////////////////////////////////////////
def createView(event=None):
    print("Create")
#////////////////////////////////////////////////////////////////////////////////////////////////////
def editView(event=None):
    print("Edit")
#////////////////////////////////////////////////////////////////////////////////////////////////////
def deleteView(event=None):
    dialog = customtkinter.CTkInputDialog(text="Type an Account ID to delete it:", title="Delete account")
    accountId = dialog.get_input()  # waits for input

    if re.search("^\d+$", accountId) != None and myDB.deleteRecord(accountId):
        showMessage(0)
    else:
        showMessage(1)
#////////////////////////////////////////////////////////////////////////////////////////////////////
def createKey(event=None):
    if generate_key() == True:
        showMessage(0)
    else:
        showMessage(1)
#////////////////////////////////////////////////////////////////////////////////////////////////////
#Form set up
customtkinter.set_appearance_mode("dark")
root = customtkinter.CTk()
root.resizable(0,0)
root.title("Passwords Encrypter")
root.geometry('600x500')

#Menu set up
menuBar = tk.Menu()
#Create, Edit & Delete options
mainMenu = tk.Menu(menuBar, tearoff=False)
mainMenu.add_command(
    label = "Create new record",
    accelerator = "CTRL+N",
    command = createView
)
root.bind_all("<Control-n>",createView)
root.bind_all("<Control-N>",createView)

mainMenu.add_command(
    label = "Edit record",
    accelerator = "CTRL+E",
    command = editView
)
root.bind_all("<Control-e>",editView)
root.bind_all("<Control-E>",editView)

mainMenu.add_command(
    label = "Delete record",
    accelerator = "CTRL+D",
    command = deleteView
)
root.bind_all("<Control-d>",deleteView)
root.bind_all("<Control-D>",deleteView)

mainMenu.add_separator()
mainMenu.add_command(label="Quit", command=root.destroy)

#RSA options
opMenu = tk.Menu(menuBar, tearoff=False)
opMenu.add_command(
    label = "Generate key",
    command = createKey
)
opMenu.add_command(
    label = "Load key",
)

menuBar.add_cascade(menu=mainMenu, label="File")
menuBar.add_cascade(menu=opMenu, label="Options")
root.config(menu=menuBar)

root.mainloop()