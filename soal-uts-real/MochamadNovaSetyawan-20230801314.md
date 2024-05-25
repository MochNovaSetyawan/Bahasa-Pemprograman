# SOAL 1
1. Jelaskan secara singkat apa itu paradigma dalam bahasa pemprograman
# JAWABAN
## JAWABAN ANDA
Paradigma dalam bahasa pemrograman mengacu pada gaya, metode, atau pendekatan yang fundamental dalam menulis dan merancang perangkat lunak. Paradigma ini tidak hanya mempengaruhi sintaks dan fitur yang digunakan dalam bahasa pemrograman tertentu, tetapi juga cara programmer memahami dan menyelesaikan masalah dalam pengembangan perangkat lunak. Berikut adalah beberapa paradigma pemrograman yang paling umum:
1. Pemrograman Imperatif

Ini adalah paradigma yang menggambarkan komputasi dalam bentuk pernyataan yang mengubah status program. Ini didasarkan pada konsep bahwa perintah dieksekusi secara sekuensial, dan setiap perintah mengubah status internal sistem. Bahasa seperti C dan Java sering mengikuti paradigma ini.
2. Pemrograman Deklaratif

Berfokus pada apa yang harus dicapai oleh program tanpa menentukan bagaimana hasilnya harus dicapai. Paradigma ini lebih peduli dengan hasil dari serangkaian operasi daripada langkah-langkah operasi itu sendiri. SQL dan HTML adalah contoh dari bahasa pemrograman yang menggunakan paradigma deklaratif.
3. Pemrograman Fungsional

Sebuah paradigma yang memperlakukan komputasi sebagai evaluasi dari fungsi matematika dan menghindari perubahan status atau data yang dapat diubah. Ini menggunakan fungsi tingkat tinggi, dan fungsi-fungsi ini sering menjadi argumen atau hasil dari fungsi lain. Bahasa seperti Haskell dan Scala didasarkan pada paradigma pemrograman fungsional.
4. Pemrograman Berorientasi Objek (OOP)

Dalam paradigma ini, program dibagi menjadi "objek", entitas kecil yang menyatukan data dan fungsi yang berhubungan dengan data tersebut. OOP menggunakan konsep seperti kelas, objek, pewarisan, enkapsulasi, dan polimorfisme untuk membantu dalam menciptakan struktur yang lebih modular dan dapat digunakan kembali. Java, Python, dan C++ adalah contoh bahasa yang mendukung OOP.
5. Pemrograman Logika

Sebuah paradigma yang didasarkan pada logika formal. Program ditulis sebagai sekumpulan pernyataan dalam bentuk logika, dan eksekusi program adalah proses mencocokkan pola dan mencari kesimpulan dari fakta-fakta. Prolog adalah salah satu bahasa yang menggunakan paradigma pemrograman logika.

# SOAL 2
2. Jelaskan apa yang di maksud dengan model data, operator, seleksi dan fungsi
# JAWABAN
## JAWABAN ANDA
Model Data

Model data adalah struktur atau mekanisme yang digunakan untuk menyimpan, memanipulasi, dan mengambil data dalam basis data atau sistem pengolahan data lainnya. Model data menentukan cara data disimpan, diorganisir, dan dihubungkan satu sama lain. Contohnya termasuk model relasional yang menggunakan tabel, baris, dan kolom, atau model objek yang menyimpan data dalam bentuk objek-objek dengan atribut dan metode.
Operator

Dalam pemrograman, operator adalah simbol atau kata kunci khusus yang digunakan untuk melakukan operasi pada satu atau lebih operand (nilai atau variabel). Operator memungkinkan pengguna untuk melakukan operasi matematika (seperti penjumlahan, pengurangan), operasi logika (AND, OR), operasi perbandingan (lebih besar dari, sama dengan), dan lain-lain.
Seleksi

Seleksi, sering disebut sebagai struktur kontrol "if-else" atau "switch", adalah mekanisme dalam pemrograman yang digunakan untuk membuat keputusan berdasarkan kondisi. Melalui seleksi, program dapat memilih jalur eksekusi tertentu berdasarkan apakah kondisi yang diberikan adalah benar atau salah. Ini adalah dasar dari logika bersyarat dalam pemrograman, memungkinkan program bertindak secara berbeda dalam respons terhadap berbagai situasi atau input.
Fungsi

Fungsi adalah blok kode yang terorganisir dan dapat digunakan kembali yang dirancang untuk melakukan tugas tertentu. Fungsi biasanya menerima input, melakukan beberapa operasi, dan mungkin mengembalikan output. Dalam pemrograman, fungsi digunakan untuk modularisasi dan pengurangan redundansi kode, memungkinkan pembuat kode untuk memisahkan program menjadi komponen-komponen yang lebih kecil, yang lebih mudah dikelola dan diuji. Fungsi bisa dibangun-in atau didefinisikan oleh pengguna.

Setiap konsep ini adalah fundamental dalam pengembangan perangkat lunak dan pemrograman komputer, memungkinkan pengembangan aplikasi yang efisien dan efektif.

# SOAL 3
3. jelaskan konsep perulangan pernyataan(Looping statement) di bawah ini
int n, _, i, _;
cout <<"Masukan jumlah baris : ";
cin >> n;
for (i = 1; i <= _; i++) {
    for (s = i; _ < n; _++)
    cout << "";
    for (j = 1; _ <= i; _++)
    cout << "*">>;
    cout <<"\n";
}

Pecahkan perulangan di atas, berikan penjelasan terhadap program tersebut dan keluaran dari program tersebut
# JAWABAN
## JAWABAN ANDA (essay3.cpp)
Program C++ yang diberikan menghasilkan pola segitiga terbalik, di mana pengguna diminta untuk memasukkan jumlah baris. Berikut adalah penjelasan singkat dari program:
1. Input Jumlah Baris: Pengguna memasukkan jumlah baris n yang diinginkan untuk pola.
2. Loop Utama (for dengan variabel i): Mengontrol jumlah baris yang dicetak. Setiap iterasi mencetak satu baris dari pola.
3. Loop Spasi (for dengan variabel s): Mencetak spasi di setiap baris untuk menyerupai bentuk segitiga yang melebar ke bawah. Jumlah spasi      berkurang seiring dengan bertambahnya baris.
4. Loop Bintang (for dengan variabel j): Mencetak bintang di setiap baris. Jumlah bintang bertambah seiring dengan bertambahnya baris.
5. Newline (\n): Mengakhiri setiap baris dengan newline untuk memulai baris baru.
Keluaran: Sebuah pola segitiga terbalik yang terdiri dari bintang, dengan bintang yang bertambah dari atas ke bawah dan spasi yang berkurang dari atas ke bawah. 

# SOAL 4
 Buatlah program sederhana dengan hasil akhir seperti berikut :
 Berarti Usia Kalian sekarang adalah 21 Tahun
# JAWABAN
## JAWABAN ANDA (essay4.cpp)

# SOAL 5
  Buatlah program sederhana dengan hasil akhir seperti berikut :
  Masukan Angka Pertama : 10
   Masukan Angka Kedua : 2
   Penjumlahan : 12
   Pengurangan : 8
   Perkalian : 20
   Pembagian : 5
# JAWABAN
## JAWABAN ANDA (essay5.cpp)

# SOAL 6
 Lengkapi penggalan source code berikut hingga bisa berfungsi dengan baik

 int main() {
    menu();
    tambah();
    kurang();
    kali();
    bagi();
    return 0;
 }
 ...
# JAWABAN
## JAWABAN ANDA (essay6.cpp)

# SOAL 7
 Buatlah diagram Alur/Flow yang sesuai dengan source code yang anda lengkapi (Soal no 6)
# JAWABAN
## JAWABAN ANDA (essay7.puml)