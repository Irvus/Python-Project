from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import sys
sys.path.append('../')
from Scripts.main import *
from Scripts.config import *
from Scripts.run import *

def mainWindow():
    window = Tk()
    window.title("Python analysis")
    btn_graph = Button(window, text="Графики", command=graphs, width = 30)
    btn_pt1 = Button(window, text="Скачать сводную таблицу 1", command = save_pt1, width = 30)
    btn_graph.place(x=250, y=200)
    btn_pt1.place(x = 250, y = 250)
    window.geometry('700x600')
    window.mainloop()



def graphs():
    window = Tk()
    window.title("Graphics")
    lbl = Label(window, text="Графики", font=("Arial Bold", 15))
    lbl.place(x = 260, y = 5)
    #combo_left = Combobox(window)
    #combo_right = Combobox(window)
    #combo_left['values'] = ('Успешные запуски', 'Стоимость', 'Количество запусков')
    #combo_right['values'] = ('Неуспешные запуски', 'Год')
    #combo_left.place(x= 125, y = 40)
    #combo_right.place(x=300, y=40)
    #btn = Button(window, text='Построить', width=30)
    lbl1 = Label(window, text = 'Зависимость успешных запусков от неуспешных')
    lbl1.place(x=150, y=40)
    btn1 = Button(window, text='Построить', command=show_gr1, width=30)
    btn1.place(x = 50, y = 65)
    btn2 = Button(window, text = 'Сохранить', command = save_gr1, width = 30)
    btn2.place(x=300, y=65)
    lbl2 = Label(window, text='Зависимость успешных запусков от года')
    lbl2.place(x=165, y=120)
    btn3 = Button(window, text='Построить', command=show_gr2, width=30)
    btn3.place(x=50, y=145)
    btn4 = Button(window, text='Сохранить', command=save_gr2, width=30)
    btn4.place(x=300, y=145)
    lbl3 = Label(window, text='Зависимость средней стоимости запуска от года')
    lbl3.place(x=165, y=200)
    btn5 = Button(window, text='Построить', command=show_gr3, width=30)
    btn5.place(x=50, y=225)
    btn6 = Button(window, text='Сохранить', command=save_gr3, width=30)
    btn6.place(x=300, y=225)
    lbl4 = Label(window, text='Зависимость количества запусков от года')
    lbl4.place(x=165, y=280)
    btn7 = Button(window, text='Построить', command=show_gr4, width=30)
    btn7.place(x=50, y=305)
    btn8 = Button(window, text='Сохранить', command=save_gr4, width=30)
    btn8.place(x=300, y=305)
    window.geometry('600x500')
    window.mainloop()

def save_pt1():
    pt1 = pt_country_status_mission(space_missions)  # страна / статус миссий
    save_table(pt1, 'Сводная таблица 1')
    messagebox.showinfo('Сделано!', 'Вы можете открыть сводную таблицу в формате xlsx '
                                    'в папке Output в файле под названием Сводная таблица 1')

def save_gr1():
    outcomesForRussia(space_missions, 'True')
    messagebox.showinfo('Скачано!', 'Вы можете открыть график в папке Graphics '
                                    'в файле под названием Outcomes for Russia.png')

def show_gr1():
    outcomesForRussia(space_missions, 'False')

def save_gr2():
    year_success(space_missions, 'True')
    messagebox.showinfo('Скачано!', 'Вы можете открыть график в папке Graphics '
                                    'в файле под названием Year and success.png')

def show_gr2():
    year_success(space_missions, 'False')

def save_gr3():
    price_year(space_missions, 'True')
    messagebox.showinfo('Скачано!', 'Вы можете открыть график в папке Graphics '
                                    'в файле под названием Price and year.png')

def show_gr3():
    price_year(space_missions, 'False')

def save_gr4():
    number_year('True')
    messagebox.showinfo('Скачано!', 'Вы можете открыть график в папке Graphics '
                                    'в файле под названием Launches per year.png')

def show_gr4():
    number_year('False')


mainWindow()
