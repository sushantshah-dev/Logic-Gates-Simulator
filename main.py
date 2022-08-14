import sys, pickle, tkinter, tkinter.ttk

class App(tkinter.Tk):
    def __init__(self, baseObject=None):
        super().__init__()

        self.baseObject = baseObject
        self.title('Logic Gate Simulator')
        self.geometry('800x600')
        self.resizable(True, True)
        
        self.menubar = tkinter.Menu(self)
        self.filemenu = tkinter.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label='Save', command=self._save)
        self.filemenu.add_command(label='Load', command=self._load)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Exit', command=self.quit)
        self.menubar.add_cascade(label='File', menu=self.filemenu)
        self.config(menu=self.menubar)

    def _save(self):
        save()

    def _load(self):
        pass

    def quit(self) -> None:
        return super().quit()

def main(baseObject=None):
    pass

def save(baseObject, filename):
    pickle.dump(baseObject, open(filename, 'wb'))

if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(pickle.load(open(sys.argv[1], 'rb')))
    elif len(sys.argv) == 1:
        main()