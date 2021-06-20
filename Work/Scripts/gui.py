from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import csv
from tkinter import messagebox
import sys

sys.path.append('../')

from Scripts.main import *
from Scripts.config import *
from Library.lib import *

def main_window():
    """
    Функция создает главное окно приложения
    Входные данные:нет
    Выходные данные:нет
    Автор: Маркова Э.
    """
    window = Tk()
    window.title("Python analysis")
    lbl = Label(text='Чтобы открыть базу данных нажмите кнопку "Базза данных"')
    lbl.place(x=190, y=100)
    btn_graph = Button(window, text="Графики", command=graphs, width=50)
    btn_pt1 = Button(window, text="Скачать сводную таблицу 1", command=save_pt1, width=50)
    btn_pt2 = Button(window, text="Скачать сводную таблицу 2", command=save_pt2, width=50)
    btn_pt3 = Button(window, text="Скачать сводную таблицу 3", command=save_pt3, width=50)
    btn_pt4 = Button(window, text="База данных", command=data_base, width=50)
    btn1 = Button(window, text="Добавить строку", command=insert, width=50)
    btn2 = Button(window, text="Удалить строку", width=50)
    btn3 = Button(window, text="Изменить строку", width=50)
    btn_graph.place(x=180, y=450)
    btn_pt1.place(x=180, y=300)
    btn_pt2.place(x=180, y=350)
    btn_pt3.place(x=180, y=400)
    btn_pt4.place(x=180, y=250)
    btn1.place(x=180, y=500)
    btn2.place(x=180, y=550)
    btn3.place(x=180, y=600)
    window.geometry('700x700')
    window.mainloop()


def graphs():
    """
    Функция создает окно с графиками
    Входные данные:нет
    Выходные данные:нет
    Автор: Маркова Э.
    """
    window = Tk()
    window.title("Graphics")
    lbl = Label(window, text="Графики", font=("Arial Bold", 15))
    lbl.place(x=260, y=5)
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
    lbl3 = Label(window, text='Зависимость стоимости запуска от года (диаграмма рассеивания)')
    lbl3.place(x=120, y=200)
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
    lbl5 = Label(window, text='Зависимость стоимости от года')
    lbl5.place(x=190, y=360)
    btn9 = Button(window, text='Построить', command=show_gr5, width=30)
    btn9.place(x=50, y=385)
    btn10 = Button(window, text='Сохранить', command=save_gr5, width=30)
    btn10.place(x=300, y=385)
    lbl6 = Label(window, text='Зависимость успешных запусков от неуспешных (столбчатая диаграмма)')
    lbl6.place(x=100, y=440)
    btn11 = Button(window, text='Построить', command=show_gr5, width=30)
    btn11.place(x=50, y=465)
    btn12 = Button(window, text='Сохранить', command=save_gr5, width=30)
    btn12.place(x=300, y=465)
    window.geometry('600x600')
    window.mainloop()


def save_pt1():
    """
    Функция сохраняет сводную таблицу 1
    Входные данные:нет
    Выходные данные:нет
    Автор: Маркова Э.
    """
    space_missions = reading(path_to_csv)
    to_3nf(space_missions)
    space_missions.info()
    pt1 = pt_country_status_mission(space_missions)
    save_table(pt1, 'Сводная таблица 1')
    messagebox.showinfo('Сделано!', 'Вы можете открыть сводную таблицу в формате xlsx '
                                    'в папке Output в файле под названием Сводная таблица 1')


def save_pt2():
    """
    Функция сохраняет сводную таблицу 2
    Входные данные:нет
    Выходные данные:нет
    Автор: Маркова Э.
    """
    space_missions = reading(path_to_csv)
    to_3nf(space_missions)
    space_missions.info()
    pt2 = pt_2(space_missions)
    save_table(pt2, 'Сводная таблица 2')
    messagebox.showinfo('Сделано!', 'Вы можете открыть сводную таблицу в формате xlsx '
                                    'в папке Output в файле под названием Сводная таблица 2')


def save_pt3():
    """
    Функция сохраняет сводную таблицу 3
    Входные данные:нет
    Выходные данные:нет
    Автор: Маркова Э.
    """
    space_missions = reading(path_to_csv)
    to_3nf(space_missions)
    space_missions.info()
    pt3 = pt_3(space_missions)
    save_table(pt3, 'Сводная таблица 3')
    messagebox.showinfo('Сделано!', 'Вы можете открыть сводную таблицу в формате xlsx '
                                    'в папке Output в файле под названием Сводная таблица 3')


def save_gr1():
    """
    Функция сохраняет график зависимости успешных запусков от неуспешных
    Входные данные:нет
    Выходные данные:нет
    Автор: Маркова Э.
    """
    outcomes_for_russia('True')
    messagebox.showinfo('Скачано!', 'Вы можете открыть график в папке Graphics '
                                    'в файле под названием Outcomes for Russia.png')


def show_gr1():
    """
    Функция выводит график зависимости успешных запусков от неуспешных
    Входные данные:нет
    Выходные данные:нет
    Автор: Маркова Э.
    """
    outcomes_for_russia('False')


def save_gr2():
    """
    Функция сохраняет график зависимости успешных запусков от года
    Входные данные:нет
    Выходные данные:нет
    Автор: Маркова Э.
    """
    year_success('True')
    messagebox.showinfo('Скачано!', 'Вы можете открыть график в папке Graphics '
                                    'в файле под названием Year and success.png')


def show_gr2():
    """
    Функция выводит график зависимости успешных запусков от года
    Входные данные:нет
    Выходные данные:нет
    Автор: Маркова Э.
    """
    year_success('False')


def save_gr3():
    """
    Функция сохраняет график зависимости средней стоимости запуска от года
    Входные данные:нет
    Выходные данные:нет
    Автор: Маркова Э.
    """
    price_year('True')
    messagebox.showinfo('Скачано!', 'Вы можете открыть график в папке Graphics '
                                    'в файле под названием Price and year.png')


def show_gr3():
    """
    Функция выводит график зависимости средней стоимости запуска от года
    Входные данные:нет
    Выходные данные:нет
    Автор: Маркова Э.
    """
    price_year('False')


def save_gr4():
    """
    Функция сохраняет график зависимости количества запусков от года
    Входные данные:нет
    Выходные данные:нет
    Автор: Маркова Э.
    """
    number_year('True')
    messagebox.showinfo('Скачано!', 'Вы можете открыть график в папке Graphics '
                                    'в файле под названием Launches per year.png')


def show_gr4():
    """
    Функция выводит график зависимости количества запусков от года
    Входные данные:нет
    Выходные данные:нет
    Автор: Маркова Э.
    """
    number_year('False')


def save_gr5():
    """
    Функция скачивает график зависимости цены запусков от года
    Входные данные:нет
    Выходные данные:нет
    Автор: Маркова Э.
    """
    max_min_price('True')
    messagebox.showinfo('Скачано!', 'Вы можете открыть график в папке Graphics '
                                    'в файле под названием Max and min price.png')


def show_gr5():
    """
    Функция выводит график зависимости цены запусков от года
    Входные данные:нет
    Выходные данные:нет
    Автор: Маркова Э.
    """
    max_min_price('False')


def data_base():
    """
    Функция выводит таблицу
    Входные данные:нет
    Выходные данные:нет
    Автор: Тарасенко И.
    """
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


def insert():
    """
    Функция вставляет новую строку в базу данных
    Входные данные: нет
    Выходные данные: нет
    Автор: Маркова Э.
    """
    def clicked():
        space_missions = reading(path_to_csv)
        to_3nf(space_missions)
        company_name = txt1.get()
        detail = txt2.get()
        status_rocket = txt3.get()
        rocket = txt4.get()
        status_mission = txt5.get()
        year = txt6.get()
        month = txt7.get()
        dow = txt8.get()
        date = txt9.get()
        time_in_min = txt10.get()
        country = txt11.get()
        insert_row(space_missions, company_name, detail, status_rocket, rocket, status_mission, year, month, dow, date,
                   time_in_min, country)
    window = Tk()
    window.title("Insert")
    lbl = Label(window, text="Рекомендуется вводить данные на английском языке и в соответствии"
                             " со следующими советами.")
    lbl1 = Label(window, text="Status Rocket вводится как либо StatusActive, либо StatusRetired.")
    lbl2 = Label(window, text="Rocket представляет собой число типа float.")
    lbl3 = Label(window, text="Status Mission вводится как либо Success, либо Failure, "
                              "либо Partial Failure, либо Prelaunch Failure.")
    lbl4 = Label(window, text="Месяц рекомендуется вводить в формате Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, "
                              "Oct, Nov, Dec.")
    lbl.place(x=10, y=10)
    lbl1.place(x=10, y=30)
    lbl2.place(x=10, y=50)
    lbl3.place(x=10, y=70)
    lbl4.place(x=10, y=90)
    lbl_info1 = Label(window, text="Company Name")
    lbl_info2 = Label(window, text="Detail")
    lbl_info3 = Label(window, text="Status Rocket")
    lbl_info4 = Label(window, text="Rocket")
    lbl_info5 = Label(window, text="Status Mission")
    lbl_info6 = Label(window, text="Year")
    lbl_info7 = Label(window, text="Month")
    lbl_info8 = Label(window, text="Day of Week")
    lbl_info9 = Label(window, text="Date")
    lbl_info10 = Label(window, text="Time in Min")
    lbl_info11 = Label(window, text="Country")
    txt1 = Entry(window, width=50)
    txt2 = Entry(window, width=50)
    txt3 = Entry(window, width=50)
    txt4 = Entry(window, width=50)
    txt5 = Entry(window, width=50)
    txt6 = Entry(window, width=50)
    txt7 = Entry(window, width=50)
    txt8 = Entry(window, width=50)
    txt9 = Entry(window, width=50)
    txt10 = Entry(window, width=50)
    txt11 = Entry(window, width=50)
    lbl_info1.place(x=10, y=130)
    txt1.place(x=110, y=130)
    lbl_info2.place(x=10, y=160)
    txt2.place(x=110, y=160)
    lbl_info3.place(x=10, y=190)
    txt3.place(x=110, y=190)
    lbl_info4.place(x=10, y=220)
    txt4.place(x=110, y=220)
    lbl_info5.place(x=10, y=250)
    txt5.place(x=110, y=250)
    lbl_info6.place(x=10, y=280)
    txt6.place(x=110, y=280)
    lbl_info7.place(x=10, y=310)
    txt7.place(x=110, y=310)
    lbl_info8.place(x=10, y=340)
    txt8.place(x=110, y=340)
    lbl_info9.place(x=10, y=370)
    txt9.place(x=110, y=370)
    lbl_info10.place(x=10, y=400)
    txt10.place(x=110, y=400)
    lbl_info11.place(x=10, y=430)
    txt11.place(x=110, y=430)
    btn = Button(window, text="Сохранить", command=clicked, width=50)
    btn.place(x=100, y=490)
    window.geometry('600x600')
    window.mainloop()
