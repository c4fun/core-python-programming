__author__ = 'Richard'

import os
from time import sleep
from tkinter import Tk, Scale, Button, Label, StringVar, Frame, \
    Scrollbar, Listbox, Entry, mainloop
from tkinter import X, Y, RIGHT, LEFT, BOTH, END


class DirList(object):
    # This class will display the directory list? Will it?
    def __init__(self, initdir = None):
        self.root = Tk()
        self.label = Label(self.root, text='Directory Lister v1.1')
        self.label.pack()

        # The current working directory as a StringVar shown in root
        self.cwd = StringVar(self.root)

        self.dir1 = Label(self.root, fg='blue', font=('Helvetica', 12, 'bold'))
        self.dir1.pack()

        # set the frame that contains the dir list(scrollbar, listbox)
        self.dir_frame = Frame(self.root)
        self.dir_scrollbar = Scrollbar(self.dir_frame)
        self.dir_scrollbar.pack(side=RIGHT, fill = Y)
        # yscrollcommand means the command on the y scroll
        self.dirs = Listbox(self.dir_frame, height=15, width=50,
                            yscrollcommand=self.dir_scrollbar.set)
        self.dirs.bind('<Double-1>', self.setDirAndGo)
        self.dir_scrollbar.config(command=self.dirs.yview)
        self.dirs.pack(side=LEFT, fill=BOTH)
        self.dir_frame.pack()

        # Entry can be affected by the cwd
        self.dir_entry = Entry(self.root, width=50,textvariable=self.cwd)
        self.dir_entry.bind('<Return>', self.doLS)
        self.dir_entry.pack()

        self.button_frame = Frame(self.root)
        self.clear = Button(self.button_frame, text='Clear',command=self.clrDir,
                            activeforeground='white', activebackground='blue')
        self.ls = Button(self.button_frame, text='List Directory',
                         command=self.doLS, activeforeground='white',
                         activebackground='green')
        self.quit = Button(self.button_frame, text='QUIT',
                           command=self.root.quit, activeforeground='white',
                           activebackground='red')
        self.clear.pack(side=LEFT)
        self.ls.pack(side=LEFT)
        self.quit.pack(side=LEFT)
        self.button_frame.pack()

        if initdir:
            self.cwd.set(os.curdir)
            self.doLS()

    def clrDir(self, ev=None):
        # set the current directory to the root
        self.cwd.set('')

    def setDirAndGo(self, ev=None):
        # set the current working dir to ?
        self.last = self.cwd.get()
        self.dirs.config(selectbackground='red')
        check = self.dirs.get(self.dirs.curselection())
        if not check:
            check = os.curdir
        self.cwd.set(check)
        self.doLS()

    def doLS(self, ev=None):
        # list the directory of the entry directory
        error = ''
        tdir = self.cwd.get()
        if not tdir:
            tdir = os.curdir

        if not os.path.exists(tdir):
            error = tdir + ': no such file'
        elif not os.path.isdir(tdir):
            error = tdir + ': not a directory'

        if error:
            self.cwd.set(error)
            self.root.update()
            sleep(2)
            if not (hasattr(self, 'last') and self.last):
                self.last = os.curdir
            self.cwd.set(self.last)
            self.dirs.config(
                selectbackground='LightSkyBlue'
            )
            self.root.update()
            return

        self.cwd.set('FETCHING DIRECTORY CONTENTS...')
        self.root.update()
        dirlist = os.listdir(tdir)
        dirlist.sort()
        os.chdir(tdir)
        self.dir1.config(text=os.getcwd())
        self.dirs.delete(0, END)
        self.dirs.insert(END, os.curdir)
        self.dirs.insert(END, os.pardir)
        for eachFile in dirlist:
            self.dirs.insert(END, eachFile)
        self.cwd.set(os.curdir)
        self.dirs.config(selectbackground='LightSkyBlue')

def main():
    d = DirList(os.curdir)
    mainloop()

if __name__ == '__main__':
    main()