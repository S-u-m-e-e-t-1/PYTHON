from tkinter import *

root=Tk()
root.geometry("600x600")
root.minsize(90,90)
root.maxsize(900,900)
#sumeet=Label(text="my 1st gui")
#sumeet.pack()
photo=PhotoImage(file="Screenshot2023-07-05115910.png")
sumeet=Label(image=photo)
sumeet.pack()








root.mainloop()

