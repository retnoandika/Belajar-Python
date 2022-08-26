# Teknik menduplikat list

a = ["Retno",'Andi',"Dika"]
print(f"a = {a}")

b = a # pass by reference
print(f"b = {b}")

# Ini akan merubah kedua list
a[1] = 'Mahar'
b.sort()
print(f"a = {a}")
print(f"b = {b}")

# address dari kedua list a dan b
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")

# menduplikat list dengan copy
print(f"membuat list c dengan a.copy()")
c = a.copy() # full duplikat / data baru

print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")
print(f"address c = {hex(id(c))}")

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("kita ubah index 0")
c[0] = "Yusuf"
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("kita ubah index 1")
c[1] = "Noor"
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")