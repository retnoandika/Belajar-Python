'''Fungsi dengan argument'''

def hello_world(nama):
    print(f"Selamat datang di dunia {nama}")

hello_world("Retno Andika")
hello_world("Yusuf Mahardika")


# program tambah
def tambah (angka_1,angka_2):
    '''fungsi tambah'''
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {hasil}")

tambah(999,1)
tambah(234,766)

def say_hi(list_peserta):
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f"Yang terhormat {peserta}")

anggota_peserta = ["retno","andik","yusuf"]

say_hi(anggota_peserta)