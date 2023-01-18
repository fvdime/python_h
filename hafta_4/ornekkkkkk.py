import tkinter

win = tkinter.Tk()

win.attributes('-alpha', 0.0)
win.iconify()

window = tkinter.Toplevel(win)
window.geometry("500x500+100+100")
window.overrideredirect(1)

photo = tkinter.PhotoImage(file="test.png")

label = tkinter.Label(window, image=photo)
label.pack()

win.mainloop()