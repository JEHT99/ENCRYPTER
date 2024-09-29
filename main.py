import tkinter as tk
from tkinter import ttk
import customtkinter
from functools import partial
from Modules.dataBase import DataBase
from Modules.forms import ParentForm, ChildForm
from Modules.crypto import generate_key, read_key, decrypt_text
import re
#////////////////////////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////////////////////////
# Global
myDB = DataBase()
shortcut = "disabled"
def showMessage(option: int):
    messages=[
        ["Success","Operation has been completed"],
        ["Error", "Operation failed, try it again"],
        ["Error", "Wrong key"],
        ["Error", "Bad parameters"]
    ]

    if option in range(len(messages)):
        if option == 0:
            tk.messagebox.showinfo(title=messages[option][0],
                               message=messages[option][1])
        else:
            tk.messagebox.showerror(title=messages[option][0],
                               message=messages[option][1])
#////////////////////////////////////////////////////////////////////////////////////////////////////
def activateShortCuts(form:object):
    form.bind_all("<Control-n>",partial(createView,flag=True))
    form.bind_all("<Control-N>",partial(createView,flag=True))
    form.bind_all("<Control-e>",editView)
    form.bind_all("<Control-E>",editView)
    form.bind_all("<Control-d>",deleteView)
    form.bind_all("<Control-D>",deleteView)
#////////////////////////////////////////////////////////////////////////////////////////////////////
def createView(event=None, flag:bool=True, target=None):
    def submit():
        key = read_key(keyPath.get())
        if key == None:
            showMessage(1)
            return
        
        if flag == False:
            status = myDB.updateRecord(target, website.get(),
                        email.get(),password.get(), key)
        else:
            status = myDB.addRecord(website.get(), email.get(),
                        password.get(),key)
        
        if status == 2:
            showMessage(3)
            return
        
        if status == 1 or status==3:
            showMessage(1)
            return

        showMessage(0)
        current.destroy()
    #////////////////////////////////////////////////////////////////////////////////////////////////
    toplevel = ChildForm("Record Creator", 300, 200)
    current = toplevel.getFormType()

    record = myDB.getRecord(target)

    if flag == True:
        websiteU.set("Example.com")
        emailU.set("Example@email.com")
    elif len(record) == 0:
        showMessage(1)
        current.destroy()
        return
    else:
        websiteU.set(record[0][1])
        emailU.set(record[0][2])

    label1 = customtkinter.CTkLabel(current,
                text="Website", fg_color="transparent")
    label1.place(x=10, y=20)

    website = customtkinter.CTkEntry(current, width=200, textvariable=websiteU)
    website.place(x=80, y=20)


    label2 = customtkinter.CTkLabel(current,
                text="Email", fg_color="transparent")
    label2.place(x=10, y=60)

    email = customtkinter.CTkEntry(current, width=200, textvariable=emailU)
    email.place(x=80, y=60)


    label3 = customtkinter.CTkLabel(current,
                text="Password", fg_color="transparent")
    label3.place(x=10, y=100)

    password = customtkinter.CTkEntry(current, width=200)
    password.place(x=80, y=100)

    button = customtkinter.CTkButton(current, text="Accept",
                width=100, command=submit)
    button.place(x=180, y=150)
#////////////////////////////////////////////////////////////////////////////////////////////////////
def editView(event=None):
    dialog = customtkinter.CTkInputDialog(text="Type an Account ID to edit it:",
                                          title="Edit Account")
    accountId = dialog.get_input()

    if accountId == None:
        return

    if re.search("^\d+$", accountId) != None:
        createView(flag=False,target=int(accountId))
    else:
        showMessage(1)
#////////////////////////////////////////////////////////////////////////////////////////////////////
def deleteView(event=None):
    dialog = customtkinter.CTkInputDialog(text="Type an Account ID to delete it:",
                                          title="Delete Account")
    accountId = dialog.get_input()

    if accountId == None:
        return

    if re.search("^\d+$", accountId) != None and myDB.deleteRecord(int(accountId)) == 0:
        showMessage(0)
        tree.delete(int(accountId))
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
    def loadKey():
        tempPath = ""
        file = tk.filedialog.askopenfilename(title="Select",initialdir="C://",
                filetypes=(("Token","*.key"),))
        
        tempPath = file
        
        if tempPath != "":
            keyPath.set(file)
            activateShortCuts(root.getFormType())
            mainMenu.entryconfig("Create new record", state="normal")
            mainMenu.entryconfig("Edit record", state="normal")
            mainMenu.entryconfig("Delete record", state="normal")

            showMessage(0)
    #////////////////////////////////////////////////////////////////////////////////////////////////
    toplevel = ChildForm("RSA Key Loader", 400, 100)

    currentFile = customtkinter.CTkEntry(toplevel.getFormType(), width=300, state="readonly",
                    textvariable=keyPath)
    currentFile.place(x=10, y=30)

    upload = customtkinter.CTkButton(toplevel.getFormType(), text="Brwose", command=loadKey,
                width=50, height=30, corner_radius=100)
    upload.place(x=320, y=30)
#////////////////////////////////////////////////////////////////////////////////////////////////////
def showPassword(event=None):
    selectedItem = tree.focus()
    record = myDB.getRecord(int(selectedItem))

    if len(record) == 0 or keyPath.get() == "":
        return
    
    try:
        currentPassword = read_key(keyPath.get())
        if currentPassword != None:
            tk.messagebox.showinfo(title="Current Password",
                message=decrypt_text(currentPassword, record[0][3]))
    except:
        showMessage(2)
#////////////////////////////////////////////////////////////////////////////////////////////////////
#Form set up
customtkinter.set_appearance_mode("dark")
root = ParentForm("Passwords Encrypter", 600, 400)
keyPath = tk.StringVar()
websiteU = tk.StringVar()
emailU = tk.StringVar()

#Menu set up
menuBar = tk.Menu()
#Create, Edit & Delete options
mainMenu = tk.Menu(menuBar, tearoff=False)
mainMenu.add_command(label = "Create new record", accelerator = "CTRL+N",
    command = partial(createView, flag=True), state="disabled")

mainMenu.add_command(label = "Edit record", accelerator = "CTRL+E",
    command = editView, state="disabled")

mainMenu.add_command(label = "Delete record", accelerator = "CTRL+D",
    command = deleteView, state="disabled")

mainMenu.add_separator()
mainMenu.add_command(label="Quit", command=root.getFormType().destroy)

#RSA options
opMenu = tk.Menu(menuBar, tearoff=False)
opMenu.add_command(label = "Generate key", command = createKey)
opMenu.add_command(label = "Load key", command = loadKeyView)

menuBar.add_cascade(menu=mainMenu, label="File")
menuBar.add_cascade(menu=opMenu, label="Options")
root.getFormType().config(menu=menuBar)

#Tree view
records = myDB.getRecords()
tree = ttk.Treeview(root.getFormType())

# Define columns
tree['columns'] = ("Website", "Email")

# Format the columns
tree.column("#0", width=50, minwidth=25)
tree.column("Website", anchor=tk.CENTER, width=150)
tree.column("Email", anchor=tk.CENTER, width=150)

# Create column headers
tree.heading("#0", text="ID", anchor=tk.CENTER)
tree.heading("Website", text="Website", anchor=tk.CENTER)
tree.heading("Email", text="Email", anchor=tk.CENTER)

# Add data to the Treeview
for item in records:
    tree.insert(parent='', index='end', iid=item[0], text=item[0], values=(item[1],item[2]))

tree.bind("<Double-1>", showPassword)

# Pack the Treeview widget
tree.pack(pady=20)

root.run()
#////////////////////////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////////////////////////