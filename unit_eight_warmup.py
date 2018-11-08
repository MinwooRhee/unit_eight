import tkinter

root = tkinter.Tk()

fahrenheit = tkinter.StringVar()
celsius = tkinter.StringVar()

root.title("tempconverter")

f_label = tkinter.Label(root, text="degrees F:")
f_label.grid(row=1, column=1)

f_entry = tkinter.Entry(root, textvariable=fahrenheit)
f_entry.grid(row=1, column=2)

c_label = tkinter.Label(root, text="degrees C:")
c_label.grid(row=2, column=1)

c_temp_label = tkinter.Label(root, textvariable=celsius)
c_temp_label.grid(row=2, column=2)

root.mainloop()
