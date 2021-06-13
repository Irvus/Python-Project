import pandas as pd
from Scripts.config import *
import matplotlib.pyplot as plt

def reading(pwd):
    '''Чтение базы данных'''
    return pd.read_csv(pwd)


def export_to_csv(df, title):
    '''Экспорт базы данных'''
    df.to_csv(path_or_buf=('Data/' + title + '.csv'))


def to_3nf(df):
    '''Приведение сводной таблицы к третьей нормальной форме
    Автор: Тарасенко И.'''
    df['Year'] = df['Datum'].apply(lambda x: int(str(x).split()[3]))  # выцепляю интовый год
    df['Month'] = df['Datum'].apply(lambda x: str(x).split()[1])  # выцепляю месяц
    df['Day of Week'] = df['Datum'].apply(lambda x: str(x).split()[0])  # выцепляю день недели
    df['Date'] = df['Datum'].apply(lambda x: int(str(x).split()[2].replace(',', '')))  # число
    df['Time in Min'] = df['Datum'].apply(lambda x: int(int(str(x).split()[4].split(':')[0]) * 60 +
                                                        int(str(x).split()[4].split(':')[1]))
                                                    if (len(str(x).split()) > 4) else None)  # Время в минутах


    df.drop('Datum', axis=1, inplace=True)

    df['Country'] = df['Location'].apply(lambda x: str(x).split(', ')[-1])  # заполняю страны как есть

    df.drop(df.columns[[0, 1]], axis=1, inplace=True)  # Выпиливаю повторяющуюся нумерацию



