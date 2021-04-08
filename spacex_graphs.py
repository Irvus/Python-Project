# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 21:33:13 2021

@author: eveli
"""

import pandas as pd
import matplotlib.pyplot as plt


space_missions = pd.read_csv("database.csv")

space_missions['Year']=space_missions['Launch Date'].apply(lambda x: str(x).split(', ')[-1])
space_missions['Month']=space_missions['Launch Date'].apply(lambda x: str(x).split(', ')[0])
space_missions['Launch Date_year']=space_missions['Launch Date'].apply(lambda x: str('20' + x).split(' ')[2])
space_missions['Launch Date_month']=space_missions['Launch Date'].apply(lambda x: str(x).split(' ')[-2])


plt.figure(figsize=(20,6))
space_missions['Launch Date_year'].value_counts().plot(kind='bar')
plt.xticks(rotation=90)
plt.title('Number of lanches per year')
plt.show()

plt.figure(figsize=(10,6))
space_missions['Landing Outcome'].value_counts().plot(kind='bar')
plt.title('Number of successful/failed landings')
plt.show()

plt.figure(figsize=(10,6))
space_missions['Customer Country'].value_counts().plot(kind='bar')
plt.title('Distribution by customer countries')
plt.show()

plt.figure(figsize=(10,6))
space_missions['Launch Site'].value_counts().plot(kind='bar')
plt.title('Distribution by launch sites')
plt.show()