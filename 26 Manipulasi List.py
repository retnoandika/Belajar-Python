## Operasi

# index 0(-3), 1(-2), 2(-1)
data = ["Retno", "Andi", "Dika"]

# mengambil data dari list ini
data_0 = data[0]
print(f"data pertama (index 0)   = {data_0}")
data_0 = data[-3]
print(f"data pertama (index -3)  = {data_0}")

data_tengah = data[1]
print(f"data tengah (index 1)    = {data_tengah}")
data_tengah = data[-2]
print(f"data tengah (index -2)   = {data_tengah}")

data_terakhir = data[2]
print(f"data terakhir (index 2)  = {data_terakhir}")
data_terakhir = data[-1]
print(f"data terakhir (index -1) = {data_terakhir}")

# mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"panjang data = {panjang_data}")

# menambahkan item pada list sesuai posisi
print(f"data sebelum ditambah = \n{data}")

data.insert(2,"Rean") # angka menandakan posisi indexnya
print(f"data sesudah ditambah = \n{data}")

data.append("Yusuf")
print(f"data ditambah lagi diakhir = \n{data}")

# menambah list dengan list
data_baru = ('Noor','Riyadi','Hana')
data.extend(data_baru)
print(f"data gabungan = \n{data}")

# merubah data
data[2] = 'Mahar'
print(f"data rubah = \n{data}")

# meremove data
data.remove('Andi')
print(f"data remove = \n{data}")

# meremove data paling akhir
data.pop()
print(f"data remove akhir = \n{data}")

data_akhir = data.pop() # cara penulisan yang berbeda
print(f"data remove akhir = \n{data}")
print(data_akhir)