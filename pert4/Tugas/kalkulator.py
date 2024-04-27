def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    if y == 0:
        return "Error: Pembagian dengan nol"
    return x / y

def hitung(pilihan, value1, value2):
    if pilihan == '1':
        return tambah(value1, value2)
    elif pilihan == '2':
        return kurang(value1, value2)
    elif pilihan == '3':
        return kali(value1, value2)
    elif pilihan == '4':
        return bagi(value1, value2)
    
def tampilan_info():
    print("Operasi:")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("5. Keluar")

def main():
    while True:
        tampilan_info()
        pilihan = input("Pilih operasi (1/2/3/4/5): ")

        if pilihan in ('1', '2', '3', '4'):
            try:
                value1 = float(input("Masukkan angka pertama: "))
                value2 = float(input("Masukkan angka kedua: "))
                hasil = hitung(pilihan, value1, value2)
                print("Hasil: ", hasil)
            except ValueError:
                print("Input tidak valid. Harap masukkan angka.")
        elif pilihan == '5':
            print("Keluar dari program...")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
         