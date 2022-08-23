# Date and Time

import datetime as dt

hari_ini = dt.date.today()
print(hari_ini)
print(f"Hari ini adalah hari = {hari_ini:%A}") # %A = hari

tanggal = dt.date(2001,4,15)
print(tanggal)
print(f"Hari ini adalah hari = {tanggal:%A}")









