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
    btn1.place(x = 50, y = 60)
    btn2 = Button(window, text = 'Сохранить', command = save_gr1, width = 30)
    window.geometry('600x500')
    window.mainloop()

def save_pt1():
    pt1 = pt_country_status_mission(space_missions)  # страна / статус миссий
    save_table(pt1, 'Сводная таблица 1')
    messagebox.showinfo('Сделано!', 'Вы можете открыть сводную таблицу в формате xlsx в папке Output')

def save_gr1():
    year_success(space_missions, 'True')

def show_gr1():
    year_success(space_missions, 'False')

mainWindow()
