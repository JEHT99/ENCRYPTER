import customtkinter
#////////////////////////////////////////////////////////////////////////////////////////////////////
class Form():
    def __init__(self, formTitle:str=None, windowWidth:int=None,
                 windowHeight:int=None)-> None:
        self.formTitle = formTitle
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.formType = None
    #////////////////////////////////////////////////////////////////////////////////////////////////
    def createForm(self):        
        (self.formType).title(self.formTitle)
        (self.formType).resizable(0,0)
        screenWidth = (self.formType).winfo_screenwidth()
        screenHeight = (self.formType).winfo_screenheight()
        windowWidth = self.windowWidth
        windowHeight = self.windowHeight

        positionWidth = round(screenWidth*.10)
        positionHeight = round(screenHeight*.10)

        (self.formType).geometry(f"{windowWidth}x{windowHeight}+{positionWidth}+{positionHeight}")
    #////////////////////////////////////////////////////////////////////////////////////////////////
    def getFormType(self)->object:
        return self.formType
    #////////////////////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////////////////////////
class ParentForm(Form):
    def __init__(self, formTitle:str=None, windowWidth:int=None,
                 windowHeight:int=None):
        Form.__init__(self, formTitle, windowWidth, windowHeight)
        self.formType = customtkinter.CTk()
        self.createForm()
    #////////////////////////////////////////////////////////////////////////////////////////////////
    def run(self)->None:
        self.formType.mainloop()
#////////////////////////////////////////////////////////////////////////////////////////////////////
class ChildForm(Form):
    def __init__(self, formTitle:str=None, windowWidth:int=None,
                 windowHeight:int=None):
        Form.__init__(self, formTitle, windowWidth, windowHeight)
        self.formType = customtkinter.CTkToplevel()
        self.createForm()
        self.formType.focus_force()
        self.formType.grab_set()
#////////////////////////////////////////////////////////////////////////////////////////////////////