from tkinter import *

window = Tk()
window.minsize(height=150, width = 300)

entry_miles = Entry()
entry_miles.grid(row=1, column=2)

label_miles = Label(text="miles",font=("Arial", 15, "normal"))
label_miles.grid(row=1, column=3)

label_2 = Label(text= 0, font=("Arial", 15, "normal"))
label_2.grid(row=2,column=2)

label_3 = Label(text="is equal to",font=("Arial", 15, "normal"))
label_3.grid(row=2, column=1)

def on_miles():
    label_2.config(text=(int(entry_miles.get())* 1.609344))

label_Km = Label(text="km", font=("Arial", 15, "normal"))
label_Km.grid(row=2, column=3)

button = Button(text="Convert",font=("Arial", 15, "normal"), command=on_miles)
button.grid(row=3,column=2)

window.mainloop()
