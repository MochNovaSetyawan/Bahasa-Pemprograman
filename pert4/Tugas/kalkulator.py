def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Pembagian dengan nol"

def main():
    while True:
        print("Operasi:")
        print("1. Tambah")
        print("2. Kurang")
        print("3. Kali")
        print("4. Bagi")
        print("5. Keluar")

        pilihan = input("Pilih operasi (1/2/3/4/5): ")

        if pilihan in ('1', '2', '3', '4'):
            num1 = float(input("Masukkan angka pertama: "))
            num2 = float(input("Masukkan angka kedua: "))

            if pilihan == '1':
                print("Hasil: ", tambah(num1, num2))

            elif pilihan == '2':
                print("Hasil: ", kurang(num1, num2))

            elif pilihan == '3':
                print("Hasil: ", kali(num1, num2))

            elif pilihan == '4':
                print("Hasil: ", bagi(num1, num2))
        
            elif pilihan == '5':
            print("Keluar dari program...")
            break
        
            else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()