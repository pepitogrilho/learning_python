# -*- coding: utf-8 -*-
"""
* Default: side="top"
* side="left" or side="right", widgets takes up all HORIZONTAL space
* side="top" or side="bottom", widgets takes up all VERTICAL space
"""

import tkinter as tk

root = tk.Tk()

root.geometry("600x400")

rectangle_1 = tk.Label(root, text="Rectangle 1", bg="green", fg="white")
rectangle_1.pack(side="right", fill="both")

rectangle_2 = tk.Label(root, text="Rectangle 2", bg="red", fg="white")
rectangle_2.pack(side="bottom", fill="both")                                               #default: side="left"


root.mainloop()



 