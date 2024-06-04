from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
    global file
    root.title("Notepad")
    file = None
    text.delete(1.0, END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])

    if file == "":
        file = None

    else:
        root.title(os.path.basename(file)+" - Notepad")
        text.delete(1.0, END)
        f  = open(file, "r")
        text.insert(1.0, f.read())
        f.close()

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Documents", "*.txt")])

        if file == "":
            file = None
        
        else:
            f = open(file, "w")
            f.write(text.get(1.0, END))
            f.close()

            root.title(os.path.basename(file)+" - Notepad")
            print("File Saved")

    else:
        f = open(file, "w")
        f.write(text.get(1.0, END))
        f.close()

def quitApp():
    root.destroy()

def cut():
    text.event_generate(("<<Cut>>"))

def copy():
    text.event_generate(("<<Copy>>"))

def paste():
    text.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad", "Notepad by Vineet")

if __name__ == '__main__':
    root = Tk()
    root.title("Notepad")
    root.geometry("900x500")

    text = Text(root, font=("", 16))
    file = None
    text.pack(expand=True, fill=BOTH)

    MenuBar = Menu(root)

    FileMenu = Menu(MenuBar, tearoff=0)
    FileMenu.add_command(label="New", command=newFile)
    FileMenu.add_command(label="Open", command=openFile)
    FileMenu.add_command(label="Save", command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=quitApp)
    MenuBar.add_cascade(label="File", menu=FileMenu)

    EditMenu = Menu(MenuBar, tearoff=0)
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)
    MenuBar.add_cascade(label="Edit", menu=EditMenu)

    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label="About Notepad", command=about)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)

    root.config(menu=MenuBar)

    Scroll=Scrollbar(text)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=text.yview)
    text.config(yscrollcommand=Scroll.set)

    root.mainloop()

# In the above code, we have created a simple Notepad application using the Tkinter library.