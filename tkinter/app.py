"""
tkinter app



everything tkinter:

['ACTIVE', 'ALL', 'ANCHOR', 'ARC', 'BASELINE', 'BEVEL', 'BOTH', 'BOTTOM', 'BROWSE', 'BUTT', 'BaseWidget', 'BitmapImage', 'BooleanVar', 'Button', 'CASCADE', 'CENTER', 'CHAR', 'CHECKBUTTON', 'CHORD', 'COMMAND', 'CURRENT', 'CallWrapper', 'Canvas', 'Checkbutton', 'DISABLED', 'DOTBOX', 'DoubleVar', 'E', 'END', 'EW', 'EXCEPTION', 'EXTENDED', 'Entry', 'Event', 'EventType', 'FALSE', 'FIRST', 'FLAT', 'Frame', 'GROOVE', 'Grid', 'HIDDEN', 'HORIZONTAL', 'INSERT', 'INSIDE', 'Image', 'IntVar', 'LAST', 'LEFT', 'Label', 'LabelFrame', 'Listbox', 'MITER', 'MOVETO', 'MULTIPLE', 'Menu', 'Menubutton', 'Message', 'Misc', 'N', 'NE', 'NO', 'NONE', 'NORMAL', 'NS', 'NSEW', 'NUMERIC', 'NW', 'NoDefaultRoot', 'OFF', 'ON', 'OUTSIDE', 'OptionMenu', 'PAGES', 'PIESLICE', 'PROJECTING', 'Pack', 'PanedWindow', 'PhotoImage', 'Place', 'RADIOBUTTON', 'RAISED', 'READABLE', 'RIDGE', 'RIGHT', 'ROUND', 'Radiobutton', 'S', 'SCROLL', 'SE', 'SEL', 'SEL_FIRST', 'SEL_LAST', 'SEPARATOR', 'SINGLE', 'SOLID', 'SUNKEN', 'SW', 'Scale', 'Scrollbar', 'Spinbox', 'StringVar', 'TOP', 'TRUE', 'Tcl', 'TclError', 'TclVersion', 'Text', 'Tk', 'TkVersion', 'Toplevel', 'UNDERLINE', 'UNITS', 'VERTICAL', 'Variable', 'W', 'WORD', 'WRITABLE', 'Widget', 'Wm', 'X', 'XView', 'Y', 'YES', 'YView', '_VersionInfoType', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '_checkbutton_count', '_cnfmerge', '_default_root', '_destroy_temp_root', '_exit', '_flatten', '_get_default_root', '_get_temp_root', '_join', '_magic_re', '_parse_version', '_setit', '_space_re', '_splitdict', '_stringify', '_support_default_root', '_test', '_tkerror', '_tkinter', '_varnum', 'collections', 'constants', 'enum', 'getboolean', 'getdouble', 'getint', 'image_names', 'image_types', 'mainloop', 're', 'sys', 'types', 'wantobjects']
"""
import tkinter as tk

root = tk.Tk()

# Set title
root.title("New App")

# App heading
heading = tk.Label(root, text="HELLO WORLD", font='45', fg='yellow', bg='gray', underline='2', borderwidth='1', width='800', padx='8', pady='8')
heading.pack()

# UI ELEMENTS

# frames
first_frame = tk.Frame(root, bg='#f4d67a', borderwidth='8', height='480', name='hello', width='300', padx='8')
first_frame.pack(side='left', padx='9', fill="both", expand=20)
# first_frame.rowconfigure(0, weight=1)


second_frame = tk.Frame(root, bg="#f45e39", height=480, padx="10", width="300", name="frame2")
second_frame.pack(side="left", padx='15', fill="both", expand=20) 

third_frame = tk.Frame(root, bg="#e39", height=480, width="300", padx="10", name="frame3")
third_frame.pack(side="left", padx='15',fill="both", expand=20)

# first frame components
mylabel = tk.Label(first_frame, text="MAGPINY", underline=8,bg="black", fg="#4eb")
mylabel.pack(side="top",fill="x")

textInput = tk.Entry(first_frame, justify="center")
textInput.pack(side="top", pady="8")

# second frame components
f2label = tk.Label(second_frame, text="Programming is Fun", background="black", fg="white", name="label2")
f2label.pack(side="top", fill="x")

# third frame components

f3label = tk.Label(third_frame, text="Just another Frame", background="black", fg="white", name="label2", justify="center")
f3label.pack(side="top", fill="x")

#anchor = 'n|s|w|e|ne|se|nw|sw|center' 

# Set window dimensions
root.geometry("900x500")

root.resizable(True, True)

root.mainloop()
