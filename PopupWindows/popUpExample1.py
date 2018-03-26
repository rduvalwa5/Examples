'''
Created on Mar 23, 2018

@author: rduvalwa2
https://www.tutorialspoint.com/python/tk_messagebox.htm
'''

from tkinter import *
import tkinter.messagebox

top = Tk()
def hello():
    tkinter.messagebox.showinfo("Say Hello", "Hello World")
#    messageBox.showinfo("Say Hello", "Hello World")

B1 = tkinter.Button(top, text = "Say Hello", command = hello)
B1.pack()

top.mainloop()