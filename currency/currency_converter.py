from tkinter import Tk, ttk
from tkinter import *
import requests
import json

from PIL import Image, ImageTk

white = "#FFFFFF"
dark_gray = "#333333"
red = "#EB5D51"

window = Tk()
window.geometry("300x320")
window.title("Currency Converter")
window.configure(bg=white)
window.resizable(height=FALSE, width=FALSE)

top = Frame(window, width=300, height=60, bg=red)
top.grid(row=0, column=0)

main = Frame(window, width=300, height=260, bg=white)
main.grid(row=1, column=0)

def convert():
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

    currency_1 = combo1.get()
    currency_2 = combo2.get()
    amount = value.get()

    query_string = { "from": currency_1, "to": currency_2, "amount": amount}

    if currency_2 == "CAD":
        symbol = "$"
    elif currency_2 == "USD":
        symbol = "$"
    elif currency_2 == "GBP":
        symbol = "£"
    elif currency_2 == "EUR":
        symbol = "€"
    elif currency_2 == "MXN":
        symbol = "$"
    elif currency_2 == "SEK":
        symbol = "₹"
    elif currency_2 == "INR":
        symbol = "kr"

    headers = {
        "x-rapidapi-host": "currency-converter18.p.rapidapi.com",
        "x-rapidapi-key": "90c59d6c9fmsh4599f814e2ffc92p17fc6djsndeaa0265ac61"
    }

    response = requests.request("GET", url, headers=headers, params=query_string)

    data = json.loads(response.text)
    converted_amount = data["result"]["convertedAmount"]
    formatted = symbol + " {:,.2f}".format(converted_amount)

    result["text"] = formatted

    print(converted_amount, formatted)

icon = Image.open("idk/icons8-convert-52.png")
icon = icon.resize((30, 30))
icon = ImageTk.PhotoImage(icon)
app_name = Label(top, image=icon, compound=LEFT, text="Currency Converter", height=50, padx=10, pady=10, anchor=CENTER, font=("Helvetica 16 bold"), bg=red, fg=white)
app_name.place(x=0, y=0)

result = Label(main, text=" ", width=16, height=2, pady=7, relief="solid", anchor=CENTER, font=("Ivy 15 bold"), bg=white, fg=dark_gray)
result.place(x=50, y=10)

currency = ["CAD", "USD", "GBP", "EUR", "MXN", "SEK", "INR"]

from_label = Label(main, text="From", width=8, height=1, padx=0, pady=0, relief="flat", anchor=NW, font=("Ivy 10"), bg=white, fg=dark_gray)
from_label.place(x=48, y=90)
combo1 = ttk.Combobox(main, width=8, justify=CENTER, font=("Ivy 12 bold"))
combo1["values"] = (currency)
combo1.place(x=50, y=115)

to_label = Label(main, text="To", width=8, height=1, padx=0, pady=0, relief="flat", anchor=NW, font=("Ivy 10"), bg=white, fg=dark_gray)
to_label.place(x=158, y=90)
combo2 = ttk.Combobox(main, width=8, justify=CENTER, font=("Ivy 12 bold"))
combo2["values"] = (currency)
combo2.place(x=160, y=115)

value = Entry(main, width=22, justify=CENTER, font=("Ivy 12 bold"), relief="solid")
value.place(x=50, y=155)

button = Button(main, text="Converter", width=19, padx=5, height=1, bg=red, fg=white, anchor=CENTER, font=("Ivy 12 bold"), command=convert)
button.place(x=15, y=210)

window.mainloop()