from tkinter import *
from tkinter import messagebox
import re

def click_handler(callback):
    def click():
        if message.get() == '':
            messagebox.showinfo("Будь внимательнее!", 'Введи сперва рост!')
        elif str(re.fullmatch(r'[^0][0-9]{2,3}', message.get())) == 'None':
            messagebox.showinfo("Будь внимательнее!", 'Должно быть минимум две цифры и не должно быть букв!!!!')
        else:
            callback()
    return click

def show_message_beer():
    messagebox.showinfo("Маринин рост", str(int(message.get()) / 26) + ' бутылок пива')
def show_message():
    messagebox.showinfo("Маринин рост", message.get() + ' см')
def show_message_dove():
    messagebox.showinfo("Маринин рост", str(int(message.get()) / 35) + ' голубей')
def show_message_sigi():
    messagebox.showinfo("Маринин рост", str(int(message.get()) / 8.4) + ' сигарет')
def show_message_marina():
    messagebox.showinfo("Маринин рост", str(int(message.get()) / 157) + ' Мариш')
window = Tk()
window.title("Маринин рост!")

label1=Label(window,text='Марина, введи свой рост в сантиметрах',width=45,height=6,bg='white',fg='black',font='arial 12')
label1.pack()

message = StringVar()

text1 = Entry(textvariable=message)
text1.place(relx=.5, rely=.1, anchor="c")

button1 = Button(window, bg="grey", text=u"Посчитать рост в бутылках пива!", command=click_handler(show_message_beer))
button1.pack()
button2 = Button(window, bg="grey", text=u"Посчитать рост!", command=click_handler(show_message))
button2.pack()
button3 = Button(window, bg="grey", text=u"Посчитать рост в голубях", command=click_handler(show_message_dove))
button3.pack()
button4 = Button(window, bg="grey", text=u"Посчитать рост в сигах", command=click_handler(show_message_sigi))
button4.pack()
button5 = Button(window, bg="grey", text=u"Посчитать рост в Маринах", command=click_handler(show_message_marina))
button5.pack()


window.mainloop()
