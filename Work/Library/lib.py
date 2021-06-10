import pandas as pd


def reading(pwd):
    return pd.read_csv(pwd)


def export_to_csv(df, title):
    df.to_csv(path_or_buf=('Data/' + title + '.csv'))


def to_3nf(df):
    df['Year'] = df['Datum'].apply(lambda x: int(str(x).split()[3]))  # выцепляю интовый год
    df['Month'] = df['Datum'].apply(lambda x: str(x).split()[1])  # выцепляю месяц
    df['Day of Week'] = df['Datum'].apply(lambda x: str(x).split()[0])  # выцепляю день недели
    df['Date'] = df['Datum'].apply(lambda x: int(str(x).split()[2].replace(',', '')))  # число
    # df['Time in Min'] = df['Datum'].apply(lambda x: int(str(x).split()[4].split(':')[0]) * 24 +   # НЕ ПАШЕТ ИЗ-ЗА ТОГО, ЧТО НЕ ВЕЗДЕ ЕСТЬ ВРЕМЯ
    #                                                                        int(str(x).split()[4].split(':')[1]))  # Время в минутах
    df.drop('Datum', axis=1, inplace=True)

    df['Country'] = df['Location'].apply(
        lambda x: str(x).split()[-1])  # заполняю страны как есть

    for i in range(df.shape[0]):  # Make USSR Great Again!
        if df.at[i, 'Year'] <= 1991 and (df.at[i, 'Country'] == 'Russia' or df.at[i, 'Country'] == 'Kazakhstan'):
            df.at[i, 'Country'] = 'USSR'

    df.drop(df.columns[[0, 1]], axis=1, inplace=True)  # Выпиливаю повторяющуюся нумерацию

