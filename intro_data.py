import pandas as pd
import numpy as np

# Membuat DataFrame dari dataset nilai siswa
data = {
    "Nama": ["Ani", "Budi", "Citra", "Dedi", "Eko"],
    "Matematika": [75, 60, 90, 50, 85],
    "Fisika": [80, 55, 85, 45, 90],
    "Kimia": [70, 50, 80, 55, 88],
    "Biologi": [65, 70, 75, 60, 70],
    "Bahasa Inggris": [90, 85, 95, 50, 92]
}

df = pd.DataFrame(data)

# **1. Hitung rata-rata nilai tiap siswa**
df["Rata-rata"] = df.iloc[:, 1:].mean(axis=1)

# **2. Tentukan status (Lulus / Remedial)**
df["Status"] = np.where(df["Rata-rata"] >= 70, "Lulus", "Remedial")

# **3. Tampilkan siswa yang harus remedial**
siswa_remedial = df[df["Status"] == "Remedial"]

# **4. Siswa dengan nilai > 80 di Matematika**
siswa_matematika_80 = df[df["Matematika"] > 80]

# **5. Siswa yang memiliki nilai < 60 di lebih dari 2 mata pelajaran**
df_nilai_only = df.iloc[:, 1:-2]  # Mengambil hanya kolom nilai (tanpa Nama, Rata-rata, Status)
siswa_nilai_kurang_60 = df[df_nilai_only.apply(lambda row: (row < 60).sum(), axis=1) > 2]

# **6. Hitung statistik tiap mata pelajaran**
statistik = df.iloc[:, 1:-2].describe().loc[["mean", "max", "min"]]

# **Menampilkan hasil**
print("DataFrame Nilai Siswa:\n", df)
print("\nSiswa yang harus remedial:\n", siswa_remedial)
print("\nSiswa dengan nilai > 80 di Matematika:\n", siswa_matematika_80)
print("\nSiswa dengan lebih dari 2 nilai < 60:\n", siswa_nilai_kurang_60)
print("\nStatistik Nilai Mata Pelajaran:\n", statistik)
