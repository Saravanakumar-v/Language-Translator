# GUI 
# Libraries used: googletrans 3.0.0, Tkinter

import main # main module

from tkinter import *
import string
from tkinter import ttk
from googletrans import LANGUAGES,LANGCODES

_mainWindow = Tk()                             # root Window
_mainWindow.geometry('770x310')

_mainWindow.resizable(0,0)
_mainWindow.config(bg = 'ghost white')

_mainWindow.title("Language Translator")

Label(_mainWindow,                             # by mentioning root window the widget be added to mainloop
    text = "LANGUAGE TRANSLATOR", 
    font = "calibri 20 bold", 
    bg='white smoke').pack()

Label(_mainWindow,
    text ="English", 
    font = 'calibri 13 bold', 
    bg ='white smoke').place(x= 30,y=62)

Input_text = Text(_mainWindow,
    font = 'calibri 20',
    width = 22)
Input_text.place(x= 30,y= 100,height= 180)

Label(_mainWindow,
    text ="Output: ", 
    font = 'calibri 13 bold', 
    bg ='white smoke').place(x=450,y=62)

Output_text = Text(_mainWindow,
    font = 'calibri 20',
    width  =22)
Output_text.place(x = 440,y = 100,height= 180)

languages = list(LANGUAGES.values())            # list of language for translation
languages = [x.title() for x in languages]      # convert string in list to title format

dest_lang = ttk.Combobox(_mainWindow,
    values= languages, 
    width =30)

dest_lang.place(x= 520,y=65)
dest_lang.set('English')

trans_btn = Button(_mainWindow, 
    text = 'Translate',
    font = 'calibri 12 bold',
    pady = 5,
    command= main.getInput)                     # calls the respective function when the button is clicked

trans_btn.place(x = 355, y= 150 )

_mainWindow.mainloop()                          # Add all the widgets to mainloop