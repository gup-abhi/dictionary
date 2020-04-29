# importing all from tkinter
from tkinter import *

# importing messagebox from tkinter
from tkinter import messagebox

# importing PyDictionary from PyDictionary
from PyDictionary import PyDictionary

# importing time module
import time

# creating function for finding meaning for specific word given by the user
def findMeaning():
    # extracting the user input from entry field
    word = entry.get()
    # creating object of Pydictionary
    dictionary = PyDictionary()
    # storing the meaning from the dictionary
    meaning = dictionary.meaning(word)
    # putting program to the sleep
    time.sleep(3)
    # printing meaning to the messagebox
    mean = messagebox.showinfo("Meaning", ""+str(meaning))

# creating window
root = Tk()
# proving size of the window
root.geometry("350x150")

# creating entry field to get user input
entry = Entry(root, font = ("times", 15, "bold"))
entry.grid(row = 2, column = 2, padx = 10, pady = 10)

# creating button to call our function to find meaning
meaning = Button(root, text = "Meaning", command = findMeaning)
meaning.grid(row = 2, column = 4, padx = 10, pady = 10)

# creating loop for the window
root.mainloop()
