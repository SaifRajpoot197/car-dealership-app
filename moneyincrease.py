money = 7000

import tkinter as tk

window = tk.Tk()
window.title("Money")
window.geometry("800x500")

label=tk.Label(window,text="Money:7000",font=("Arial",30))
label.pack(pady=50,padx=25)

label2=tk.Label(window,text="Car : 5000",font=("Arial",30))
label2.pack(pady=50,padx=25)

entry = tk.Entry(window, font=("Arial", 20))
entry.pack()

def add_custom_money():
    global money
    amount = int(entry.get())  
    label.config(text="Money: " + str(money))

def add_money():
    global money
    money +=1000
    label.config(text="Money:"+str(money))

def spend_money():
    global money
    money -= 1000
    label.config(text="Money:"+str(money))

def buy_car():
    global money
    if money >= 5000: 
        money -= 5000
        label.config(text="Money: " + str(money))
        label2.config(text="Car purchased!")
    else: 
        label2.config(text="Not enough Money")

def sell_car():
    global money
    money = money + 4000  
    label.config(text="Money: " + str(money))
    label2.config(text="Car: Sold!")


button = tk.Button(window,text="Add Money",bg="green",fg="White",command=add_money,)
button.pack()

button2=tk.Button(window,text="Spend Money",bg="Red",fg="White",command=spend_money)
button2.pack()

button3= tk.Button(window,text="Buy Car",bg="Black",fg="white",command=buy_car)
button3.pack()

button4 = tk.Button(window,text="Sale Car",bg="Blue",fg="white",command=sell_car)
button4.pack()

button5 = tk.Button(window, text="Money Added", command=add_custom_money)
button5.pack()

window.mainloop()