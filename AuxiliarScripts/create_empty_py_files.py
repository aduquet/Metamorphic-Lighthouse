import pandas as pd
import numpy as np
import glob as gl
import pathlib
import time
import json
import sys
import os


info_file = pd.read_csv('infoFile/info_groups.csv', index_col=0)

groupList = list(set(info_file['groupID']))


print(groupList)
    