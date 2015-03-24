from functools import partial as pto
from tkinter import Tk, Button, X, messagebox

WARN = 'warn'
CRITICAL = 'critical'
REGULAR = 'regular'

# define the SIGNS levels
SIGNS = {
    'do not enter': CRITICAL,
    'railroad crossing': WARN,
    '55\nspeed limit': REGULAR,
    'wrong way': CRITICAL,
    'merging traffic': WARN,
    'one way': REGULAR,
}

def critical_msg():
    return messagebox.showerror('Error', 'Error Button Pressed!')

def warn_msg():
    return messagebox.showwarning('Warning', 'Warning Button Pressed!')

def info_msg():
    return messagebox.showinfo('Info', 'Info Button Pressed!')
# critical_msg = lambda: messagebox.showerror('Error', 'Error Button Pressed!')
# warn_msg = lambda: messagebox.showwarning('Warning','Warning Button Pressed!')
# info_msg = lambda: messagebox.showinfo('Info', 'Info Button Pressed!')

top = Tk()
top.title('Road Signs')
Button(top, text='QUIT', command=top.quit, bg='red', fg='white').pack()

my_button = pto(Button, top)
# Here is 2 level of partial
critical_button = pto(my_button, command=critical_msg, bg='white', fg='red')
warn_button = pto(my_button, command=warn_msg, bg='goldenrod1')
regular_button = pto(my_button, command=info_msg, bg='white')

for eachSign in SIGNS:
    signType = SIGNS[eachSign]
    # In non-web environment, eval & for can be used to dynamically
    # generate expressions to execute
    cmd = '%s_button(text=%r%s).pack(fill=X, expand=True)'%(
        signType, eachSign,
        '.upper()' if signType == CRITICAL else '.title()')
    eval(cmd)

top.mainloop()


