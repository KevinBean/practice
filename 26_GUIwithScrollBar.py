# Python 2.7
import Tkinter as tki
from ScrolledText import ScrolledText

class App(object):

    def __init__(self):
        self.root = tki.Tk()

    # create a Text widget with a Scrollbar attached
        self.txt = ScrolledText(self.root, undo=True)
        self.txt['font'] = ('consolas', '12')
        self.txt.pack(expand=True, fill='both')

app = App()
app.root.mainloop()