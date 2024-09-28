import tkinter as tk
import customtkinter
from dataBase import DataBase
from crypto import generate_key, read_key
import re
#////////////////////////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////////////////////////
myDB = DataBase()
#////////////////////////////////////////////////////////////////////////////////////////////////////
def showMessage(option: int):
    messages=[
        ["Success","Operation has been completed"],
        ["Error", "Operation failed, try it again"],
        ["Error", "Wrong key"]
    ]

    if option in range(len(messages)):
        if option == 0:
            tk.messagebox.showinfo(title=messages[option][0],
                               message=messages[option][1])
        else:
            tk.messagebox.showerror(title=messages[option][0],
                               message=messages[option][1])
#////////////////////////////////////////////////////////////////////////////////////////////////////
def createView(event=None):
    print("Create")
#////////////////////////////////////////////////////////////////////////////////////////////////////
def editView(event=None):
    print("Edit")
#////////////////////////////////////////////////////////////////////////////////////////////////////
def deleteView(event=None):
    dialog = customtkinter.CTkInputDialog(text="Type an Account ID to delete it:",
                                          title="Delete account")
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
def loadKey(event=None):
    toplevel = customtkinter.CTkToplevel(root)
    toplevel.resizable(0,0)
    toplevel.title("RSA Key Loader")
    toplevel.geometry('500x100')

    fileContent = tk.StringVar()
    currentFile = customtkinter.CTkEntry(toplevel, width=300, state="readonly",
                                         textvariable=fileContent)
    currentFile.place(x=10, y=30)

    upload = customtkinter.CTkButton(toplevel, text="Brwose", command=None,
                    width=20, height=2)
    upload.place(x=260, y=30)

    submit = customtkinter.CTkButton(toplevel, text="Load", state="disabled",
                    command=None, width=20, height=2)
    submit.place(x=420, y=30)
#////////////////////////////////////////////////////////////////////////////////////////////////////
#Form set up
customtkinter.set_appearance_mode("dark")
root = customtkinter.CTk()
root.resizable(0,0)
root.title("Passwords Encrypter")
root.geometry('600x500')
#keyPath = tk.StringVar()

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
    command = loadKey
)

menuBar.add_cascade(menu=mainMenu, label="File")
menuBar.add_cascade(menu=opMenu, label="Options")
root.config(menu=menuBar)

root.mainloop()