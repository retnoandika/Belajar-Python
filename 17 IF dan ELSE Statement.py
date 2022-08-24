# If dan Else Statement

# 1. if ny
# 2. kondisi
# 3. aksinya

nama = input("Siapa nama anda? ")

# 1. program if inline
if nama == "Retno" : print('Kamu lagi apa?')
print('akhir dari program')

# 2. program if indentation
nama = input("Siapa nama anda? ")
if nama == "Retno":
    print("Kamu lagi apa?")
    print("Lagi dimana?")
print(f"Terima kasih {nama}")

# 3. Else statement
nama = input("Siapa nama anda? ")
if nama == 'Retno':
    print(f"Hai {nama}, kamu lagi belajar kah?" )
else:
    print(f'Ah kamu {nama}, kirain siapa')
print("Terima kasih waktunya")