# GUI -> Graphical User Interface

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Init
window = tk.Tk()
window.configure(bg="white") # background jemdela
window.geometry("400x200") # ukuran jendela
window.resizable(False,False) # mengunci ukuran jendela supaya tidak dapat diubah
window.title("Program Retno Andika") # memberi judul

# Variable 
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

# Fungsi
def tombol_click():
    '''fungsi ini akan dipanggil oleh tombol'''
    pesan = f'Hallo {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}, Ganteeng!'
    showinfo(title="Whazzup!",message=pesan)

# Frame input
input_frame = ttk.Frame(window)
# Penempatan grid, pack, place
input_frame.pack(padx=10,pady=10,fill="x",expand=True)

# Komponen-komponen
# 1. label nama depan
nama_depan_label = ttk.Label(input_frame,text="Nama Depan")
nama_depan_label.pack(padx=10,fill="x",expand=True)
# 2. Entry nama depan
nama_depan_entry = ttk.Entry(input_frame,textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10,fill="x",expand=True)
# 3. label nama belakang
nama_belakang_label = ttk.Label(input_frame,text="Nama Belakang")
nama_belakang_label.pack(padx=10,fill="x",expand=True)
# 4. Entry nama belakang
nama_belakang_entry = ttk.Entry(input_frame,textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10,fill="x",expand=True)
# 5. Tombol
tombol_sapa = ttk.Button(input_frame,text="Sapa!",command=tombol_click)
tombol_sapa.pack(fill="x",expand=True,padx=10,pady=10)

# Main loop window
window.mainloop()