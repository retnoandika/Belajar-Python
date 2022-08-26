# Date and Time

import datetime as dt

hari_ini = dt.date.today()
print(hari_ini)
print(f"Hari ini adalah hari = {hari_ini:%A}") # %A = hari

tanggal = dt.date(2001,4,15)
print(tanggal)
print(f"Hari ini adalah hari = {tanggal:%A}")

print(5*"="+" Tanggal Lahir "+5*"=")

print("Silahkan masukkan tanggal, \nbulan dan tahun lahir Anda")
tanggal = int(input("Tanggal \t: "))
bulan = int(input("Bulan \t\t: "))
tahun = int(input("Tahun \t\t: "))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"Tanggal lahir Anda adalah : {tanggal_lahir}")
print(f"Harinya adalah : {tanggal_lahir:%A}")

umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365 # days digunakan untuk menghilangkan days nya
umur_bulan_sisa = (umur_hari.days % 365) //30 


print(f"Umur anda adalah: {umur_tahun} tahun, {umur_bulan_sisa} bulan")







