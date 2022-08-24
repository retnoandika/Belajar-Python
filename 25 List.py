## --- lIST ---

# Kumpulan data numbers
data_angka = [2,5,6,3,5,9]
print(data_angka)

# Kumpulan data string
data_string = ["retno","dika",'andi']
print(data_string)

# Kumpulan data boolean
data_boolean = [True, False, False, True, True]
print(data_boolean)

# Kumpulan data campuran
data_campuran = [2,3,4,"retno","beli", True, False, "ikan", 5]
print(data_campuran)

# cara alternatif membuat list
data_range = range(0,10,2) # range(start,stop,step)
print(data_range)
data_list = list(data_range)
print(data_list)

# membuat list dengan for loop, list comprehension
list_for = [i for i in range(0,10)]
print(list_for)
list_for = [i**3 for i in range(0,10)] # dapat digabungkan dengan berbagai operator +,-,/,*,**,%
print(list_for)

# membuat list dengan for dan if
list_for_if = [i for i in range(0,10) if i != 5] # menghilangkan angka 5
print(list_for_if)

list_for_if = [i for i in range(0,10) if i%2 == 0] # angka genap
print(list_for_if)

list_for_if = [i**2 for i in range(0,10) if i%2 != 0] # angka ganjil dan di kuadratkan
print(list_for_if)

