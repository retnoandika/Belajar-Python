# memasukkan data atau argument

# dengan cara biasa
def fungsi(nama,tinggi,berat):
    print(f"{nama} memiliki tinggi {tinggi} cm dan berat {berat} kg")

fungsi("Retno",175,56)

# dengan cara list
def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama} memiliki tinggi {tinggi} cm dan berat {berat} kg")

fungsi(["Dika",140,40])

# Menggunakan *args (argument) : mirip seperti list tapi tanpa ".copy" dan kurung siku saat print
def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} memiliki tinggi {tinggi} cm dan berat {berat} kg")

fungsi("Yusuf",160,46)

# studi kasus # tidak perlu pakai args asal ada tanda '*'
def tambah(*data):
    # data tipenya adalah tuple, dia bisa diiterasi
    output = 0 
    for angka in data:
        output += angka
    return output

hasil = tambah(1,3,5,7,6,4)
print(f"hasil = {hasil}")
     
hasil = tambah(14,45,41)
print(f"hasil = {hasil}")

print(f"hasil = {tambah(3,4,3)}")
# bisa menggunakan banyak data 