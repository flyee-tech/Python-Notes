##################################################
# ----------- Python的GUI --------------- #
##################################################

# Python支持多种图形界面的第三方库，包括：Tk wxWidgets Qt GTK
# Python自带的库是支持Tk的Tkinter，使用Tkinter，无需安装任何包，就可以直接使用。

from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.quitButton = Button(self, text="Quit", command=self.quit())
        self.helloLabel = Label(self, text="hello label")
        self.pack()
        self.helloLabel.pack()
        self.quitButton.pack()


app = Application()
app.master.title('hello world')
app.mainloop()
