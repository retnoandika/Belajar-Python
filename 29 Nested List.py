data_0 = [1,2]
data_1 = [3,4]

data_list_biasa = [1,2,3,4]

print(f"list biasa = {data_list_biasa}")

list_2D = [data_0,data_1,5,7,2,4] # menggabungkan list dan data lain

print(f"list 2D = {list_2D}")

# contoh penggunaan
peserta_0 = ["Retno",21,"Laki-laki"]
peserta_1 = ["Andi",15,"Laki-laki"]
peserta_2 = ["Laras",20,"Perempuan"]

list_peserta = [peserta_0,peserta_1,peserta_2]
print(f"peserta = {list_peserta}\n")

for peserta in list_peserta:
    print(f"Nama\t : {peserta[0]}")
    print(f"Umur\t : {peserta[1]} tahun")
    print(f"Gender\t : {peserta[2]}\n")

# dengan reference
list_copy = list_peserta.copy()
print(f"peserta = {list_peserta}")
peserta_0[0] = 'Rean'
print(f"peserta = {list_copy}")
print(f"peserta = {list_peserta}")