import tkinter as tk

def button_click(number):
    current = entry_display.get()
    entry_display.delete(0, tk.END)
    entry_display.insert(0, current + str(number))

def button_clear():
    entry_display.delete(0, tk.END)

def button_operation(op):
    global first_num
    first_num = float(entry_display.get())
    global operation
    operation = op
    entry_display.delete(0, tk.END)

def button_equal():
    second_num = float(entry_display.get())
    entry_display.delete(0, tk.END)
    if operation == "+":
        entry_display.insert(0, first_num + second_num)
    elif operation == "-":
        entry_display.insert(0, first_num - second_num)
    elif operation == "*":
        entry_display.insert(0, first_num * second_num)
    elif operation == "/":
        entry_display.insert(0, first_num / second_num)

root = tk.Tk()
root.title("Calculator")

entry_display = tk.Entry(root, width=20, font=("Arial", 16))
entry_display.grid(row=0, column=0, columnspan=4)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 12),
                       command=lambda t=text: button_click(t) if t.isdigit() else button_operation(t) if t in "+-*/" else button_equal() if t == "=" else button_clear())
    button.grid(row=row, column=col)

root.mainloop()