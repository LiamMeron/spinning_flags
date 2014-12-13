from Tkinter import *
import Tkinter.ScrolledText as tksc

class Root(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):#Setup the window with it's buttons and menus
        self.grid()

        self.MessageBox = Text(self, height=5, width = 10)
        self.MessageBox.grid(column=0,row=1,sticky='EW')

        
        self.TextEntryBox = Entry(self)
        self.TextEntryBox.grid(column=0,row=0,sticky='EW')
        self.TextEntryBox.bind("<Return>", self.onPressEnter)
        self.TextEntryBox.focus_set()

        
    def onPressEnter(self,event):

        self.MessageBox.configure(state='normal')
        self.MessageBox.insert(INSERT,self.TextEntryBox.get())
        self.MessageBox.configure(state='disabled')

        self.TextEntryBox.focus_set()
        self.TextEntryBox.delete(0, END)
        


if __name__ == "__main__":
    app = Root(None)
    app.title = "BasicGui 0.1"
    app.mainloop()
