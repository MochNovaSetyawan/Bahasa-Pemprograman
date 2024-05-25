#include <iostream>

using namespace std;

void menu() {
    cout << "Menu Kalkulator Sederhana\n";
    cout << "1. Tambah\n";
    cout << "2. Kurang\n";
    cout << "3. Kali\n";
    cout << "4. Bagi\n";
}

int tambah(int a, int b) {
    return a + b;
}

int kurang(int a, int b) {
    return a - b;
}

int kali(int a, int b) {
    return a * b;
}

double bagi(int a, int b) {
    if (b != 0)
        return (double)a / b;
    else {
        cout << "Error: Pembagian dengan nol tidak diperbolehkan.\n";
        return 0.0;
    }
}

int main() {
    int x, y, opsi;
    
    menu();
    cout << "Masukkan pilihan operasi (1-4): ";
    cin >> opsi;
    cout << "Masukkan bilangan pertama: ";
    cin >> x;
    cout << "Masukkan bilangan kedua: ";
    cin >> y;

    switch (opsi) {
        case 1:
            cout << "Hasil Tambah: " << tambah(x, y) << endl;
            break;
        case 2:
            cout << "Hasil Kurang: " << kurang(x, y) << endl;
            break;
        case 3:
            cout << "Hasil Kali: " << kali(x, y) << endl;
            break;
        case 4:
            cout << "Hasil Bagi: ";
            if (y == 0) {
                cout << "Error: Pembagian dengan nol tidak diperbolehkan.\n";
            } else {
                cout << bagi(x, y) << endl;
            }
            break;
        default:
            cout << "Pilihan tidak valid.\n";
            break;
    }
    
    return 0;
}
