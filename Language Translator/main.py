
# Language Translator 
# Libraries used: googletrans 3.0.0

from typing import Type
import GUI # GUI module

from tkinter.constants import INSERT  
from tkinter import messagebox  
from googletrans import Translator
from tkinter import StringVar           

# translate the input text and return to Front-end
def Translate(input, language):              
    translator = Translator() 
    try:                                    # initialize the Library: googletrans 3.0.0 Translator
        if(len(input) == 0):
            msg = 'Input Error : No input is given'
            messagebox.showerror("Error message", msg)      # shows error message
            raise TypeError                                 # When TypeError occur the program raise error
        
        else:
            translated = translator.translate(input,src= 'en',dest= language)         
            GUI.Output_text.insert(INSERT,translated.text)    # INSERT the text output to the Front-end textBox
    
    except TypeError:
        print("Input Error: No input is given.")
        GUI._mainWindow.mainloop()

# function get the input for translation from Front-end
def getInput():
    ip = StringVar()                        # set the variable to String
    lang = GUI.dest_lang.get()
    ip = GUI.Input_text.get("1.0",'end-1c') # get the text to translate
    
    GUI.Output_text.delete("1.0","end")     # removes the previous translated text from Front-end
    Translate(ip, lang)                     # send the value to respective function()

