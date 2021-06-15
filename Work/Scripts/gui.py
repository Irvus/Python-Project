from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import csv
from tkinter import messagebox
import sys

sys.path.append('../')

from Scripts.main import *
from Scripts.config import *


# from Scripts.run import *

def main_window():
    '''Функция создает главное окно приложения
    Входные данные:нет
    Выходные данные:нет
    Автор: Маркова Э.'''
    window = Tk()
    window.title("Python analysis")
    btn_graph = Button(window, text="Графики", command=graphs, width=50)
    btn_pt1 = Button(window, text="Скачать сводную таблицу 1", command=save_pt1, width=50)
    btn_pt2 = Button(window, text="Скачать сводную таблицу 2", command=save_pt2, width=50)
    btn_pt3 = Button(window, text="Скачать сводную таблицу 3", command=save_pt3, width=50)
    btn_pt4 = Button(window, text="База данных", command=data_base, width=50)
    btn_graph.place(x=180, y=250)
    btn_pt1.place(x=180, y=300)
    btn_pt2.place(x=180, y=350)
    btn_pt3.place(x=180, y=400)
    btn_pt4.place(x=180, y=450)
    window.geometry('700x600')
    window.mainloop()


def graphs():
    '''Функция создает окно с графиками
    Входные данные:нет
    Выходные данные:нет
    Автор: Маркова Э.'''
    window = Tk()
    window.title("Graphics")
    lbl = Label(window, text="Графики", font=("Arial Bold", 15))
    lbl.place(x=260, y=5)
    # combo_left = Combobox(window)
    # combo_right = Combobox(window)
    # combo_left['values'] = ('Успешные запуски', 'Стоимость', 'Количество запусков')
    # combo_right['values'] = ('Неуспешные запуски', 'Год')
    # combo_left.place(x= 125, y = 40)
    # combo_right.place(x=300, y=40)
    # btn = Button(window, text='Построить', width=30)
    lbl1 = Label(window, text='Зависимость успешных запусков от неуспешных')
    lbl1.place(x=150, y=40)
    btn1 = Button(window, text='Построить', command=show_gr1, width=30)
    btn1.place(x=50, y=65)
    btn2 = Button(window, text='Сохранить', command=save_gr1, width=30)
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
    '''Функция сохраняет сводную таблицу 1
    Входные данные:нет
    Выходные данные:нет
    Автор: Маркова Э.'''
    space_missions = reading(path_to_csv)
    to_3nf(space_missions)
    space_missions.info()
    pt1 = pt_country_status_mission(space_missions)
    save_table(pt1, 'Сводная таблица 1')
    messagebox.showinfo('Сделано!', 'Вы можете открыть сводную таблицу в формате xlsx '
                                    'в папке Output в файле под названием Сводная таблица 1')


def save_pt2():
    '''Функция сохраняет сводную таблицу 2
    Входные данные:нет
    Выходные данные:нет
    Автор: Маркова Э.'''
    space_missions = reading(path_to_csv)
    to_3nf(space_missions)
    space_missions.info()
    pt2 = pt_2(space_missions)
    save_table(pt2, 'Сводная таблица 2')
    messagebox.showinfo('Сделано!', 'Вы можете открыть сводную таблицу в формате xlsx '
                                    'в папке Output в файле под названием Сводная таблица 2')


def save_pt3():
    '''Функция сохраняет сводную таблицу 3
    Входные данные:нет
    Выходные данные:нет
    Автор: Маркова Э.'''
    space_missions = reading(path_to_csv)
    to_3nf(space_missions)
    space_missions.info()
    pt3 = pt_3(space_missions)
    save_table(pt3, 'Сводная таблица 3')
    messagebox.showinfo('Сделано!', 'Вы можете открыть сводную таблицу в формате xlsx '
                                    'в папке Output в файле под названием Сводная таблица 3')


def save_gr1():
    '''Функция сохраняет график зависимости успешных запусков от неуспешных
    Входные данные:нет
    Выходные данные:нет
    Автор: Маркова Э.'''
    space_missions = reading(path_to_csv)
    outcomesForRussia(space_missions, 'True')
    messagebox.showinfo('Скачано!', 'Вы можете открыть график в папке Graphics '
                                    'в файле под названием Outcomes for Russia.png')


def show_gr1():
    '''Функция выводит график зависимости успешных запусков от неуспешных
    Входные данные:нет
    Выходные данные:нет
    Автор: Маркова Э.'''
    space_missions = reading(path_to_csv)
    outcomes_for_russia(space_missions, 'False')


def save_gr2():
    '''Функция сохраняет график зависимости успешных запусков от года
        Входные данные:нет
        Выходные данные:нет
        Автор: Маркова Э.'''
    space_missions = reading(path_to_csv)
    year_success(space_missions, 'True')
    messagebox.showinfo('Скачано!', 'Вы можете открыть график в папке Graphics '
                                    'в файле под названием Year and success.png')


def show_gr2():
    '''Функция выводит график зависимости успешных запусков от года
            Входные данные:нет
            Выходные данные:нет
            Автор: Маркова Э.'''
    space_missions = reading(path_to_csv)
    year_success(space_missions, 'False')


def save_gr3():
    '''Функция сохраняет график зависимости средней стоимости запуска от года
    Входные данные:нет
    Выходные данные:нет
    Автор: Маркова Э.'''
    space_missions = reading(path_to_csv)
    price_year(space_missions, 'True')
    messagebox.showinfo('Скачано!', 'Вы можете открыть график в папке Graphics '
                                    'в файле под названием Price and year.png')


def show_gr3():
    '''Функция выводит график зависимости средней стоимости запуска от года
    Входные данные:нет
    Выходные данные:нет
    Автор: Маркова Э.'''
    space_missions = reading(path_to_csv)
    price_year(space_missions, 'False')


def save_gr4():
    '''Функция сохраняет график зависимости количества запусков от года
        Входные данные:нет
        Выходные данные:нет
        Автор: Маркова Э.'''
    number_year('True')
    messagebox.showinfo('Скачано!', 'Вы можете открыть график в папке Graphics '
                                    'в файле под названием Launches per year.png')


def show_gr4():
    '''Функция выводит график зависимости количества запусков от года
    Входные данные:нет
    Выходные данные:нет
    Автор: Маркова Э.'''
    number_year('False')


def data_base():
    '''Функция выводит таблицу
        Входные данные:нет
        Выходные данные:нет
        Автор: Тарасенко И..'''
    df = reading(path_to_new_csv)
    df.drop(df.columns[[0, 1]], axis=1, inplace=True)
    tree = ttk.Treeview()

    df_col = df.columns.values.tolist()
    tree["columns"] = df_col
    counter = len(df)

    for x in range(len(df_col)):
        tree.column(df_col[x], width=100)
        tree.heading(df_col[x], text=df_col[x])

    row_labels = df.index.tolist()

    for i in range(counter):
        tree.insert('', i, text=row_labels[i], values=df.iloc[i, :].tolist())

    ysb = ttk.Scrollbar(orient=tk.VERTICAL, command=tree.yview)
    xsb = ttk.Scrollbar(orient=tk.HORIZONTAL, command=tree.xview)
    tree.configure(yscroll=ysb.set, xscroll=xsb.set)
    ysb.pack(side=tk.RIGHT, fill=tk.Y)
    xsb.pack(side=tk.TOP, fill=tk.X)
    tree.pack()

