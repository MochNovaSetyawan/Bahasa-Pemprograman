#include <iostream>

using namespace std;

double tambah(double x, double y) {
    return x + y;
}

double kurang(double x, double y) {
    return x - y;
}

double kali(double x, double y) {
    return x * y;
}

double bagi(double x, double y) {
    if (y == 0) {
        cout << "Error: Pembagian dengan nol" << endl;
        return 0;
    }
    return x / y;
}

void tampilan_info() {
    cout << "Operasi:" << endl;
    cout << "1. Tambah" << endl;
    cout << "2. Kurang" << endl;
    cout << "3. Kali" << endl;
    cout << "4. Bagi" << endl;
    cout << "5. Keluar" << endl;
}

int main() {
    while (true) {
        tampilan_info();
        int pilihan;
        cout << "Pilih operasi (1/2/3/4/5): ";
        cin >> pilihan;

        if (pilihan >= 1 && pilihan <= 4) {
            double value1, value2;
            cout << "Masukkan angka pertama: ";
            cin >> value1;
            cout << "Masukkan angka kedua: ";
            cin >> value2;

            double hasil;
            switch (pilihan) {
                case 1:
                    hasil = tambah(value1, value2);
                    break;
                case 2:
                    hasil = kurang(value1, value2);
                    break;
                case 3:
                    hasil = kali(value1, value2);
                    break;
                case 4:
                    hasil = bagi(value1, value2);
                    break;
            }
            cout << "Hasil: " << hasil << endl;
        } else if (pilihan == 5) {
            cout << "Keluar dari program..." << endl;
            break;
        } else {
            cout << "Pilihan tidak valid!" << endl;
        }
    }

    return 0;
}
