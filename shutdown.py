#!/usr/bin/python3
import subprocess
from tkinter import *
from tkinter import messagebox
import re

def shutdown_time():
    shutdown_cmd = "shutdown"
    shutdown_cmd_arg = "-h"
    if message.get() == '':
        messagebox.showinfo("Будь внимательнее!", 'Введи время!')
    elif str(re.fullmatch(r'^([01]\d|2[0-3]):([0-5]\d)$', str(message.get()))) == 'None':
        messagebox.showinfo("Будь внимательнее!", 'Проверь введенное время на корректность! Формат таков:\n XX:YY')
    else:
        subprocess.call([shutdown_cmd, shutdown_cmd_arg, str(message.get())])
        messagebox.showinfo("Выключение ПК",'Компьютер будет выключен в ' + str(message.get()))
        window.destroy()

def shutdown_cancel():
    shutdown_cmd = "shutdown"
    shutdown_cmd_arg = "-c"
    subprocess.call([shutdown_cmd,shutdown_cmd_arg])
    messagebox.showinfo("Отмена выключения", 'Автоматическое выключение компьютера отменено')
    window.destroy()

window = Tk()
window.title("Linux Shutdowner")

text1 = Label(text="В какое время выключить ПК?")
text1.pack()

message = Entry()
message.pack()

button1 = Button(window, bg="grey", text=u"Выключить пк в заданное время!", command=shutdown_time)
button1.pack()
button2 = Button(window, bg="grey", text=u"Отменить выключение пк", command=shutdown_cancel)
button2.pack()

window = mainloop()

