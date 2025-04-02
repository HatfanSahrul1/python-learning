import numpy as np
import pandas as pd

data = {
    "Nama" : ["Hatfan", "Sahrul", "Ramadhan"],
    "Matematika" : [3.5, 3.8, 3.1],
    "Fisika" : [3.1, 4.0, 3.7],
    "Listrik" : [3.5, 2.7, 3.5]
}

df = pd.DataFrame(data)
df["Rerata Siswa"] = df.iloc[:, 1:].mean(axis=1)

rerata_kelas = df.iloc[:, 1:].mean(axis=0)
rerata_kelas["Nama"] = "Rerata Kelas"
df = pd.concat([df, pd.DataFrame([rerata_kelas])], ignore_index=True)

print("Data\n", df)
# print("\nkelas\n", rerata_kelas)