#include <iostream>

using namespace std;

int main() {
    int angkaPertama, angkaKedua;
    
    // Meminta input dari pengguna
    cout << "Masukan Angka Pertama : ";
    cin >> angkaPertama;
    cout << "Masukan Angka Kedua   : ";
    cin >> angkaKedua;
    
    cout << "Penjumlahan : " << angkaPertama + angkaKedua << endl;
    cout << "Pengurangan : " << angkaPertama - angkaKedua << endl;
    cout << "Perkalian   : " << angkaPertama * angkaKedua << endl;
    
    if (angkaKedua != 0) {
        cout << "Pembagian   : " << angkaPertama / angkaKedua << endl;
    } else {
        cout << "Pembagian   : tidak dapat dibagi dengan nol" << endl;
    }
    
    return 0;
}
