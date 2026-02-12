import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("350x450")
root.resizable(False, False)

expression = ""
equation = tk.StringVar()

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equalpress():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

entry = tk.Entry(
    root,
    textvariable=equation,
    font=("Arial", 20),
    bd=10,
    relief="sunken",
    justify="right"
)
entry.grid(columnspan=4, ipadx=8, ipady=15)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for text, row, col in buttons:
    if text == "=":
        tk.Button(root, text=text, width=6, height=2,
                  font=("Arial", 14), command=equalpress)\
            .grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(root, text=text, width=6, height=2,
                  font=("Arial", 14),
                  command=lambda t=text: press(t))\
            .grid(row=row, column=col, padx=5, pady=5)

tk.Button(root, text="C", width=28, height=2,
          font=("Arial", 14), bg="red", fg="white",
          command=clear)\
    .grid(row=5, columnspan=4, padx=5, pady=5)

root.mainloop()