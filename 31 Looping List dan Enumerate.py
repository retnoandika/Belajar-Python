# looping dari list

# for loop
print("for loop")
kumpulan_angka = [4,3,2,5,6,1]

for angka in kumpulan_angka:
    print(f"angka = {angka}")

peserta = ["retno","andi","dika","mahar","yusuf"]

for nama in peserta:
    print(f"nama  = {nama}")

# for loop dan range
print("\nfor loop dan range")
kumpulan_angka =[10,5,7,3,7,5,3]

panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f"angka = {kumpulan_angka[i]}")

# while loop
print("\nwhile loop")
kumpulan_angka = [10,5,7,3,7,5,3]

panjang = len(kumpulan_angka)
i = 0

while i < panjang:
    print(f"angka = {kumpulan_angka[i]}")
    i += 1

# list comprehension
print("\nlist comprehension")

data = ["dika",1,2,3,"andi"]
[print(f"data = {i}") for i in data]

kumpulan_angka = [10,5,7,3,7,5,3]
[print(f"data = {i}") for i in kumpulan_angka]

angka = [10,5,7,3,7,5,3]
angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)

# enumerate
print("\nenumerate")
data_list = ["dika",1,2,3,"andi"]

for index,data in enumerate(data_list):
    print(f"index = {index}, data = {data}")