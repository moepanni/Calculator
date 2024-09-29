from tkinter import Tk, END, Entry, N, E, S, W, Button
from tkinter import font
from tkinter import Label
from functools import partial


def get_input(entry, argu):
    """Insert the argument into the entry widget."""
    entry.insert(END, argu)


def backspace(entry):
    """Remove the last character from the entry widget."""
    input_len = len(entry.get())
    if input_len > 0:
        entry.delete(input_len - 1)


def clear(entry):
    """Clear the entry widget."""
    entry.delete(0, END)


def calc_expression(expression):
    """Calculate the mathematical expression passed as a string."""
    try:
        return str(eval(expression.strip()))
    except ZeroDivisionError:
        return "Error: Divide by 0"
    except Exception:
        return "Error"


def calc(entry):
    """Evaluate the expression in the entry widget and display the result."""
    input_info = entry.get()
    output = calc_expression(input_info)
    clear(entry)
    entry.insert(END, output)


def popupmsg(message):
    """Display an error message in a popup window."""
    popup = Tk()
    popup.resizable(0, 0)
    popup.geometry("200x100")
    popup.title("Alert")
    popup.configure(bg='light blue')  # Set background to light blue

    label = Label(popup, text=message, fg='black', bg='light blue')
    label.pack(side="top", fill="x", pady=10)

    B1 = Button(popup, text="Okay", bg="#0000FF", fg='black', command=popup.destroy)
    B1.pack()

    popup.mainloop()


def cal():
    """Main function to run the calculator GUI."""
    root = Tk()
    root.title("Calculator")
    root.resizable(0, 0)
    root.configure(bg='light blue')  # Set background to light blue

    entry_font = font.Font(size=15)
    entry = Entry(root, justify="right", font=entry_font)
    entry.grid(row=0, column=0, columnspan=4,
               sticky=N + W + S + E, padx=5, pady=5)

    cal_button_bg = '#0000FF'    # Blue
    num_button_bg = '#FFFFFF'    # White
    other_button_bg = '#FFFFFF'  # White
    text_fg = '#000000'          # Black text
    button_active_bg = '#ADD8E6' # Light blue when active

    num_button = partial(Button, root, fg=text_fg, bg=num_button_bg,
                         padx=10, pady=3, activebackground=button_active_bg)
    cal_button = partial(Button, root, fg=text_fg, bg=cal_button_bg,
                         padx=10, pady=3, activebackground=button_active_bg)

    # Row 1 Buttons
    button_backspace = Button(root, text='<-', bg=other_button_bg, fg=text_fg,
                              padx=10, pady=3, command=lambda: backspace(entry),
                              activebackground=button_active_bg)
    button_backspace.grid(row=1, column=0, columnspan=2, padx=3, pady=5, sticky=N + S + E + W)

    button_clear = Button(root, text='C', bg=other_button_bg, fg=text_fg,
                          padx=10, pady=3, command=lambda: clear(entry),
                          activebackground=button_active_bg)
    button_clear.grid(row=1, column=2, pady=5)

    button_divide = cal_button(text='/', command=lambda: get_input(entry, '/'))
    button_divide.grid(row=1, column=3, pady=5)

    # Row 2 Buttons
    button7 = num_button(text='7', command=lambda: get_input(entry, '7'))
    button7.grid(row=2, column=0, pady=5)

    button8 = num_button(text='8', command=lambda: get_input(entry, '8'))
    button8.grid(row=2, column=1, pady=5)

    button9 = num_button(text='9', command=lambda: get_input(entry, '9'))
    button9.grid(row=2, column=2, pady=5)

    button_multiply = cal_button(text='*', command=lambda: get_input(entry, '*'))
    button_multiply.grid(row=2, column=3, pady=5)

    # Row 3 Buttons
    button4 = num_button(text='4', command=lambda: get_input(entry, '4'))
    button4.grid(row=3, column=0, pady=5)

    button5 = num_button(text='5', command=lambda: get_input(entry, '5'))
    button5.grid(row=3, column=1, pady=5)

    button6 = num_button(text='6', command=lambda: get_input(entry, '6'))
    button6.grid(row=3, column=2, pady=5)

    button_subtract = cal_button(text='-', command=lambda: get_input(entry, '-'))
    button_subtract.grid(row=3, column=3, pady=5)

    # Row 4 Buttons
    button1 = num_button(text='1', command=lambda: get_input(entry, '1'))
    button1.grid(row=4, column=0, pady=5)

    button2 = num_button(text='2', command=lambda: get_input(entry, '2'))
    button2.grid(row=4, column=1, pady=5)

    button3 = num_button(text='3', command=lambda: get_input(entry, '3'))
    button3.grid(row=4, column=2, pady=5)

    button_add = cal_button(text='+', command=lambda: get_input(entry, '+'))
    button_add.grid(row=4, column=3, pady=5)

    # Row 5 Buttons
    button0 = num_button(text='0', command=lambda: get_input(entry, '0'))
    button0.grid(row=5, column=0, pady=5)

    button_decimal = num_button(text='.', command=lambda: get_input(entry, '.'))
    button_decimal.grid(row=5, column=1, pady=5)

    button_power = cal_button(text='^', command=lambda: get_input(entry, '**'))
    button_power.grid(row=5, column=2, pady=5)

    button_equals = cal_button(text='=', command=lambda: calc(entry))
    button_equals.grid(row=5, column=3, pady=5)

    # Exit Button
    exit_button = Button(root, text='Quit', fg='black', bg='black',
                         command=root.quit, height=1, width=7)
    exit_button.grid(row=6, column=1, columnspan=2, pady=5)

    root.mainloop()


def main():
    """Main function to initialize the calculator."""
    cal()


if __name__ == '__main__':
    main()
