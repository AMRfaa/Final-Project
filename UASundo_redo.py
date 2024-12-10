undo_stack = ["menjalankan office word", "membuka google chrome","menjelankan visual studio code"]
redo_stack = []

def menu():
    print("\n  >>  MENU  <<")
    print("1. Tambahkan aksi")
    print("2. Undo")
    print("3. Redo")
    print("4. Lihat stack undo dan redo")
    print("5. Keluar")

def tambah_aksi (aksi):
    undo_stack.append(aksi)
    redo_stack.clear()  
    print("Aksi",aksi,"ditambahkan.")

def undo():
    if undo_stack:
        aksi = undo_stack.pop()
        redo_stack.append(aksi)
        print("Undo aksi: ",aksi,)
    else:
        print("Tidak ada aksi untuk di-undo!")

def redo():
    if redo_stack:
        aksi = redo_stack.pop()
        undo_stack.append(aksi)
        print("Redo : ",aksi,".")
    else:
        print("Tidak ada aksi untuk di-redo!")

def hasil():
    print ("stack undo: ",undo_stack)
    print ("stack redo: ",redo_stack)
        
while True:
    menu()
    pilihan = input("Pilih menu (1-5): ")
    if pilihan == "1":
        aksi = input("Masukkan aksi: ")
        tambah_aksi (aksi)
    elif pilihan == "2":
        undo()
    elif pilihan == "3":
        redo()
    elif pilihan == "4":
        hasil()
    elif pilihan == "5":
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid! Silakan pilih menu yang tersedia.")
