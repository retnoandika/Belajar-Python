# Kalkulator sederhana
print(20*"=")
print("Kalkulator Sederhana")
print(20*"=", "\n")

angka_1 = float(input("masukkan angka 1 = "))
operator = input("operator (+, -, /, x) = ")
angka_2 = float(input("masukkan angka 2 = "))

# percabangan
if operator == "+":
    hasil = angka_1 + angka_2
    print(f"{angka_1} {operator} {angka_2} = {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"{angka_1} {operator} {angka_2} = {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"{angka_1} {operator} {angka_2} = {hasil}")
elif operator == "x" or operator == "*":
    hasil = angka_1 * angka_2
    print(f"{angka_1} {operator} {angka_2} = {hasil}")
else:
    print("Masukkan yang benar dong! bikin salah aja")

print("Terima kasih sudah mencoba kalkulator sederhana")
