import sains.matematika
# from sains import fisika # cara lain pakai "from"
from sains.fisika import gaya as force # cara lain pakai "." untuk lebih ke fokus rumusnya ke mana



hasil_tambah = sains.matematika.tambah(5,5,6,4)
print(f"hasil tambah dari package = {hasil_tambah}")


gaya = force(90,10)
print(f"gaya adalah = {gaya}")