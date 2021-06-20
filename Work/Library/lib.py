import pandas as pd
import matplotlib.pyplot as plt
import sys

sys.path.append('../')
from Scripts.config import *


def reading(pwd):
    """
    Чтение базы данных
    Входные данные: строка
    Выходные данные: датафрейм
    Автор: Тарасенко И.
    """
    return pd.read_csv(pwd)


def export_to_csv(df, title):
    """
    Входные данные: датафрейм, строка
    Выходные данные: нет
    Автор: Тарасенко И.
    """
    df.to_csv(path_or_buf=(path + '/' + title + '.csv'))

def save_table(table, title):
    """
    Функция сохраняет датафрейм в .xslx
    Входные данные: датафрейм, строка
    Выходные данные: нет
    Автор: Маркова Э.
    """
    table.to_excel(path_out + '/' + title + '.xlsx')

def to_3nf(df):
    """
    Приведение сводной таблицы к третьей нормальной форме
    Входные данные: датафрейм
    Выходные данные: нет
    Автор: Тарасенко И.
    """
    df['Year'] = df['Datum'].apply(lambda x: int(str(x).split()[3]))  # выцепляю интовый год
    df['Month'] = df['Datum'].apply(lambda x: str(x).split()[1])  # выцепляю месяц
    df['Day of Week'] = df['Datum'].apply(lambda x: str(x).split()[0])  # выцепляю день недели
    df['Date'] = df['Datum'].apply(lambda x: int(str(x).split()[2].replace(',', '')))  # число
    df['Time in Min'] = df['Datum'].apply(lambda x: int(int(str(x).split()[4].split(':')[0]) * 60 +
                                                        int(str(x).split()[4].split(':')[1]))
                                                    if (len(str(x).split()) > 4) else None)  # Время в минутах
    df.drop('Datum', axis=1, inplace=True)

    df['Country'] = df['Location'].apply(lambda x: str(x).split(', ')[-1])  # заполняю страны как есть
    df.drop('Location', axis=1, inplace=True)

    df.drop(df.columns[[0, 1]], axis=1, inplace=True)  # Выпиливаю повторяющуюся нумерацию


def insert_row(df, company_name, detail, status_rocket, rocket, status_mission, year, month, dow, date,
               time_in_min, country):
    """
    Добавление строки в базу данных
    Входные данные: датафрейм, строка, строка, строка, целое число, строка, целое число, строка, строка, строка,
                    целое число, целое число, строка
    Выходные данные: датафрейм
    Автор - И. Тарасенко
    """
    df = df.append({'Company Name': company_name,
                    'Detail': detail,
                    'Status Rocket': status_rocket,
                    ' Rocket': rocket,
                    'Status Mission': status_mission,
                    'Year': year,  # TODO: при вводе чисел пользователем проверять формат
                    'Month': month,
                    'Day of Week': dow,
                    'Date': date,
                    'Time in Min': time_in_min,
                    'Country': country},
                   ignore_index=True)
    return df


def remove_row(df, num):
    """
    Удаление строки из датафрейма
    Входные данные: датафрейм, целое число
    Выходные данные: нет
    Автор - И. Тарасенко
    """
    df.drop([num], axis=0, inplace=True)
