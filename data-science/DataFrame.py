import numpy as np
import pandas as pd

data = {
    "Nama" : ["Hatfan", "Sahrul", "Ramadhan"],
    "Matematika" : [3.5, 3.8, 3.1],
    "Fisika" : [3.1, 4.0, 3.7],
    "Listrik" : [3.5, 2.7, 3.5]
}

df = pd.DataFrame(data)

print("Data\n", df)