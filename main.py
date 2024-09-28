import tkinter as tk
import customtkinter
from dataBase import DataBase
from crypto import generate_key, read_key
import re
#////////////////////////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////////////////////////
myDB = DataBase()
keyPath = ""
messages = {
    "success": ["Notify", "Operation have been completed"],
    "fail" : ["Error", "Operation failed, try it again"],
    "badKey" : ["Error", "Wrong key"]
}
#////////////////////////////////////////////////////////////////////////////////////////////////////
def createView(event=None):
    print("Create")
#////////////////////////////////////////////////////////////////////////////////////////////////////
def editView(event=None):
    print("Edit")
#////////////////////////////////////////////////////////////////////////////////////////////////////
def deleteView(event=None):
    dialog = customtkinter.CTkInputDialog(text="Type account id to delete it:", title="Delete account")
    accountId = dialog.get_input()  # waits for input

    if re.search("^\d+$", accountId) != None and myDB.deleteRecord(accountId):
        tk.messagebox.showinfo(message = messages["success"][1],
                            title = messages["success"][0])
    else:
        tk.messagebox.showerror(message = messages["fail"][1],
                            title = messages["fail"][0])
#////////////////////////////////////////////////////////////////////////////////////////////////////
def createKey(event=None):
    if generate_key() == True:
        tk.messagebox.showinfo(message = messages["success"][1],
                            title = messages["success"][0])
    else:
        tk.messagebox.showerror(message = messages["fail"][1],
                            title = messages["fail"][0])
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