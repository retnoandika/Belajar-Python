# 51 Membuat Module

# cara lain mengambil module
from matematika import tambah,kali,pangkat # tidal perlu menambahkan nama modulenya lagi

# from matematika import * # tanda * akan mengambil semua isi module

hasil_tambah = tambah(1,2,3,4)
print(f'hasil tambah = {hasil_tambah}')

hasil_kali = kali(1,2,3,4)
print(f'hasil kali   = {hasil_kali}')

pangkat_3 = pangkat(2)
print(f"hasil pangkat3 = {pangkat_3(3)}")