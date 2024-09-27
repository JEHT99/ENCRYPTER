import tkinter as tk
import customtkinter
from dataBase import DataBase
from crypto import generate_key, read_key
#////////////////////////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////////////////////////
myDB = DataBase()
messages = {
    "success": ["Notify", "Operation have been"],
    "fail" : ["Error", "Failed operation, try it again"],
    "badKey" : ["Error", "Wrong key"]
}
#////////////////////////////////////////////////////////////////////////////////////////////////////
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
)
root.bind_all("<Control-n>")
root.bind_all("<Control-N>")

mainMenu.add_command(
    label = "Edit record",
    accelerator = "CTRL+E",
)
root.bind_all("<Control-e>")
root.bind_all("<Control-E>")

mainMenu.add_command(
    label = "Delete record",
    accelerator = "CTRL+D",
)
root.bind_all("<Control-d>")
root.bind_all("<Control-D>")

mainMenu.add_separator()
mainMenu.add_command(label="Quit", command=root.destroy)

#RSA options
opMenu = tk.Menu(menuBar, tearoff=False)
opMenu.add_command(
    label = "Generate key",
)
opMenu.add_command(
    label = "Load key",
)

menuBar.add_cascade(menu=mainMenu, label="File")
menuBar.add_cascade(menu=opMenu, label="Options")
root.config(menu=menuBar)

root.mainloop()