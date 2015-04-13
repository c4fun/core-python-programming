import tkinter as tk

class SaveFile(object):
    def __init__(self, master=None, string_to_write=''):
        self.master = tk.Tk()
        self.string_to_write = string_to_write
        self.name_entry = tk.Entry(self.master, text='Input file name')
        self.ok_button = tk.Button(self.master, text='Save to this file',
                                   command=self.ok_button_func)
        self.cancel_button = tk.Button(self.master, text='Cancel',
                                       command=self.master.quit)

        # pack the widgets to show them
        self.name_entry.pack()
        self.ok_button.pack()
        self.cancel_button.pack()

    def ok_button_func(self):
        filename = self.name_entry.get()
        with open(filename, 'wt', encoding='utf=8') as f:
            f.write(self.string_to_write)

    def quit(self):
        # self.master.protocol("WM_DELETE_WINDOW", callback)
        pass


def app(master):
    def open_file(event):
        filename = filename_entry.get()
        with open(filename, 'rt', encoding='utf-8') as f:
            # set the text widget with the text file info
            for line in f:
                text.insert(tk.END, line)

    def save_file(event):
        strings_to_write = text.get("1.0", tk.END)
        SaveFile(string_to_write=strings_to_write)

    # create 3 buttons:
    frame_buttons = tk.Frame(master)
    frame_buttons.grid(row=0)
    open_button = tk.Button(frame_buttons, text='OPEN')
    save_button = tk.Button(frame_buttons, text='SAVE')
    quit_button = tk.Button(frame_buttons, text='QUIT', activeforeground='red',
                            command=master.quit)
    # create 1 label with 1 ENTRY
    filename_label = tk.Label(frame_buttons, text='File')
    filename_entry = tk.Entry(frame_buttons, text='Input file name')

    # bind the open_button + <Button-1> event with open_file
    open_button.bind('<Button-1>', open_file)
    # bind the save_button + <Button-1> event with save_file
    save_button.bind('<Button-1>', save_file)

    # grid them
    filename_label.grid(row=0, column=0)
    filename_entry.grid(row=0, column=1)
    open_button.grid(row=0, column=2)
    save_button.grid(row=0, column=3)
    quit_button.grid(row=0, column=4)


    # create a textbox
    text = tk.Text()
    text.grid(row=1, rowspan=5)


if __name__ == '__main__':
    root = tk.Tk()
    app(root)
    root.mainloop()