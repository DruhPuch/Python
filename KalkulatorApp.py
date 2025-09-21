from tkinter import *

window = Tk()
window.title('Kalkulator')
#window.geometry('300x300')
#window.minsize(300, 300)

wynik = 0
x = ''
y = ''
z = 0
warning = 0
error = 'error'
def OnButtonClick(button_id):
        global x, y, z, wynik, warning, error

        if button_id == button_id not in ('C', '+', '-', '=', '/', '*'):
            if z != 0:
                y = str(y) + str(button_id)
            elif z == 0:
                x = str(x) + str(button_id)
        elif button_id == 'C':
            x = ''
            y = ''
            z = 0
            wynik = 0
            warning = 0
            label.config(text=x)
        elif button_id == '+':
            z = 1
        elif button_id == '-':
            z = 2
        elif button_id == '*':
            z = 3
        elif button_id == '/':
            z = 4
        if z == 0 and warning == 0:
            label.config(text=x)
        elif z != 0 and warning == 0:
            label.config(text=y)
        if button_id == '=':
            if z == 1:
                warning = 1
                wynik = int(x)+int(y)
            elif z == 2:
                warning = 1
                wynik = int(x)-int(y)
            elif z == 3:
                warning = 1
                wynik = int(x)*int(y)
            elif z == 4:
                warning = 1
                if y == 0:
                    wynik = str(error)
                else:
                    wynik = int(x)/int(y)
            if warning == 1:
                label.config(text = wynik)


toggle = Checkbutton(text = 'Number 1 is -')
toggle2 = Checkbutton(text = 'Number 2 is -')

label = Label(window, text = x)
label.config(bg='grey', pady = 10)
label2 = Label(window, text = 'Po każdym działaniu nacisnąć C, nie dzielić przez 0 bo crash, pozdro, minusowe liczby też jeszcze nie działają', pady = 10)

button1 = Button(window, text="1", pady=10, padx=10, command=lambda: OnButtonClick(1))
button2 = Button(window, text="2", pady=10, padx=10, command=lambda: OnButtonClick(2))
button3 = Button(window, text="3", pady=10, padx=10, command=lambda: OnButtonClick(3))
button4 = Button(window, text="4", pady=10, padx=10, command=lambda: OnButtonClick(4))
button5 = Button(window, text="5", pady=10, padx=10, command=lambda: OnButtonClick(5))
button6 = Button(window, text="6", pady=10, padx=10, command=lambda: OnButtonClick(6))
button7 = Button(window, text="7", pady=10, padx=10, command=lambda: OnButtonClick(7))
button8 = Button(window, text="8", pady=10, padx=10, command=lambda: OnButtonClick(8))
button9 = Button(window, text="9", pady=10, padx=10, command=lambda: OnButtonClick(9))
button0 = Button(window, text="0", pady=10, padx=10, command=lambda: OnButtonClick(0))
buttonC = Button(window, text="C", pady=10, padx=10, command=lambda: OnButtonClick('C'))
buttonZnak1 = Button(window, text="+", pady=10, padx=10, command=lambda: OnButtonClick('+'))
buttonZnak2 = Button(window, text="-", pady=10, padx=10, command=lambda: OnButtonClick('-'))
buttonZnak3 = Button(window, text="*", pady=10, padx=10, command=lambda: OnButtonClick('*'))
buttonZnak4 = Button(window, text="/", pady=10, padx=10, command=lambda: OnButtonClick('/'))
buttonZnak5 = Button(window, text="=", pady=10, padx=10, command=lambda: OnButtonClick('='))

label2.grid(row=0, columnspan=4, sticky="ew", pady=10)
label.grid(row=1, columnspan=4, sticky="ew", pady = 10)

button1.grid(row=2, column=0, sticky="ew")
button2.grid(row=2, column=1, sticky="ew")
button3.grid(row=2, column=2, sticky="ew")
buttonZnak1.grid(row=2, column=3, sticky="ew")

button4.grid(row=3, column=0, sticky="ew")
button5.grid(row=3, column=1, sticky="ew")
button6.grid(row=3, column=2, sticky="ew")
buttonZnak2.grid(row=3, column=3, sticky="ew")

button7.grid(row=4, column=0, sticky="ew")
button8.grid(row=4, column=1, sticky="ew")
button9.grid(row=4, column=2, sticky="ew")
buttonZnak3.grid(row=4, column=3, sticky="ew")

buttonC.grid(row=5, column=0, sticky="ew")
button0.grid(row=5, column=1, sticky="ew")
buttonZnak5.grid(row=5, column=2, sticky="ew")
buttonZnak4.grid(row=5, column=3, sticky="ew")

toggle.grid(row=6, column=0,columnspan=2, sticky="ew")
toggle2.grid(row=6, column=2, columnspan=2, sticky="ew")

window.mainloop()

#count = 0

#def click():
  #  global count
  #  count += 1
  #  label.config(text=count)
  #  label2.pack()

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