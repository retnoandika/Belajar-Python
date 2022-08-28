# operasi dictionary

data_dict = {
    "cup":"ucup surucup",
    "tong":"otong surotong",
    "dung":"dudung surudung"
}

# panjang dictionary
len_dict = len(data_dict)
print(f"panjang dictionary: {len_dict}")

# mengecek key exist atau tidak
key = "tong"
checkkey = key in data_dict
print(f"apakah {key} ada di data_dict: {checkkey}")

# mengakses value (read) dengan get
print(data_dict["cup"]) # print biasa
print(data_dict.get("cup")) # pakai get
print(data_dict.get("kis",)) # tidak ada key
print(data_dict.get("kis","key tidak ditemukan")) # dengan pesen tidak ditemukan

# mengupdate data
data_dict["cup"] = 'ucup si ganteng'
print(data_dict)
data_dict["sep"] = 'asep si kasyep'
print(data_dict)

data_dict.update({"cup":"ucup surucup"}) # cara yang lebih efektif dari sebelumnya diatas
print(data_dict)
data_dict.update({"retno":"retno si ganteng"}) # otomatis menambah data jika tidak ada 
print(data_dict)

# mendelete data pada dictionary
del data_dict['retno']
print(data_dict)
