''' Default Argument'''

# def fungsi(argement)
# def fungsi(argement = nilai defaultnya):

# contoh 1
def say_hello(nama = "Ganteng"):
    '''fungsi dengan default argement'''
    print(f"Hello {nama}")

say_hello("Retno")
say_hello() # () jika tidak ada isinya akan mengikuti defaultnya

# contoh 2
def sapa_dia(nama,pesan = "Apa kabar?"):
    '''Fungsi dengan satu input biasa, dan satu default'''
    print(f"Hai {nama}, {pesan}")

sapa_dia("Retno","Hai ganteeng")
sapa_dia("Andika")

# contoh 3
def hitung_pangkat(angka,pangkat):
    hasil = angka**pangkat
    return hasil

print(hitung_pangkat(2,4))

hasil = hitung_pangkat(pangkat=3, angka=5) # bisa dibalik dan di definisikan isinya
print(hasil)

# contoh 4 
def fungsi(input1=1,input2=2,input3=3,input4=4):
    hasil = input1 + input2 + input3 + input4
    return hasil

print(fungsi())
print(fungsi(input3=10,input2=10)) # bisa dirubah argumentnya asal ada definisinya