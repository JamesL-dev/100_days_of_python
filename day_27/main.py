#################################################################
#
# Miles to kilometers app
#
#################################################################

import tkinter

def miles_to_km(miles):
    km = round(int(miles) * 1.60934)
    return km


def button_clicked():
    new_text = miles_to_km(input.get())
    result_label.config(text=f"{new_text}")


window = tkinter.Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

input = tkinter.Entry(width=7)
input.grid(column=2, row=1)
miles = tkinter.Label(text="Miles")
miles.grid(column=3, row=1)
equal_to_label = tkinter.Label(text="is equal to")
equal_to_label.grid(column=1, row=2)
km_label = tkinter.Label(text="Km")
km_label.grid(column=3, row=2)
result_label = tkinter.Label(text="0")
result_label.grid(column=2, row=2)



# Button
button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(column=2, row=3)


window.mainloop()

