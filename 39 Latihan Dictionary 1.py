import datetime
import os
import string
import random

# template dictionary mahasiswa
mahasiswa_template = {
    'nama':'nama',
    'npm':'00000000',
    'sks_lulus':0,
    'lahir':datetime.datetime(1111,1,11)
}

data_mahasiswa = {}

while True:
    os.system('cls')
    print(f"{'SELAMAT DATANG':^20}")
    print(f"{'DATA MAHASISWA':^20}")
    print("-"*20)

    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    mahasiswa['nama'] = input('Nama Mahasiswa: ')
    mahasiswa['npm'] = input('NPM Mahasiswa: ')
    mahasiswa['sks_lulus'] = input('SKS Lulus: ')
    tahun_lahir = int(input('Tahun lahir (yyyy): '))
    bulan_lahir = int(input('Bulan lahir (1-12): '))
    tanggal_lahir = int(input('Tanggal lahir (1-31): '))
    mahasiswa['lahir'] = datetime.datetime(tahun_lahir,bulan_lahir,tanggal_lahir)

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_mahasiswa.update({KEY:mahasiswa})

    print(f"{'KEY':<6} {'Nama':<17} {'NPM':<8} {'SKS':<3} {'Tanggal Lahir':<8}")
    print("-"*56)

    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa
        NAMA = data_mahasiswa[KEY]['nama']
        NPM = data_mahasiswa[KEY]['npm']
        SKS = data_mahasiswa[KEY]['sks_lulus']
        LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

        print(f"{KEY:<6} {NAMA:<17} {NPM:<8} {SKS:^3} {LAHIR:<9}")

    print("\n")        
    is_done = input('Apakah ingin menambahkan data?(y/n)')
    if is_done == 'n':
        break

print("\nAkhir dari program, terima kasih")
