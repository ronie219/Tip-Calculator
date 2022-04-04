import tkinter as tk
import tkinter.messagebox
from tkinter import *


def calculate():
    try:
        bill = int(billEntry.get().strip())
        percent = int(percentEntry.get().strip())
        people = int(peopleEntry.get().strip())

        billEntry.delete(0, END)
        percentEntry.delete(0, END)
        peopleEntry.delete(0, END)

        order = "Your order is \nBill: $" + str(bill) + "\nTip percent: " + str(percent) + "%\nTotal people: " + str(
            people) + "\nEach person should pay: $" + str(round((bill * percent / 100 + bill) / people, 2))
        tkinter.messagebox.showinfo("Final order", order)

    except ValueError:
        tkinter.messagebox.showinfo("Error", "Either your bill, percent, or people is wrong, please enter only numbers")

        billEntry.delete(0, END)
        percentEntry.delete(0, END)
        peopleEntry.delete(0, END)


window = tk.Tk()
window.title("Tip calculator")

billLabel = tk.Label(text="Enter the bill(no dollars)")
billEntry = tk.Entry()
billLabel.pack()
billEntry.pack()

percentLabel = tk.Label(text="Enter the percent you wish to tip(no percent)")
percentEntry = tk.Entry()
percentLabel.pack()
percentEntry.pack()

peopleLabel = tk.Label(text="Enter the number of people(including yourself)")
peopleEntry = tk.Entry()
peopleLabel.pack()
peopleEntry.pack()

submit = tk.Button(
    text="Calculate tip!",
    width=25,
    height=5,
    bg="white",
    fg="black",
    command=calculate
)
submit.pack()
window.mainloop()