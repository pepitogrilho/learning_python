# -*- coding: utf-8 -*-
"""
"""
import tkinter as tk

root = tk.Tk()

root.geometry("600x400")

rectangle_1 = tk.Label(root, text="Rectangle 1", bg="green", fg="white")
rectangle_1.pack(side="left", fill="both", expand=True)

rectangle_2 = tk.Label(root, text="Rectangle 2", bg="red", fg="white")
rectangle_2.pack(fill="both", expand=True)


root.mainloop()
