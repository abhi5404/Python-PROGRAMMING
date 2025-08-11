from tkinter import *
import math
import tkinter as tk

is_shift_active = False

# Function to add in the entry of text display
def toggle_shift():
    global is_shift_active
    is_shift_active = not is_shift_active
    # Update the Shift button color to indicate state
    shift_button["bg"] = 'white' if is_shift_active else '#3C3636'

#Index function
def button_click(char):
    global calc_operator
    calc_operator += str(char)
    text_input.set(calc_operator)
    # Auto-scroll the entry widget
    text_display.xview_moveto(1)  # Scroll to the right

# Function to clear the whole entry of text display
def button_clear_all():
    global calc_operator
    calc_operator = ""
    text_input.set("")

# Function to delete one by one from the last in the entry of text display
def button_delete():
    global calc_operator
    text = calc_operator[:-1]
    calc_operator = text
    text_input.set(text)

# Function to calculate the factorial of a number
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

def fact_func():
    global calc_operator
    result = str(factorial(int(calc_operator)))
    calc_operator = result
    text_input.set(result)

# Function to calculate trigonometric numbers of an angle
def trig_sin():
    global calc_operator
    if is_shift_active:
        calc_operator += "arcsin"
        text_input.set(calc_operator)
    else:
        if calc_operator == "" or calc_operator[-1] == "(":
            calc_operator += "sin"
            text_input.set(calc_operator)
        else:
            try:
                value = float(calc_operator)
                result = str(round(math.sin(math.radians(value)), 10))
                calc_operator = result
                text_input.set(result)
            except ValueError:
                text_input.set("ERROR")

def trig_cos():
    global calc_operator
    if is_shift_active:
        calc_operator += "arccos"
        text_input.set(calc_operator)
    else:
        if calc_operator == "" or calc_operator[-1] == "(":
            calc_operator += "cos"
            text_input.set(calc_operator)
        else:
            try:
                value = float(calc_operator)
                result = str(round(math.cos(math.radians(value)), 10))
                calc_operator = result
                text_input.set(result)
            except ValueError:
                text_input.set("ERROR")

def trig_tan():
    global calc_operator
    if is_shift_active:
        calc_operator += "arctan"
        text_input.set(calc_operator)
    else:
        if calc_operator == "" or calc_operator[-1] == "(":
            calc_operator += "tan"
            text_input.set(calc_operator)
        else:
            try:
                value = float(calc_operator)
                result = str(round(math.tan(math.radians(value)), 10))
                calc_operator = result
                text_input.set(result)
            except ValueError:
                text_input.set("ERROR")

def combination(n, r):
    if r > n:
        return "ERROR"
    else:
        return math.comb(n, r)

def permutation(n, r):
    if r > n:
        return "ERROR"
    else:
        return math.perm(n, r)

def square_root():
    global calc_operator
    try:
        number = float(calc_operator)
        if number >= 0:
            result = math.sqrt(number)
            calc_operator = str(result) 
        else:
            calc_operator = "ERROR"
        text_input.set(calc_operator) 
    except ValueError:
        calc_operator = "ERROR"
        text_input.set(calc_operator)

def third_root():
    global calc_operator
    try:
        value = float(calc_operator)
        temp = str(value ** (1 / 3))
        calc_operator = temp
    except ValueError:
        temp = "ERROR"
    except Exception as e:
        temp = f"ERROR: {str(e)}"
    text_input.set(temp)

def sign_change():
    global calc_operator
    if calc_operator[0] == '-':
        temp = calc_operator[1:]
    else:
        temp = '-' + calc_operator
    calc_operator = temp
    text_input.set(temp)

def percent():
    global calc_operator
    temp = str(eval(calc_operator + '/100'))
    calc_operator = temp
    text_input.set(temp)

def button_equal():
    global calc_operator
    try:
        if 'nCr(' in calc_operator:
            n, r = map(int, calc_operator.split('nCr(')[1].rstrip(')').split(','))
            temp_op = str(combination(n, r))
        elif 'nPr(' in calc_operator:
            n, r = map(int, calc_operator.split('nPr(')[1].rstrip(')').split(','))
            temp_op = str(permutation(n, r))
        elif 'arcsin(' in calc_operator:
            value = float(calc_operator.split('arcsin(')[1].rstrip(')'))
            result_radians = math.asin(value)
            result_degrees = math.degrees(result_radians)
            temp_op = str(round(result_degrees))
        elif 'arccos(' in calc_operator:
            value = float(calc_operator.split('arccos(')[1].rstrip(')'))
            result_radians = math.acos(value)
            result_degrees = math.degrees(result_radians)
            temp_op = str(round(result_degrees))
        elif 'arctan(' in calc_operator:
            value = float(calc_operator.split('arctan(')[1].rstrip(')'))
            result_radians = math.atan(value)
            result_degrees = math.degrees(result_radians)
            temp_op = str(round(result_degrees))
        elif 'sin(' in calc_operator:
            value = float(calc_operator.split('sin(')[1].rstrip(')'))
            temp_op = str(round(math.sin(math.radians(value)), 10))
        elif 'cos(' in calc_operator:
            value = float(calc_operator.split('cos(')[1].rstrip(')'))
            temp_op = str(round(math.cos(math.radians(value)), 10))
        elif 'tan(' in calc_operator:
            value = float(calc_operator.split('tan(')[1].rstrip(')'))
            temp_op = str(round(math.tan(math.radians(value)), 10))
        else:
            temp_op = str(eval(calc_operator))

        text_input.set(temp_op)
        calc_operator = temp_op
    except Exception:
        text_input.set("ERROR")

def calculate_exponent():
    global calc_operator
    try:
        value = float(calc_operator)
        result = str(round(math.exp(value), 10))
        text_input.set(result)
        calc_operator = result
    except ValueError:
        text_input.set("ERROR")

'''
Variables
'''
sin, cos, tan = math.sin, math.cos, math.tan
log, ln = math.log10, math.log
e = math.exp
p = math.pi
E = '10*'

tk_calc = Tk()

tk_calc.configure(bg="#293C4A", bd=10)
tk_calc.title("Scientific Calculator")
tk_calc.resizable(False, False)

calc_operator = ""
text_input = StringVar()

# Updated Entry widget to allow for horizontal scrolling
text_display = Entry(tk_calc, font=('sans-serif', 20, 'bold'), textvariable=text_input,
                     bd=5, insertwidth=5, bg='#BBB', justify='right')
text_display.grid(columnspan=5, padx=10, pady=15)

button_params = {'bd': 5, 'fg': '#BBB', 'bg': '#3C3636', 'font': ('sans-serif', 20, 'bold')}
button_params_main = {'bd': 5, 'fg': '#000', 'bg': '#BBB', 'font': ('sans-serif', 20, 'bold')}


'''
# Buttons
# '''

# Shift button
shift_button = Button(tk_calc, button_params, text='Shift', command=toggle_shift)
shift_button.grid(row=1, column=0, sticky="nsew")

# Add label next to shift button using place() to control the exact position without affecting grid layout
shift_info_label = Label(tk_calc, text="(This enables inverse trigonometric functions)",
                         font=('Arial', 12), fg='grey')  # Adjust font size and color as needed
shift_info_label.place(x=shift_button.winfo_x() + shift_button.winfo_width() + 95, y=shift_button.winfo_y() + 95)



# Absolute value of a number
abs_value = Button(tk_calc, button_params, text='abs',
                   command=lambda:button_click('abs')).grid(row=2, column=0, sticky="nsew")
# Remainder of a division
modulo = Button(tk_calc, button_params, text='mod',
                command=lambda:button_click('%')).grid(row=2, column=1, sticky="nsew")





# Comma button
com = Button(tk_calc, button_params, text='com',
                 command=lambda:button_click(',')).grid(row=2, column=2, sticky="nsew")





# Factorial of a number
factorial_button = Button(tk_calc, button_params, text='x!',
                   command=fact_func).grid(row=4, column=2, sticky="nsew")
# Euler's number e
eulers_num = Button(tk_calc, button_params, text='e',
                    command=lambda:button_click(str(math.exp(1)))).grid(row=2, column=4, sticky="nsew")

#--2nd row--
# Sine of an angle in degrees
sine = Button(tk_calc, button_params, text='sin',
             command=trig_sin).grid(row=3, column=0, sticky="nsew")
# Cosine of an angle in degrees
cosine = Button(tk_calc, button_params, text='cos',
             command=trig_cos).grid(row=3, column=1, sticky="nsew")
# Tangent of an angle in degrees
tangent = Button(tk_calc, button_params, text='tan',
             command=trig_tan).grid(row=3, column=2, sticky="nsew")


# Temprary test purpose

combination_button = Button(tk_calc, button_params, text='nCr',
                            command=lambda: button_click('nCr(')).grid(row=3, column=3, sticky="nsew")

# Permutation button (nPr)
permutation_button = Button(tk_calc, button_params, text='nPr',
                            command=lambda: button_click('nPr(')).grid(row=2, column=3, sticky="nsew")


# Pi(3.14...) number
pi_num = Button(tk_calc, button_params, text='π',
                command=lambda:button_click(str(math.pi))).grid(row=3, column=4, sticky="nsew")

#--3rd row--
# Power of 2
second_power = Button(tk_calc, button_params, text='x\u00B2',
             command=lambda:button_click('**2')).grid(row=4, column=0, sticky="nsew")
# Power of 3
third_power = Button(tk_calc, button_params, text='x\u00B3',
             command=lambda:button_click('**3')).grid(row=4, column=1, sticky="nsew")



# Inverse number
inv_power = Button(tk_calc, button_params, text='x\u207b\xb9',
             command=lambda:button_click('**(-1)')).grid(row=4, column=3, sticky="nsew")
# Powers of 10
tens_powers = Button(tk_calc, button_params, text='10^x', font=('sans-serif', 15, 'bold'),
                     command=lambda:button_click('10**')).grid(row=4, column=4, sticky="nsew")

#--4th row--
# Square root of a number
square_root = Button(tk_calc, button_params, text='\u00B2\u221A',
                     command=square_root).grid(row=5, column=0, sticky="nsew")
# Third root of a number
third_root = Button(tk_calc, button_params, text='\u00B3\u221A',
                    command=third_root).grid(row=5, column=1, sticky="nsew")
# nth root of a number
nth_root = Button(tk_calc, button_params, text='\u221A',
                  command=lambda:button_click('**(1/')).grid(row=5, column=2, sticky="nsew")
# Logarithm of a number with base 10
log_base10 = Button(tk_calc, button_params, text='log\u2081\u2080', font=('sans-serif', 16, 'bold'),
                   command=lambda:button_click('log')).grid(row=5, column=3, sticky="nsew")
# Logarithm of a number with base e (ln)
log_basee = Button(tk_calc, button_params, text='ln',
                   command=lambda:button_click('ln')).grid(row=5, column=4, sticky="nsew")

#--5th row--
# Add a left parentheses
left_par = Button(tk_calc, button_params, text='(',
                  command=lambda:button_click('(')).grid(row=6, column=0, sticky="nsew")
# Add a right parentheses
right_par = Button(tk_calc, button_params, text=')',
                   command=lambda:button_click(')')).grid(row=6, column=1, sticky="nsew")
# Change the sign of a number
signs = Button(tk_calc, button_params, text='\u00B1',
               command=sign_change).grid(row=6, column=2, sticky="nsew")
# Transform number to percentage
percentage = Button(tk_calc, button_params, text='%',
               command=percent).grid(row=6, column=3, sticky="nsew")


# Define the e^x button
ex = Button(tk_calc, button_params, text='e^x', command=calculate_exponent).grid(row=6, column=4, sticky="nsew")

#--6th row--
button_7 = Button(tk_calc, button_params_main, text='7', command=lambda:button_click('7')).grid(row=7, column=0, sticky="nsew")
button_8 = Button(tk_calc, button_params_main, text='8', command=lambda:button_click('8')).grid(row=7, column=1, sticky="nsew")
button_9 = Button(tk_calc, button_params_main, text='9', command=lambda:button_click('9')).grid(row=7, column=2, sticky="nsew")
button_div = Button(tk_calc, button_params, text='/',
                    command=lambda:button_click('/')).grid(row=7, column=3, sticky="nsew")
button_clear = Button(tk_calc, button_params, text='C',
                     command=button_clear_all).grid(row=7, column=4, sticky="nsew")

#--7th row--
button_4 = Button(tk_calc, button_params_main, text='4', command=lambda:button_click('4')).grid(row=8, column=0, sticky="nsew")
button_5 = Button(tk_calc, button_params_main, text='5', command=lambda:button_click('5')).grid(row=8, column=1, sticky="nsew")
button_6 = Button(tk_calc, button_params_main, text='6', command=lambda:button_click('6')).grid(row=8, column=2, sticky="nsew")
button_mult = Button(tk_calc, button_params, text='*',
                     command=lambda:button_click('*')).grid(row=8, column=3, sticky="nsew")
button_delete = Button(tk_calc, button_params, text='DEL',
                       command=button_delete).grid(row=8, column=4, sticky="nsew")

#--8th row--
button_1 = Button(tk_calc, button_params_main, text='1', command=lambda:button_click('1')).grid(row=9, column=0, sticky="nsew")
button_2 = Button(tk_calc, button_params_main, text='2', command=lambda:button_click('2')).grid(row=9, column=1, sticky="nsew")
button_3 = Button(tk_calc, button_params_main, text='3', command=lambda:button_click('3')).grid(row=9, column=2, sticky="nsew")
button_sub = Button(tk_calc, button_params, text='-',
                    command=lambda:button_click('-')).grid(row=9, column=3, sticky="nsew")
button_eq = Button(tk_calc, button_params, text='=',
                   command=button_equal).grid(row=9, column=4, rowspan=2,sticky="nsew")

#--9th row--
button_0 = Button(tk_calc, button_params_main, text='0', command=lambda:button_click('0')).grid(row=10, column=0, columnspan=2, sticky="nsew")
button_dot = Button(tk_calc, button_params_main, text='.', command=lambda:button_click('.')).grid(row=10, column=2, sticky="nsew")
button_add = Button(tk_calc, button_params, text='+',
                    command=lambda:button_click('+')).grid(row=10, column=3, sticky="nsew")
# Run the tkinter event loop
tk_calc.mainloop()