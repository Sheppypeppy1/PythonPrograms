from tkinter import *

window = Tk()

window.title("Mile to KM Converter")
window.minsize(width=500,height=300)
window.config(padx=20,pady=20)

input = Entry(width=10)
input.grid(row=0,column=1)

#Label
my_label = Label(text="Miles", font=("Arial",16))
my_label.grid(row=0,column=2)

my_label2 = Label(text="is equal to", font=("Arial",16))
my_label2.grid(row=1,column=0)

my_label3 = Label(text="0", font=("Arial",16))
my_label3.grid(row=1,column=1)

my_label5 = Label(text="km", font=("Arial",16))
my_label5.grid(row=1,column=2)
def Button_Clicked():
    my_label3["text"] = str(int(input.get())*1.609)
    
    

button = Button(text="Calculate", command=Button_Clicked)
button.grid(row=2,column=1)




window.mainloop()