# import 

# fungsinya adalah untuk mengambil program dari file external .py
# program dari file external .py

# 1. untuk menyambung program dari external
import program_print
import program_dika

# 2. import dengan data
import program_variable
import program_yusuf

# data ada di namespace variable
print(program_variable.data)
print(program_yusuf.data)

# 3. import dengan fungsi
import mtk
hasil = mtk.tambah(4,5)
print(hasil)