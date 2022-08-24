# Pass -> berfungsi sebagai dummy, tidak akan dieksekusi
print(5*"=", "Pass", 5*"=")
angka = 0
print(f"angka sekarang -> {angka}")

while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}") # aksi 1

    if angka == 3:
        print("nice")
        pass # tidak akan dieksekusi

    print("whassup!") # aksi 2
print("\n")

# Continue
print(5*"=", "Continue", 5*"=")
angka = 0
print(f"angka sekarang -> {angka}")

while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}") # aksi 1

    if angka == 3:
        print("nice")
        continue # akan membuat loop melompat ke step selanjutnya

    print("whassup!") # aksi 2

print("Finish")



