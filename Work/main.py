import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from Scripts.config import *
from Library.lib import *


def pt_country_status_mission(df):  # вроде бы оно работает, погоняй
    pt1 = pd.pivot_table(df,
                         index=['Country'],
                         values=['Date'],
                         columns=['Status Mission'],
                         aggfunc=[len],
                         fill_value=0)
    return pt1


def pt2(df):
    pt2 = pd.pivot_table(df,
                         index=['Year', 'Status Mission'],
                         values=['Date'],
                         columns=['Country'],
                         aggfunc=[len],
                         fill_value=0)
    return pt2


space_missions = reading(PWD)
to_3nf(space_missions)
space_missions.info()

pt1 = pt_country_status_mission(space_missions)  # страна / статус миссий
pt2 = pt2(space_missions)  # страна - статус миссий / год


export_to_csv(space_missions, 'space_missions')  # переделать на кнопку в UI


