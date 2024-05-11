def tampilkan_menu(menu):
    for index, item in enumerate(menu):
        print(f"{index+1}. {item} - Rp{menu[item]}")

def definisi_menu():
    menu_teh = {
        'Teh Hitam': 5000,
        'Teh Hijau': 6000,
        'Teh Manis': 4000,
    }
    menu_kopi = {
        'Kopi Tubruk': 8000,
        'Kopi Latte': 15000,
        'Kopi Susu': 10000,
    }
    return menu_teh, menu_kopi

def function_pilihMenu(menu_teh, menu_kopi):
    while True:
        pilihan = input("Pilih minuman Anda (Teh/Kopi): ").lower()
        if pilihan == "teh":
            tampilkan_menu(menu_teh)
            return menu_teh
        elif pilihan == "kopi":
            tampilkan_menu(menu_kopi)
            return menu_kopi
        else:
            print("Pilihan tidak valid. Silakan pilih antara 'Teh' atau 'Kopi'.")

def function_pilihListMenu(menu_dipilih):
    total_harga = 0
    while True:
        pilihan_item = int(input("Pilih nomor menu yang diinginkan (atau 0 untuk selesai): "))
        if pilihan_item == 0:
            break
        if 1 <= pilihan_item <= len(menu_dipilih):
            item_terpilih = list(menu_dipilih.keys())[pilihan_item - 1]
            jumlah = int(input(f"Berapa banyak {item_terpilih} yang Anda inginkan? "))
            total_harga += jumlah * menu_dipilih[item_terpilih]
        else:
            print("Pilihan tidak valid. Silakan pilih nomor yang sesuai dengan menu.")
    return total_harga

def main():
    menu_teh, menu_kopi = definisi_menu()
    menu_dipilih = function_pilihMenu(menu_teh, menu_kopi)
    total_harga = function_pilihListMenu(menu_dipilih)
    print(f"Total yang harus dibayar: Rp{total_harga}")

if __name__ == "__main__":
    main()
