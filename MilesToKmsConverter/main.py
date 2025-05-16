from tkinter import *

def calculate():
    miles = float(miles_input.get())
    km = round(miles * 1.60934)
    answer.config(text=f"{km}")

window = Tk()
window.title("Miles to Kms converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.insert(0, "0")
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

answer = Label(text="0")
answer.grid(column=1, row=1)

kilometer_label = Label(text="Kms")
kilometer_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)





window.mainloop()