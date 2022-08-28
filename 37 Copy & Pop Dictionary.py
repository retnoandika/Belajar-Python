# copy dictionary

teman_teman = {
    "cup":"ucup surucup",
    "tong":"otong surotong",
    "dung":"dudung surudung",
    "sep":"asep si kasyep",
    "cuy":"ucuy surucuy"
}

friends = teman_teman.copy() # pakai copy supaya salah satu data tidak berubah mengikuti yang satunya
print(f'teman-teman: {teman_teman}\n')
print(f'friends: {friends}\n')

teman_teman["cup"]="ucup si kereen"
print(f'teman-teman: {teman_teman}\n')
print(f'friends: {friends}\n')

# pop dictionary = berdasarkan key (mentransfer data) jadi data yg di dictionary menjadi hilang
dataAsep = friends.pop("sep")
print(f'data Asep: {dataAsep}\n')
print(f'friends: {friends}\n')

# popitem dictionary = yg terakhir yg diambil (mentransfer data) jadi data yg di dictionary menjadi hilang
dataTerakhir = friends.popitem()
print(f'data terakhir: {dataTerakhir}\n')
print(f'friends: {friends}\n')