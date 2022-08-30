## GLobal dan local scope

from glob import glob
from re import I


nama_global = 'Retno' # <- ini variabel global

# akses variabel global dalam fungsi
def fungsi():
    print(f"fungsi menampilkan {nama_global}")

fungsi()

# akses variabel global dalam loop
for i in range(0,5):
    print(f"loop {i} - {nama_global}")

# percabangan 
if True:
    print(f"if menampilkan {nama_global}")

## Variabel Local Scope

def fungsi2():
    nama_local = "Ucup" # <- variabel local scope

fungsi2()
# print(nama_local) # tidak bisa dilakukan

## Contoh 1: penggunaan akses variabel
nama = "Dika"
def say_dika():
    print(f"Hello {nama}")

say_dika()

## Contoh 2: merubah variabel global
angka = 0
nama = "Yusuf"

def ubah(angka_baru,nama_baru):
    global angka
    global nama
    angka = angka_baru
    nama = nama_baru

print(f"Sebelum {angka,nama}")
ubah(15,"Mahardika")
print(f"Setelah {angka,nama}")

## Contoh 3
angka = 0 

for i in range(0,5):
    angka += i
    angka_dummy = 0

print(angka)
print(angka_dummy)

if True:
    angaka = 10
    angka_dummy = 10

print(angka)
print(angka_dummy)



