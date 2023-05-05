import tkinter
window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=50, height=30)
window.config(padx=20, pady=20)

equal = tkinter.Label(text="is equal to")
equal.grid(column=0, row=1)
miles = tkinter.Label(text="Miles")
miles.grid(column=2, row=0)
km = tkinter.Label(text="Km")
km.grid(column=2, row=1)

input = tkinter.Entry(width=10)
input.grid(column=1, row=0)

km_value = tkinter.Label(text="0")
km_value.grid(column=1, row=1)


def button_clicked():
    new_km = input.get()
    km = int(new_km) * 1.609344
    km_value.config(text=f"{km:.1f}")


button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()