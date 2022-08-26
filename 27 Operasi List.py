data_angka =[1,4,2,4,7,3,8,7,7,8,6,5,4,8,2,5,2,9,8,3]

print(f"data angka = \n{data_angka}")

# count data
jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)

print(f"jumlah angka 4 = {jumlah_data_4}")
print(f"jumlah angka 3 = {jumlah_data_3}")

# ambil posisi data (index)
data = ["Retno","Andi","Dika","Yusuf"]
print(f'data = {data}')

index_andi = data.index("Andi")
index_yusuf = data.index("Yusuf")
print(f"index si Andi = {index_andi}")
print(f"index si Yusuf = {index_yusuf}")

# mengurutkan data
print(f"data angka sebelum di sort = \n{data_angka}")
data_angka.sort()
print(f"data angka sort = \n{data_angka}")

print(f"data = \n{data}")
data.sort()
print(f"data sort = \n{data}")

# balik urutan list
data_angka.reverse()
data.reverse()
print(f"data di reverse = \n{data_angka} \n{data}")
