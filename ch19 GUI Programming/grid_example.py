import tkinter as tk
from tkinter import W, E, S, N
import os

if __name__ == '__main__':
    master = tk.Tk()

    tk.Label(master, text="First").grid(row=0, sticky=W)
    tk.Label(master, text="Second").grid(row=1, sticky=W)

    e1 = tk.Entry(master)
    e2 = tk.Entry(master)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)

    check_button = tk.Checkbutton(master, text='check')
    check_button.grid(columnspan=2, sticky = W)

    photo_image = tk.PhotoImage(file="baidulm.gif")
    image_button = tk.Button(master, image=photo_image)
    image_button.grid(row=0, column=2, columnspan=2, rowspan=2,
                  sticky=W+E+N+S, padx=5, pady=5)
    button1 = tk.Button(master, text='Zoom in')
    button2 = tk.Button(master, text='Zoom out')

    button2.grid(row=2, column=3)
    button1.grid(row=2, column=2)

    master.mainloop()