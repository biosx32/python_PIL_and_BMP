import tkinter
from tkinter import Button

def toggle(btn):

    if btn['fg'] != "black":
        print(btn['fg'])
        btn.configure(bg="red")
    else:
        btn.configure(bg="blue")


window = tkinter.Tk()
window.resizable(width=False, height=False)
window.minsize(width= 1000, height = 500)

a = None
a = Button (window, width=40, height = 20, fg="white", command=toggle(a))

a.place(x=20, y=20)




window.mainloop()





			

