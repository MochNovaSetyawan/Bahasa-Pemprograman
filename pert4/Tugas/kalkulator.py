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
    print("1.Tambah")
    print("2.Kurang")
    print("3.Kali")
    print("4.Bagi")
    print("5.Keluar")


def main():
    while True:
        pilihan = input("Pilih operasi (1/2/3/4/5): ")

        if pilihan in ('1', '2', '3', '4'):
            value1 = float(input("Masukkan angka pertama: "))
            value2 = float(input("Masukkan angka kedua: "))
            hasil = hitung(pilihan, value1, value2)
            print("Hasil: ", hasil)
        elif pilihan == '5':
            print("Quit")
            break
        else:
            print("Pilihan tidak valid!")        


if __name__ == "__main__":
    main()            