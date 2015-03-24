__author__ = 'Richard'

import tkinter


def resize(ev=None):
    label.config(font='Consolas -%d bold'% scale.get())


root = tkinter.Tk()
root.geometry('250x150')

label = tkinter.Label(root, text='Hello World!', font='Arial -12 bold')
label.pack(fill=tkinter.Y, expand=1)

scale = tkinter.Scale(root, from_=10, to=40, orient=tkinter.HORIZONTAL,
                      command=resize)
scale.set(12)
scale.pack(fill=tkinter.X, expand=1)

quit_ = tkinter.Button(root, text='QUIT', command=root.quit,
                      activeforeground='white', activebackground='red')
quit_.pack()

tkinter.mainloop()
