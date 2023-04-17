from tkinter import *

window = Tk()

window.title("My first GUI program!")
window.minsize(width=500,height=300)
window.config(padx=20,pady=20)

#Label
my_label = Label(text="I am a label", font=("Arial",24,"bold"))
my_label.grid(row=0,column=0)

my_label["text"] = "New Text"
my_label.config(text="New Text")

def Button_Clicked():
    my_label["text"] = input.get()

button = Button(text="Click Me", command=Button_Clicked)
button.grid(row=1,column=1)

button = Button(text="New Button")
button.grid(row=0,column=3)

input = Entry(width=10)
input.grid(row=2,column=4)


window.mainloop()