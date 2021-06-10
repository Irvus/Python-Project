import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from Scripts.config import *
from Library.lib import *


space_missions = reading(PWD)
to_3nf(space_missions)
space_missions.info()

export_to_csv(space_missions, 'space_missions')


