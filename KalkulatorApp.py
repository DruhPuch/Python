from tkinter import *

count = 0

#def click():
  #  global count
  #  count += 1
  #  label.config(text=count)
  #  label2.pack()

window = Tk()
button1 = Button(window, text="1")
button2 = Button(window, text="2")
button3 = Button(window, text="3")
button4 = Button(window, text="4")
button5 = Button(window, text="5")
button6 = Button(window, text="6")
button7 = Button(window, text="7")
button8 = Button(window, text="8")
button9 = Button(window, text="9")
button0 = Button(window, text="0")
buttonC = Button(window, text="C")
buttonZnak1 = Button(window, text="+")
buttonZnak2 = Button(window, text="- ")
buttonZnak3 = Button(window, text="* ")
buttonZnak4 = Button(window, text="/")
buttonZnak5 = Button(window, text="=")

button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=0, column=2)
buttonZnak1.grid(row=0, column=3)
button4.grid(row=1, column=0)
button5.grid(row=1, column=1)
button6.grid(row=1, column=2)
buttonZnak2.grid(row=1, column=3)
button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)
buttonZnak3.grid(row=2, column=3)


buttonZnak4.grid(row=4, column=3)
#button.config(command=click)
#button.config(font=('Ink Free',50,'bold'))
#button.config(bg='#D92020')
#button.config(fg='purple')
#button.config(activebackground='yellow')
#button.config(activeforeground='purple')
#image = PhotoImage(file='Lymhurst.png')
#button.config(image=image)
#button.config(compound='bottom')
#button.config(state="active") #disabled
#label = Label(window, text=count)
#label.config(font=('Manospace',50))
#label.pack()
#button.pack()
#label2 = Label(window, image=image)
window.mainloop()
