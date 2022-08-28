import datetime
from uuid import NAMESPACE_DNS

mahasiswa1 = {
    "nama":"Ucup Surucup",
    "npm":"19022001",
    "sks_lulus":130,
    'beasiswa':False,
    'lahir':datetime.datetime(2001,4,10)
}

mahasiswa2 = {
    "nama":"Otong Surotong",
    "npm":"19022002",
    "sks_lulus":140,
    'beasiswa':True,
    'lahir':datetime.datetime(2002,10,10)
}

mahasiswa3 = {
    "nama":"Asep Si Kasyep",
    "npm":"19022003",
    "sks_lulus":100,
    'beasiswa':False,
    'lahir':datetime.datetime(2000,2,29)
}

data_mahasiswa = {
    'MAH001':mahasiswa1,
    'MAH002':mahasiswa2,
    'MAH003':mahasiswa3,
}

print(f"{'KEY':<6} {'NAMA':<17} {'NPM':<8} {'SKS':<3} {'BEASISWA':<9} {'LAHIR':<8}")
print("-"*56)

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa
    NAMA = data_mahasiswa[KEY]['nama']
    NPM = data_mahasiswa[KEY]['npm']
    SKS = data_mahasiswa[KEY]['sks_lulus']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

    print(f"{KEY:<6} {NAMA:<17} {NPM:<8} {SKS:^3} {BEASISWA:^9} {LAHIR:<9}")

