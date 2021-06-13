import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from Scripts.config import *
from Library.lib import *


def pt_country_status_mission(df):  # вроде бы оно работает, погоняй
    '''Функция создает сводную таблицу
    Автор: Тарасенко И.'''
    pt1 = pd.pivot_table(df,
                         index=['Country'],
                         values=['Date'],
                         columns=['Status Mission'],
                         aggfunc=[len],
                         fill_value=0)
    return pt1


def pt2(df):
    '''Функция создает сводную таблицу
        Автор: Тарасенко И.'''
    pt2 = pd.pivot_table(df,
                         index=['Year', 'Status Mission'],
                         values=['Date'],
                         columns=['Country'],
                         aggfunc=[len],
                         fill_value=0)
    return pt2


def pt3(df):
    '''Функция создает сводную таблицу
        Автор: Тарасенко И.'''
    pt3 = pd.pivot_table(df,
                         index=['Year'],
                         values=['Date'],
                         columns=[' Rocket'],
                         aggfunc=[len],
                         fill_value=0)
    return pt3


def outcomesForRussia(df):
    '''Функция создает круговой график, показывающий соотношение
    успешных запусков к неуспешным для России, на основе сводной таблицы
    Автор: Маркова Э.'''
    #name = 'outcomesForRussia.png' # !!!!!!потом надо сделать так, чтобы имя пользователь вводил!!!!!!!!!
    labels = 'Faliure', 'Partial faliure', 'Success'
    sizes = [62, 30, 1303]
    explode = (0.5, 0.5, 0.5)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels = labels, autopct='%1.1f%%',
        shadow=False, radius=20, startangle=90)
    ax1.legend(title = 'Outcomes for Russia:')
    ax1.axis('equal')
    plt.show()
    fig1.savefig('Graphics/outcomesForRussia.png')

def year_success(df):
    '''Функция строит категоризированную диаграмму зависимости успешных
    запусков от года
    Автор: Маркова Э.'''
    #year = (1962, 1963, 1964, 1965, 1966, 1967, 1968,
         #1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978)
    #number = [7, 4, 7, 7, 13, 33, 37, 40, 52, 54, 52, 64, 56, 64, 63, 71, 60]
    #year = ([1963, 1962, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1972, 1973, 1976, 1978, 1976, 1973, 1975, 1977])
    #number = [4, 7, 7, 13, 33, 37, 40, 52, 54, 56, 60, 63, 64, 71, 80, 85, 85]
    year = (1962, 1963, 1964, 1965, 1966, 1967, 1968,
            1969, 1970, 1971, 1972, 1973, 1974, 1975)
    number = [4, 7, 7, 13, 33, 37, 40, 52, 54, 56, 60, 63, 64, 71]

    plt.bar(year, number, align='center')  # A bar chart
    plt.xlabel('Year')
    plt.ylabel('Number')
    plt.savefig('Graphics/year_success.png')
    plt.show()

space_missions = reading(PWD)
to_3nf(space_missions)
space_missions.info()

pt1 = pt_country_status_mission(space_missions)  # страна / статус миссий
pt2 = pt2(space_missions)  # страна - статус миссий / год
pt3 = pt3(space_missions)  # год - стоимость в очень странном виде

export_to_csv(space_missions, 'space_missions')  # !!!!!!!переделать на кнопку в UI!!!!
export_to_csv(pt1, "Сводная таблица 1")
export_to_csv(pt2, "Сводная таблица 2")
export_to_csv(pt3, "Сводная таблица 3")
#outcomesForRussia(space_missions)
year_success(space_missions)