"""
This is a simple text editor.
Open: It can open a file as a text file
Quit: Quit the text editor.
Save: Open a new Toplevel entry box allowing customer to input customized filename.

Features: The App and SaveFile are two separate frames.
    They will not show together
"""

import tkinter as tk

class SaveFile(tk.Toplevel):
    def __init__(self, original_frame, string_to_write=''):
        tk.Toplevel.__init__(self)
        self.original_frame = original_frame
        self.string_to_write = string_to_write
        self.name_entry = tk.Entry(self, text='Input file name')
        self.ok_button = tk.Button(self, text='Save to this file',
                                   command=self.ok_button_func)
        self.cancel_button = tk.Button(self, text='Cancel',
                                       command=self.onClose)

        # pack the widgets to show them
        self.name_entry.pack()
        self.ok_button.pack()
        self.cancel_button.pack()

    def onClose(self):
        self.destroy()
        self.original_frame.show()

    def ok_button_func(self):
        filename = self.name_entry.get()
        with open(filename, 'wt', encoding='utf=8') as f:
            f.write(self.string_to_write)

    def quit(self):
        # self.master.protocol("WM_DELETE_WINDOW", callback)
        pass

    
class App(object):
    def __init__(self, master=None):

        self.master = master
        # create 3 buttons in a frame:
        self.frame_buttons = tk.Frame(master)
        self.frame_buttons.grid(row=0)
        self.open_button = tk.Button(self.frame_buttons, text='OPEN')
        self.save_button = tk.Button(self.frame_buttons, text='SAVE')
        self.quit_button = tk.Button(self.frame_buttons, text='QUIT', activeforeground='red',
                                     command=master.quit)
        # create 1 label with 1 ENTRY
        self.filename_label = tk.Label(self.frame_buttons, text='File')
        self.filename_entry = tk.Entry(self.frame_buttons, text='Input file name')

        # bind the self.open_button + <Button-1> event with open_file
        self.open_button.bind('<Button-1>', self.open_file)
        # bind the self.save_button + <Button-1> event with save_file
        self.save_button.bind('<Button-1>', self.save_file)

        # grid them
        self.filename_label.grid(row=0, column=0)
        self.filename_entry.grid(row=0, column=1)
        self.open_button.grid(row=0, column=2)
        self.save_button.grid(row=0, column=3)
        self.quit_button.grid(row=0, column=4)

        # create a textbox in another frame
        self.text = tk.Text()
        self.text.grid(row=1, rowspan=5)

    def open_file(self, event):
        filename = self.filename_entry.get()
        with open(filename, 'rt', encoding='utf-8') as f:
            # set the text widget with the text file info
            for line in f:
                self.text.insert(tk.END, line)

    def save_file(self, event):
        strings_to_write = self.text.get("1.0", tk.END)
        self.hide()
        SaveFile(self, string_to_write=strings_to_write)

    def hide(self):
        """hide the current self"""
        self.master.withdraw()

    def show(self):
        """show the frame after the otherFrame is destroyed"""
        self.master.update()
        self.master.deiconify()


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()