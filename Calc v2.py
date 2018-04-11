from tkinter import *
root = Tk()
root.minsize(width=115, height=130)
root.maxsize(width=150, height=130)
eq_ua = ""

# Functions


def btn_press(num):
    global eq_ua
    eq_ua = eq_ua + str(num)
    equation.set(eq_ua)


def equal_press():
    global eq_ua
    total = eval(eq_ua)
    equation.set(total)
    eq_ua = ""


def clear_label():
    global eq_ua
    eq_ua = ""
    equation.set("")


def buttonfunc(text, comm, row, col):
    Button(root, text=text, width=2, command=lambda: btn_press(comm)).grid(row=row, column=col)


def buttonfunc_result(text, comm, row, col):
    Button(root, text=text, width=2, command=comm).grid(row=row, column=col)


equation = StringVar()
calculation = Label(root, textvariable=equation, bg="White")

equation.set("Calculator")
calculation.grid(columnspan=4)

# Buttons
one = buttonfunc('1', 1, 1, 0)
two = buttonfunc('2', 2, 1, 1)
three = buttonfunc('3', 3, 1, 2)
four = buttonfunc('4', 4, 2, 0)
five = buttonfunc('5', 5, 2, 1)
six = buttonfunc('6', 6, 2, 2)
seven = buttonfunc('7', 7, 3, 0)
eight = buttonfunc('8', 8, 3, 1)
nine = buttonfunc('9', 9, 3, 2)
zero = buttonfunc('0', 0, 4, 1)

# Operators
op_plus = buttonfunc('+', '+', 1, 3)
op_minus = buttonfunc('-', '-', 2, 3)
op_multiply = buttonfunc('*', '*', 3, 3)
op_divide = buttonfunc('/', '/', 4, 3)

# Getting result
op_equal = buttonfunc_result('=', equal_press, 4, 2)
op_clear = buttonfunc_result('C', clear_label, 4, 0)

root.mainloop()
