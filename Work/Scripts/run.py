import sys
sys.path.append('../')
from Scripts.main import *
from Scripts.config import *
from Scripts.gui import *

space_missions = reading(path_to_csv)
to_3nf(space_missions)
space_missions.info()
mainWindow()
'''
pt1 = pt_country_status_mission(space_missions)
save_table(pt1, 'Сводная таблица 1')
'''

'''
pt1 = pt_country_status_mission(space_missions)  # страна / статус миссий
save_table(pt1, 'Сводная таблица 1')
pt2 = pt2(space_missions)  # страна - статус миссий / год
save_table(pt2, 'Сводная таблица 2')
pt3 = pt3(space_missions)  # год - стоимость в очень странном виде
save_table(pt3, 'Сводная таблица 3')

export_to_csv(space_missions, 'space_missions')  # !!!!!!!переделать на кнопку в UI!!!!
save_table(space_missions, 'space_missions')
outcomesForRussia(space_missions)
price_year(space_missions)
number_year()
'''