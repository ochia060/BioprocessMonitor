# test stuff i have no idea how to do this

import os

import numpy as np
import pandas as pd

LINE_BREAK = "\n"+500*"="+"\n"

path_import=os.path.join("PyCharm","class things", "assignment 1", "dataset_fermentation.csv")

print(f"*Dataset path: {path_import}")


df=pd.read_csv(path_import)
print(df)