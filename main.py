import tkinter as tk
import customtkinter
from dataBase import DataBase
from forms import ParentForm, ChildForm
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
    toplevel = ChildForm("Record creator", 300, 200)
#////////////////////////////////////////////////////////////////////////////////////////////////////
def editView(event=None):
    print("Edit")
#////////////////////////////////////////////////////////////////////////////////////////////////////
def deleteView(event=None):
    dialog = customtkinter.CTkInputDialog(text="Type an Account ID to delete it:",
                                          title="Delete account")
    accountId = dialog.get_input()

    if accountId == None:
        return

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
def loadKeyView(event=None):
    toplevel = ChildForm("RSA Key Loader", 470, 100)

    fileContent = tk.StringVar()
    currentFile = customtkinter.CTkEntry(toplevel.getFormType(), width=300, state="readonly",
                                         textvariable=fileContent)
    currentFile.place(x=10, y=30)

    upload = customtkinter.CTkButton(toplevel.getFormType(), text="Brwose", command=None,
                    width=50, height=30, corner_radius=100)
    upload.place(x=320, y=30)

    submit = customtkinter.CTkButton(toplevel.getFormType(), text="Load", state="disabled",
                    command=None, width=50, height=30, corner_radius=100)
    submit.place(x=400, y=30)
#////////////////////////////////////////////////////////////////////////////////////////////////////
#Form set up
customtkinter.set_appearance_mode("dark")
root = ParentForm("Passwords Encrypter", 600, 500)

#Menu set up
menuBar = tk.Menu()
#Create, Edit & Delete options
mainMenu = tk.Menu(menuBar, tearoff=False)
mainMenu.add_command(
    label = "Create new record",
    accelerator = "CTRL+N",
    command = createView
)
root.getFormType().bind_all("<Control-n>",createView)
root.getFormType().bind_all("<Control-N>",createView)

mainMenu.add_command(
    label = "Edit record",
    accelerator = "CTRL+E",
    command = editView
)
root.getFormType().bind_all("<Control-e>",editView)
root.getFormType().bind_all("<Control-E>",editView)

mainMenu.add_command(
    label = "Delete record",
    accelerator = "CTRL+D",
    command = deleteView
)
root.getFormType().bind_all("<Control-d>",deleteView)
root.getFormType().bind_all("<Control-D>",deleteView)

mainMenu.add_separator()
mainMenu.add_command(label="Quit", command=root.getFormType().destroy)

#RSA options
opMenu = tk.Menu(menuBar, tearoff=False)
opMenu.add_command(
    label = "Generate key",
    command = createKey
)
opMenu.add_command(
    label = "Load key",
    command = loadKeyView
)

menuBar.add_cascade(menu=mainMenu, label="File")
menuBar.add_cascade(menu=opMenu, label="Options")
root.getFormType().config(menu=menuBar)

root.run()