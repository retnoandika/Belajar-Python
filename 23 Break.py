# Break = loop langsung stop atau berakhir
angka = 0

while angka < 5:
    angka += 1
    print(f"angka sekarang = {angka}")

    if angka == 3:
        print("nice")
        break

    print('wassup!')

print("cukup finish")

print(20*"=")


data_int = int(input("hitung sampai = "))
angka = 0

while True:
    angka += 1
    print(f"count = {angka}")

    if angka == data_int:
        print("nice")
        break

    print("okkay")

print("cukuup sudah selesai")

