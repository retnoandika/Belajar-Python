
import numpy as np # Berguna untuk data scient dan machine learning

list_a = [1,2,3,4] # list biasa
vector_a = np.array([1,2,3,4]) # pakai numpy

print(f"list_a = {list_a}")
# print(f"list_a pangkat 2 = {list_a**2}") <- ini akan gagal 
print(f"vector_a = {vector_a}")
print(f"vector_a pangkat 2 = {vector_a**2}") 
print(f"vector_a kali 5 = {vector_a*5}") 

matrix_b = np.array([(1,2),(3,4)])
print(f"matrix_b = \n{matrix_b}")
print(f"matrix_b pangkat 2 = \n{matrix_b**2}")

zeros_c = np.zeros((2,2)) # angka awal untuk jumlah baris dan angka ke dua untuk kolom
print(f"zeros c = \n{zeros_c}")

ones_d = np.ones((2,2))
print(f"ones d = \n{ones_d}")

jumlah = matrix_b + matrix_b**2 + ones_d
print(f"jumlah = {jumlah}")