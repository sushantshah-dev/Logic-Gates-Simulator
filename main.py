import sys, pickle, tkinter, tkinter.ttk
from module import Module

class App(tkinter.Tk):
    def __init__(self, baseObject=None, file=None):
        super().__init__()

        self.baseObject = baseObject
        self.file = file

        self.title('Logic Gate Simulator - ' + self.file if self.file else 'Logic Gate Simulator')
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

        self.tab_layout = tkinter.ttk.Notebook(self)
        self.tab_layout.pack(side='bottom', fill='both', expand=True)
        
        self.tabs = []
        self.new_tab(self.baseObject)

    def new_tab(self, baseObject: Module) -> None:
        self.tabs.append((tkinter.Frame(self.tab_layout), baseObject))
        tkinter.Canvas(self.tabs[-1][0], bg="#202020").pack(fill='both', expand=True)
        self.tab_layout.add(self.tabs[-1][0], text=self.tabs[-1][1].name)

    def _save(self):
        save()

    def _load(self):
        pass

    def quit(self) -> None:
        return super().quit()

def main(baseObject=None):
    if baseObject is None:
        baseObject = Module()
    save(baseObject, 'temp_project.pickle')
    app = App(baseObject)
    app.mainloop()

def save(baseObject, filename):
    pickle.dump(baseObject, open(filename, 'wb'))

if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(pickle.load(open(sys.argv[1], 'rb')))
    elif len(sys.argv) == 1:
        main()