from tkinter import *
def main():
    root = Tk()
    root.title("Calculator")
    log = Entry(root, width=35, borderwidth=5)
    log.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


    def click(number):
        current = log.get()
        log.delete(0, END)
        log.insert(0, str(current) + str(number))


    def clear():
        log.delete(0, END)


    def add():
        global operator
        operator = "add"
        number_one = log.get()
        global f_num
        f_num = int(number_one)
        log.delete(0, END)


    def equal():
        s_num = log.get()
        log.delete(0, END)
        if operator == "add":
            log.insert(0, f_num + int(s_num))
        elif operator == "subtract":
            log.insert(0, f_num - int(s_num))
        elif operator == "multiply":
            log.insert(0, f_num * int(s_num))
        elif operator == "divide":
            log.insert(0, f_num / int(s_num))


    def subtract():
        global operator
        operator = "subtract"
        number_one = log.get()
        global f_num
        f_num = int(number_one)
        log.delete(0, END)


    def multiply():
        global operator
        operator = "multiply"
        number_one = log.get()
        global f_num
        f_num = int(number_one)
        log.delete(0, END)


    def divide():
        global operator
        operator = "divide"
        number_one = log.get()
        global f_num
        f_num = int(number_one)
        log.delete(0, END)


    button1 = Button(root, text="1",bg="blue",font=("bold"), padx=40, pady=20, command=lambda: click(1))
    button2 = Button(root, text="2",bg="blue",font=("bold"), padx=40, pady=20, command=lambda: click(2))
    button3 = Button(root, text="3",bg="blue",font=("bold"), padx=40, pady=20, command=lambda: click(3))
    button4 = Button(root, text="4",bg="blue",font=("bold"), padx=40, pady=20, command=lambda: click(4))
    button5 = Button(root, text="5",bg="blue",font=("bold"), padx=40, pady=20, command=lambda: click(5))
    button6 = Button(root, text="6",bg="blue",font=("bold"), padx=40, pady=20, command=lambda: click(6))
    button7 = Button(root, text="7",bg="blue",font=("bold"), padx=40, pady=20, command=lambda: click(7))
    button8 = Button(root, text="8",bg="blue",font=("bold"), padx=40, pady=20, command=lambda: click(8))
    button9 = Button(root, text="9",bg="blue",font=("bold"), padx=40, pady=20, command=lambda: click(9))
    button0 = Button(root, text="0",bg="blue",font=("bold"), padx=40, pady=20, command=lambda: click(0))

    button_add = Button(root, text="+",bg="blue",font=("bold"), padx=40, pady=20, command=add)
    button_multiply = Button(root, text="*",bg="blue",font=("bold"), padx=42, pady=20, command=multiply)
    button_divide = Button(root, text="/",bg="blue",font=("bold"), padx=42, pady=20, command=divide)
    button_subtract = Button(root, text="-",bg="blue",font=("bold"), padx=42, pady=20, command=subtract)

    button_equal = Button(root, text="=",bg="blue",font=("bold"), padx=90, pady=20, command=equal)
    button_clear = Button(root, text="Clear",bg="blue",font=("bold"), padx=75, pady=20, command=clear)
    button1.grid(row=3, column=0)
    button2.grid(row=3, column=1)
    button3.grid(row=3, column=2)

    button4.grid(row=2, column=0)
    button5.grid(row=2, column=1)
    button6.grid(row=2, column=2)

    button7.grid(row=1, column=0)
    button8.grid(row=1, column=1)
    button9.grid(row=1, column=2)

    button0.grid(row=4, column=0)

    button_clear.grid(row=4, column=1, columnspan=2)
    button_add.grid(row=5, column=0)
    button_equal.grid(row=5, column=1, columnspan=2)

    button_subtract.grid(row=6, column=0)
    button_multiply.grid(row=6, column=1)
    button_divide.grid(row=6, column=2)
    root.mainloop()
if __name__=="__main__":
    main()
