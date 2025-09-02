# Created by Raymond Tilstone

import tkinter as tk      #importing from the tkinter module

#Global variable declaration
calculation = ''

#Functions made for the buttons

def btn_click(symbol):    #Function to add all input from the buttons to a string
    global calculation
    calculation += str(symbol)
    textResult.delete(1.0, 'end')
    textResult.insert(1.0, calculation)
    
def btn_equals():    #Function for the equals button to evaluate the math operations and expressions from the string in order to perform multiple calculations
    global calculation
    try:
        calculation = str(eval(calculation)) # 'eval':This function is used to evaluate the string expression directly
        textResult.delete(1.0, 'end')
        textResult.insert(1.0, calculation)
    except:
        btn_clear()
        textResult.insert(1.0, 'Error')   #Error handling code using a try/except statement
   
def btn_clear():
    global calculation
    calculation =''
    textResult.delete(1.0, 'end')

#Creating the root window
ROOT = tk.Tk()  #importing a window from tkinter
ROOT.geometry('320x500')

ROOT.title('Raymonds Calculator')  #Title of the window

#Creating a frame in the root window
mainFrame = tk.Frame(ROOT, bg = 'BLACK', pady = 30, borderwidth = 2)   #Importing a frame from the tkinter module
mainFrame.pack(fill = tk.BOTH, expand = True)  #.pack helps position the component on the window in a grid like format
mainFrame.columnconfigure(0, weight = 1)
mainFrame.rowconfigure(1, weight = 1)

#Creating a Text widget
textResult = tk.Text(mainFrame, width = 15,height = 2, font = ('Arial', 24, 'bold'), bg = 'GREEN', fg = 'WHITE')   #Importing a text component from the tkinter module
textResult.grid(columnspan = 8)

#Creating the buttons required
button_1 = tk.Button(mainFrame,cursor = 'hand2',width = 5, height = 2, text = '1', font = ('Jokerman', 13, 'bold'),   #lambda is good for writing one-liner functions as well as anonymous functions
                    command = lambda: btn_click(1), bg = 'LIGHTGREEN')
button_1.place(x =0, y= 100)	#Placement of buttons on the main frame

button_2 = tk.Button(mainFrame,cursor = 'hand2',width = 5, height = 2, text = '2', font = ('Jokerman', 13, 'bold'),  
                    command = lambda: btn_click(2), bg = 'LIGHTGREEN')
button_2.place(x =80, y= 100)

button_3 = tk.Button(mainFrame,cursor = 'hand2',width = 5, height = 2, text = '3', font = ('Jokerman', 13, 'bold'),
                    command = lambda: btn_click(3), bg = 'LIGHTGREEN')
button_3.place(x =160, y= 100)

button_4 = tk.Button(mainFrame,cursor = 'hand2',width = 5, height = 2, text = '4', font = ('Jokerman', 13, 'bold'),
                    command = lambda: btn_click(4), bg = 'LIGHTGREEN')
button_4.place(x =0, y= 170)

button_5 = tk.Button(mainFrame,cursor = 'hand2',width = 5, height = 2, text = '5', font = ('Jokerman', 13, 'bold'),
                    command = lambda: btn_click(5), bg = 'LIGHTGREEN')
button_5.place(x =80, y= 170)

button_6 = tk.Button(mainFrame,cursor = 'hand2',width = 5, height = 2, text = '6', font = ('Jokerman', 13, 'bold'),
                    command = lambda: btn_click(6), bg = 'LIGHTGREEN')
button_6.place(x =160, y= 170)

button_7 = tk.Button(mainFrame,cursor = 'hand2',width = 5, height = 2, text = '7', font = ('Jokerman', 13, 'bold'),   #More and more buttons
                    command = lambda: btn_click(7), bg = 'LIGHTGREEN')
button_7.place(x =0, y= 240)

button_8 = tk.Button(mainFrame,cursor = 'hand2',width = 5, height = 2, text = '8', font = ('Jokerman', 13, 'bold'),
                    command = lambda: btn_click(8), bg = 'LIGHTGREEN')
button_8.place(x =80, y= 240)

button_9 = tk.Button(mainFrame,cursor = 'hand2',width = 5, height = 2, text = '9', font = ('Jokerman', 13, 'bold'),
                    command = lambda: btn_click(9), bg = 'LIGHTGREEN')
button_9.place(x =160, y= 240)

button_0 = tk.Button(mainFrame,cursor = 'hand2',width = 5, height = 2, text = '0', font = ('Jokerman', 13, 'bold'),
                    command = lambda: btn_click(0), bg = 'LIGHTGREEN')
button_0.place(x =0, y= 310)

buttonPoint = tk.Button(mainFrame,cursor = 'hand2',width = 5, height = 2, text = '.', font = ('Jokerman', 13, 'bold'),
                        command = lambda: btn_click('.'), bg = 'LIGHTGREEN')
buttonPoint.place(x =80, y= 310)

buttonPlus = tk.Button(mainFrame,cursor = 'hand2',width = 5, height = 2, text = '+', font = ('Jokerman', 13, 'bold'),   #Yes even more buttons
                       command = lambda: btn_click('+'), bg = 'LIME')
buttonPlus.place(x =240, y= 100)

buttonMinus = tk.Button(mainFrame,cursor = 'hand2',width = 5, height = 2, text = '-', font = ('Jokerman', 13, 'bold'),
                        command = lambda: btn_click('-'), bg = 'LIME')
buttonMinus.place(x =240, y= 170)

buttonMultiply = tk.Button(mainFrame,cursor = 'hand2',width = 5, height = 2, text = '*', font = ('Jokerman', 13, 'bold'),
                           command = lambda: btn_click('*'), bg = 'LIME')
buttonMultiply.place(x =240, y= 240)

buttonDivide = tk.Button(mainFrame,cursor = 'hand2',width = 5, height = 2, text = '/', font = ('Jokerman', 13, 'bold'),
                         command = lambda: btn_click('/'), bg = 'LIME')
buttonDivide.place(x =240, y= 310)

buttonBrackets_1 = tk.Button(mainFrame,cursor = 'hand2',width = 5, height = 2, text = '(', font = ('Jokerman', 13, 'bold'),
                            command = lambda: btn_click('('), bg = 'LIGHTGREEN')
buttonBrackets_1.place(x =0, y= 380)

buttonBrackets_2 = tk.Button(mainFrame,cursor = 'hand2',width = 5, height = 2, text = ')', font = ('Jokerman', 13, 'bold'),
                            command = lambda: btn_click(')'), bg = 'LIGHTGREEN')
buttonBrackets_2.place(x =80, y= 380)

buttonClear = tk.Button(mainFrame,cursor = 'hand2',width = 11, height = 2, text = 'CLEAR', font = ('Jokerman', 13, 'bold'),
                        command = lambda: btn_clear(), bg = 'RED')
buttonClear.place(x =160, y= 380)

buttonEquals = tk.Button(mainFrame,cursor = 'hand2',width = 5, height = 2, text = '=', font = ('Arial', 15, 'bold'), bg = 'GREEN',
                         command = btn_equals)
buttonEquals.place(x =160, y= 310)

ROOT.mainloop()	#Updates the GUI after an event takes place and returns back to the mainloop
                    
