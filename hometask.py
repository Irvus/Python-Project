"""
Created on Fri Jun 4 02:25:13 2021

@author: ilia
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

space_missions = pd.read_csv("Space_Corrected.csv")

space_missions['Year'] = space_missions['Datum'].apply(lambda x: int(str(x).split()[3]))  # выцепляю интовый год
space_missions['Month'] = space_missions['Datum'].apply(lambda x: str(x).split()[1])  # выцепляю месяц
space_missions['Country'] = space_missions['Location'].apply(lambda x: str(x).split()[-1])  # заполняю страны как есть

for i in range(space_missions.shape[0]):  # Make USSR Great Again!
    if space_missions.at[i, 'Year'] <= 1991 and (space_missions.at[i, 'Country'] == 'Russia' or
                                                 space_missions.at[i, 'Country'] == 'Kazakhstan'):
        space_missions.at[i, 'Country'] = 'USSR'

space_missions = space_missions.drop(space_missions.columns[[0]], axis=1)  # Выпиливаю повторяющуюся нумерацию
space_missions.columns.values[0] = 'Numbers'  # Именую столбец с нумерацией
space_missions.info()

pt1 = pd.pivot_table(space_missions,
                     index=['Country'],
                     values=['Status Mission'],
                     columns=['Status Mission'],
                     aggfunc=[len],
                     fill_value=0)


plt.figure(figsize=(20, 6))
space_missions['Launch Date_year'].value_counts().plot(kind='bar')
plt.xticks(rotation=90)
plt.title('Number of launches per year')
plt.show()

plt.figure(figsize=(10, 6))
space_missions['Landing Outcome'].value_counts().plot(kind='bar')
plt.title('Number of successful/failed landings')
plt.show()

plt.figure(figsize=(10, 6))
space_missions['Customer Country'].value_counts().plot(kind='bar')
plt.title('Distribution by customer countries')
plt.show()

plt.figure(figsize=(10, 6))
space_missions['Launch Site'].value_counts().plot(kind='bar')
plt.title('Distribution by launch sites')
plt.show()
