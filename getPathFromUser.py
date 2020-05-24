#!python3
#function to get a selected by user folder path to string

def askUserForPath():
    import tkinter as tk
    from tkinter import filedialog
    import sys, re, os
    
    root = tk.Tk()
    root.withdraw() #to hide the empty window, only show Windows GUI
    path = filedialog.askdirectory()
    return path

print(askUserForPath())
