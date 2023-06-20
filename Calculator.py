from tkinter import *
from tkinter import colorchooser
from tkinter import messagebox
from tkinter import ttk
from time import sleep
from random import randint


def download():
    global bar
    while bar['value'] < 100:
        bar['value'] += randint(5, 20)
        sleep(0.5)
        percent.set(f"{int(bar['value'])}%")
        new_window.update()
        if bar['value'] >= 90:
            new_window.destroy()
            break


count = 0
def handle_window_close():
    global count
    new_window.destroy()
    if messagebox.askokcancel(title='Error', message='Do you want to exit?', icon='question'):
        count = 1
    else:
        count = -1


new_window = Tk()
new_window.title('Calculator')
new_window.protocol("WM_DELETE_WINDOW", lambda: handle_window_close())
percent = StringVar()

bar = ttk.Progressbar(new_window, length=300)
bar.pack()
bar_label = Label(new_window, textvariable=percent)
bar_label.pack()
submit_button = Button(new_window, text='DOWNLOAD', fg='black', bg='white', command=download)
submit_button.pack()
new_window.mainloop()


def button_press(num):
    global equation_text
    global equation_label

    try:
        equation_text = equation_text + str(num)

        if len(equation_text) >= 24:
            messagebox.showwarning(title='Error', message='The area is full')
        else:
            equation_label.set(equation_text)
    except Exception as error:
        print(error)


def equals():
    global equation_text

    try:

        total = str(eval(equation_text))

        equation_label.set(total)

        equation_text = total

    except SyntaxError:

        equation_label.set("syntax error")

        equation_text = ""

    except ZeroDivisionError:

        equation_label.set("arithmetic error")

        equation_text = ""
    except TypeError:
        equation_label.set("syntax error")
        equation_text = ""


def clear():
    global equation_text

    equation_label.set("")

    equation_text = ""


def delete():
    global equation_text
    equation_text = equation_text[0:len(equation_text) - 1]
    equation_label.set(equation_text)


def change_window_color():
    global window
    window.config(background=colorchooser.askcolor()[1])


def change_frame_color():
    global frame
    frame.config(background=colorchooser.askcolor()[1])


def change_label_color():
    global label
    label.config(background=colorchooser.askcolor()[1])


def quitt():
    quit()

if count == 0 or count == 1:
    window = Tk()

    window.title("Calculator program")

    window.config(background='yellow')

    equation_text = ""

    equation_label = StringVar()

    menubar = Menu(window)
    window.config(menu=menubar)
    FileMenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(menu=FileMenu, label='File')
    FileMenu.add_command(label='Change background', command=change_window_color)
    FileMenu.add_command(label='Change frame', command=change_frame_color)
    FileMenu.add_command(label='Change label', command=change_label_color)
    FileMenu.add_separator()
    FileMenu.add_command(label='Exit', command=quitt)

    frame = Frame(window, pady=10, relief=RAISED, borderwidth=5, bg='black')
    frame.pack()

    label = Label(frame, textvariable=equation_label, font=('consolas', 20), width=24, height=2, bg='#00FF00',
                  fg='black')
    label.grid(row=0, column=0, columnspan=5)

    delete = Button(frame, text="Del", height=3, width=6, font=35, fg='black', bg='white',
                    command=delete)
    delete.grid(row=1, column=3)

    comma = Button(frame, text='_', height=3, width=6, font=35, fg='black', bg='white',
                   command=lambda: button_press('_'))
    comma.grid(row=1, column=0)

    bracket1 = Button(frame, text='(', height=3, width=6, font=35, fg='black', bg='white',
                      command=lambda: button_press('('))
    bracket1.grid(row=1, column=1)

    bracket2 = Button(frame, text=')', height=3, width=6, font=35, fg='black', bg='white',
                      command=lambda: button_press(')'))
    bracket2.grid(row=1, column=2)

    button1 = Button(frame, text=1, height=3, width=6, font=35, fg='green', bg='red',
                     command=lambda: button_press(1))
    button1.grid(row=2, column=0)

    button2 = Button(frame, text=2, height=3, width=6, font=35, fg='green', bg='red',
                     command=lambda: button_press(2))
    button2.grid(row=2, column=1)

    button3 = Button(frame, text=3, height=3, width=6, font=35, fg='green', bg='red',
                     command=lambda: button_press(3))
    button3.grid(row=2, column=2)

    button4 = Button(frame, text=4, height=3, width=6, font=35, fg='green', bg='red',
                     command=lambda: button_press(4))
    button4.grid(row=3, column=0)

    button5 = Button(frame, text=5, height=3, width=6, font=35, fg='green', bg='red',
                     command=lambda: button_press(5))
    button5.grid(row=3, column=1)

    button6 = Button(frame, text=6, height=3, width=6, font=35, fg='green', bg='red',
                     command=lambda: button_press(6))
    button6.grid(row=3, column=2)

    button7 = Button(frame, text=7, height=3, width=6, font=35, fg='green', bg='red',
                     command=lambda: button_press(7))
    button7.grid(row=4, column=0)

    button8 = Button(frame, text=8, height=3, width=6, font=35, fg='green', bg='red',
                     command=lambda: button_press(8))
    button8.grid(row=4, column=1)

    button9 = Button(frame, text=9, height=3, width=6, font=35, fg='green', bg='red',
                     command=lambda: button_press(9))
    button9.grid(row=4, column=2)

    button0 = Button(frame, text=0, height=3, width=6, font=35, fg='green', bg='red',
                     command=lambda: button_press(0))
    button0.grid(row=5, column=1)

    plus = Button(frame, text='+', height=3, width=6, font=35, fg='black', bg='white',
                  command=lambda: button_press('+'))
    plus.grid(row=2, column=3)

    minus = Button(frame, text='-', height=3, width=6, font=35, fg='black', bg='white',
                   command=lambda: button_press('-'))
    minus.grid(row=3, column=3)

    multiply = Button(frame, text='*', height=3, width=6, font=35, fg='black', bg='white',
                      command=lambda: button_press('*'))
    multiply.grid(row=4, column=3)

    divide = Button(frame, text='/', height=3, width=6, font=35, fg='black', bg='white',
                    command=lambda: button_press('/'))
    divide.grid(row=5, column=3)

    equal = Button(frame, text='=', height=18, width=6, font=35, fg='yellow', bg='blue',
                   command=equals)
    equal.grid(row=1, column=4, rowspan=5)

    decimal = Button(frame, text='.', height=3, width=6, font=35, fg='black', bg='white',
                     command=lambda: button_press('.'))
    decimal.grid(row=5, column=0)

    power = Button(frame, text='**', height=3, width=6, font=35, fg='black', bg='white',
                   command=lambda: button_press('**'))
    power.grid(row=5, column=2)

    clear = Button(frame, text='clear', font=('Arial', 30, 'bold'),
                   fg='red', bg='#42f5e3',
                   command=clear)
    clear.grid(row=6, column=0, columnspan=5)

    window.mainloop()
