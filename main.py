from tkinter import *
from tkinter.ttk import *
from time import strftime
tk=Tk()
tk.title('Arafat-Clock')
tk.iconbitmap('icon.ico')
def time():
    text=strftime("%I:%M:%S %p")
    label.config(text=text)
    label.after(1000, time)

label = Label(tk, font=("Comic Sans MS", 40, 'bold'), background='black', foreground='deeppink3')
label.pack(anchor='center')
time()
mainloop()