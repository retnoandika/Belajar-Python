import os
from re import U

# Program menghitung luas dan keliling persegi panjang

# Membuat header program
# os.system('cls')
# print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
# print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
# print(f"{'<'*20:<20}{'>'*20:>20}")
# 
# # Mengambil input user
# LEBAR = int(input("Masukkan nilai lebar: "))
# PANJANG = int(input("Masukkan nilai panjang: "))
# 
# # Program menghitung luas
# LUAS = PANJANG*LEBAR
# KELILING = 2*(PANJANG+LEBAR)
# 
# # tampilkan hasil
# print(f"hasil perhitungan luas = {LUAS}")
# print(f"hasil perhitungan keliling = {KELILING}")

def header():
    '''Fungsi Header'''
    os.system('cls')
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'<'*20:<20}{'>'*20:>20}")

def input_user():
    '''Fungsi Input User'''
    # Mengambil input user
    lebar = int(input("Masukkan nilai lebar: "))
    panjang = int(input("Masukkan nilai panjang: "))
    return lebar,panjang

def hitung_luas(lebar,panjang):
    '''Fungsi Luas'''
    return(lebar*panjang)

def hitung_keliling(lebar,panjang):
    '''Fungsi Keliling'''
    return(2*(lebar+panjang))

def display(message,value):
    '''Fungsi Display'''
    print(f"Hasil perhitungan {message} = {value}")

# Program utama

while True:
    header()
    LEBAR,PANJANG = input_user()
    LUAS = hitung_luas(LEBAR,PANJANG)
    KELILING = hitung_keliling(LEBAR,PANJANG)

    display("luas", LUAS)
    display("keliling", KELILING)

    isContinue = input("Apakah lanjut (y/n)? ")
    if isContinue == "n":
        break

print("Program selesai, Terima kasih")
