import sys

sys.path.append('../')

from Scripts.main import *
from Scripts.config import *
from Scripts.gui import *

space_missions = reading(path_to_csv)
to_3nf(space_missions)
space_missions.info()
main_window()

