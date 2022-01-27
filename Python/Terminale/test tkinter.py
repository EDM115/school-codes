from tkinter import *

window=Tk()



window.title("Test")
window.geometry("1000x500")
window.config(background="grey")


bg = PhotoImage(file = "gris.ppm")
label_image=Label(window, image = bg)
label_image.place(x = 0, y = 0)
'''
frame1 = Frame(window)
frame1.pack(pady = 20 )
'''
label_title=Label(window, text="Salut mon pote !", font=("Courrier", 10), bg='yellow')
label_title.pack(expand=True)




window.mainloop()