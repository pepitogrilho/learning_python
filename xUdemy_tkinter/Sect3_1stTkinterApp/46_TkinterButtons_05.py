# -*- coding: utf-8 -*-
"""
"""
import tkinter as tk
from tkinter import ttk

def greet():
  print("Hello world!")

root = tk.Tk()


greet_button = ttk.Button(root,text="Greet", command=greet)
greet_button.pack(side="top")

quit_button = ttk.Button(root,text="Quit", command=root.destroy)
quit_button.pack(side="top", fill="x")

root.mainloop()
