from tkinter import *


class Application(Frame):
     def __init__(self,master=None, *args, **kwargs):
         Frame.__init__(self,master, *args, **kwargs)
         self.grid()
         self.createWidgets()
         self.flag=True
         self.transparent=False
         self.top = self.winfo_toplevel()

     def overturn(self):
         self.top.update_idletasks()
         self.top.overrideredirect(self.flag)
         self.flag=not self.flag

     def createWidgets(self):
         self.canvas = Canvas(self, bg='green')
         self.canvas.pack()
         self.flagButton = Button(self, text='try this', bg='green', command=self.overturn)
         self.flagButton.pack()
app = Application()
app.master.title("sample application")
app.mainloop()