from tkinter import *
from tkinter import messagebox
window =Tk()
window.title("Calculator App")
text_space=Entry(window)
text_space.grid(row=1,column=0,rowspan=2,columnspan=4)
def read_input():
    input=text_space.get()
    return input
def check_input():
    try:
        input=float(read_input())
    except ValueError:
        messagebox.showinfo(title="error",message=f"invalid input, enter a number")
        return False
    else:
        return input
def insert_number(button):
    user_input=check_input()
    if user_input!=False:
        text_space.delete(0, END)
        text_space.insert(0, user_input + float(button))

def clear():
    text_space.delete(0, END)
    text_space.insert(0, "")
def add(): 
    global old_input,operation
    user_input=check_input()
    if user_input!=False:
        operation = "addition"
        old_input = float(user_input)
        text_space.delete(0, END)
def minus(): 
    global old_input,operation
    user_input=check_input()
    if user_input!=False:
        operation = "substraction"
        old_input = float(user_input)
        text_space.delete(0, END)
def multiplication():
    global old_input,operation
    user_input=check_input()
    if user_input!=False:
        operation = "multiplication"
        old_input = float(user_input)
        text_space.delete(0, END)
def division():
    global old_input,operation
    user_input=check_input()
    if user_input!=False:
        operation = "division"
        old_input = float(user_input)
        text_space.delete(0, END)
def get_result():
    user_input=check_input()
    if user_input!=False:
        try:
            text_space.delete(0, END)
            if operation == "addition" :
                text_space.insert(0 , float(old_input) + float(user_input))
            if operation == "substraction" :
                text_space.insert(0 , float(old_input) - float(user_input))
            if operation == "multiplication" :
                text_space.insert(0 , float(old_input) * float(user_input))
            if operation == "division" :
                text_space.insert(0, float(old_input) / float(user_input))
        except NameError:
            messagebox.showinfo(title="error",message=f"operation is not defined")
def create_calculator_buttons():
    buttons_list=[]
    button_Plus =Button(window, text="+", font=("Arial",15), bg='#BEB8B7', fg='black', command=add)
    button_Minus=Button(window, text="-", font=("Arial",15), bg='#BEB8B7', fg='black', command=minus)
    button_Multiply=Button(window, text="x", font=("Arial",15), bg='#BEB8B7', fg='black', command=multiplication)
    button_Division=Button(window, text="/", font=("Arial",15), bg='#BEB8B7', fg='black', command=division)
    button_Equal=Button(window, text="=", font=("Arial",15), bg='#BEB8B7', fg='black', command=get_result)
    button_clear=Button(window, text="C", font=("Arial",15), bg='#BEB8B7', fg='black', command=clear)
    buttons_list.extend([button_Plus,button_Minus,button_Multiply,button_Division,button_clear,button_Equal])
    return buttons_list
def grid_calculator_buttons():
    buttons_list=create_calculator_buttons()
    row=3
    column=0
    for button in buttons_list:
        button.grid(row=row,column=column)
        column+=1
        if column==4:
            row+=1
            column=0
grid_calculator_buttons()
window.mainloop()






