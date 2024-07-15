# -*- coding: utf-8 -*-
"""M1_Capstone CRUD_Kenzi

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Xgv95aMoHQu5ScOs4ete4z4xLqOBTtuL
"""

# Capstone Project M1
# Kenzi Lamberto
# Data Stok Gudang

#!pip install tabulate
from tabulate import tabulate

# database awalnya
gudang_db = [
    {"Kode": "INTC1", "Merek" : "Intel", "Tipe" : "CPU", "Nama" : "i7", "Harga" : 250000, "Stok": 1},
    {"Kode": "INTC2", "Merek" : "Intel", "Tipe" : "CPU", "Nama" : "i5", "Harga" : 200000, "Stok": 5},
    {"Kode": "AMDG3", "Merek" : "AMD", "Tipe" : "GPU", "Nama" : "Radeon 7", "Harga" : 270000, "Stok": 3},
    {"Kode": "AMDC4", "Merek" : "AMD", "Tipe" : "CPU", "Nama" : "Ryzen 5", "Harga" : 180000, "Stok": 0}
 ]


# =========================================================================================
# Fungsi Main Menu
def main_menu():
    while True:
        print()
        print("Selamat Datang di Stok Gudang Kenzi!\n Silahkan pilih menu di bawah")
        print('''
        List Menu:
        1. Menampilkan Daftar Barang
        2. Menambahkan Barang Baru
        3. Mengupdate Informasi dari suatu Barang
        4. Menghapus Barang
        5. CEPAT INFOKAN KEPERLUAN TAMBAH STOK
        6. Exit
        ''')

        user_choice(choose_option())
        break

# User input function
def choose_option():
    user_choice = input("Pilih Opsi dari List Menu: ")
    return user_choice

# Direct menu function
def user_choice(a_choice):

    if a_choice == '1':
        menu_read()
    elif a_choice == '2':
        menu_create()
    elif a_choice == '3':
        menu_update()
    elif a_choice == '4':
        menu_delete()
    elif a_choice == '5':
        menu_restock()
    elif a_choice == '6':
        menu_exit()
    else:
        print("\nInput yang anda masukkan tidak sesuai dengan pilihan menu yang tersedia")
        main_menu()
        user_choice(choose_option())

# =========================================================================================
# Fungsi Menu Read
def menu_read():
    print(tabulate(gudang_db,headers = 'keys', tablefmt = 'pretty'))
    main_menu()


# =========================================================================================
# Fungsi Menu Create
def menu_create():
    global gudang_db
    new_stock_brand = input_stock_brand()
    new_stock_type = input_stock_type()
    new_stock_name = input_stock_name()
    new_stock_price = input_stock_price()
    new_stock_amount = input_stock_amount()
    new_stock_id = auto_stock_id(new_stock_brand, new_stock_type)
    new_stock_data = {'Kode': new_stock_id, 'Merek': new_stock_brand, "Tipe" : new_stock_type, 'Nama': new_stock_name, 'Harga': new_stock_price, 'Stok': new_stock_amount}
    gudang_db.append(new_stock_data)
    print("Sukses menambahkan barang!")
    main_menu()

# Apa mereknya
def input_stock_brand():
    print('''
    List Menu:
    1. Menambahkan Merek Intel
    2. Menambahkan Merek AMD
    3. Menambahkan Merek Lainnya
    4. Back to Main Menu
    ''')
    #stock_brand = 0
    user_input = input("Pilih Opsi dari List Menu: ")
    if user_input == '1':
        stock_brand = "Intel"
        return stock_brand
    elif user_input == '2':
        stock_brand = "AMD"
        return stock_brand
    elif user_input == '3':
        stock_brand = input("Ketik Nama Merek: ")
        return stock_brand
    elif user_input == '4':
        main_menu()
    else:
        print('input tidak sesuai, gw pulangin ke main menu ya')
        main_menu()

# Apa tipenya
def input_stock_type():
    print('''
    List Menu:
    1. Menambahkan Tipe CPU
    2. Menambahkan Tipe GPU
    3. Menambahkan Tipe Lainnya
    4. Back to Main Menu
    ''')
    #stock_brand = 0
    user_input = input("Pilih Opsi dari List Menu: ")
    if user_input == '1':
        stock_type = "CPU"
        return stock_type
    elif user_input == '2':
        stock_type = "GPU"
        return stock_type
    elif user_input == '3':
        stock_type = input("Ketik Nama Tipe: ")
        return stock_type
    elif user_input == '4':
        main_menu()
    else:
        print('input tidak sesuai, gw pulangin ke main menu ya')
        main_menu()

# Apa namanya
def input_stock_name():
    stock_name = input("Ketik Nama Barang (ketik back untuk kembali ke main menu): ")
    if stock_name.lower() == 'back':
        main_menu()
    else:
        return stock_name

# Berapa harganya
def input_stock_price():
    stock_price = int(input("Ketik Harga Barang: "))
    if stock_price > 0:
        return stock_price
    else:
        print('input tidak sesuai, gw pulangin ke main menu ya')
        main_menu()

# Berapa jumlah stoknya
def input_stock_amount():
    stock_amount = int(input("Ketik Jumlah Barang: "))
    if stock_amount >= 0:
        return stock_amount
    else:
        print('input tidak sesuai, gw pulangin ke main menu ya')
        main_menu()

# Auto buat ID-nya
def auto_stock_id(stock_brand, stock_type):
    global gudang_db
    stock_id = stock_brand[0:3].upper() + str(stock_type[0]) + str(len(gudang_db))
    return stock_id

# =========================================================================================
# Fungsi Menu Update
def menu_update():
    global gudang_db
    input_update()
    main_menu()

def input_update():
    print(tabulate(gudang_db,headers = 'keys', tablefmt = 'pretty'))
    #global gudang_db
    list_id_stock = []
    list_id_column = []

    input_id = input("Masukkan ID barang yang hendak di-update: ").upper()

    for i in gudang_db:
        list_id_stock.append(i['Kode'])

    list_id_column = list(gudang_db[0].keys())
    list_id_column.pop(0)


    if input_id in list_id_stock:
        print("Ketik salah satu dari nama kolom berikut", list_id_column)
        input_column_name = input(f"Masukkan nama kolom untuk diganti dari item dengan ID {input_id}: ").capitalize()

        while input_column_name not in list_id_column:
            print("Kolom yang dimasukkan tidak ada, ulangi")
            input_column_name = input(f"Masukkan ulang nama kolom untuk diganti dari item dengan ID {input_id}: ").capitalize()

            if input_column_name in list_id_column:
                return update_stock_info(list_id_stock, input_id, input_column_name)
            else:
                continue
        else:
            return update_stock_info(list_id_stock, input_id, input_column_name)

    else:
        print("ID yang dimasukkan tidak ada, ulangi")
        return input_update()

def update_stock_info(list_id_stock, input_id, input_column_name):
    new_value = input(f"Input value baru dari ID {input_id} pada kolom {input_column_name}: ")
    if input_column_name == "Harga":
        input_column_name = int(input_column_name)
        while new_value <= 0:
            print(f"\n Value dari kolom {input_column_name} tidak boleh 0 ataupun negatif")
            new_value = input(f"Input value baru dari ID {input_id} pada kolom {input_column_name}: ")

    elif input_column_name == "Stok":
        input_column_name = int(input_column_name)
        while new_value < 0:
            print(f"\n(INFO) Value dari kolom {input_column_name} tidak boleh negatif")
            new_value = input(f"Input value baru dari ID {input_id} pada kolom {input_column_name}: ")

    # Memberi konfirmasi untuk finalisasi update
    yes_no = input(f"Apakah anda ingin mengupdate data dari data stok {input_id} (y/n)? ")

    if yes_no == 'y':
        # Jika kolom memengaruhi ID, maka ID akan update (berarti Merek dan Tipe maka ID berpengaruh kan ya)
        # Jika kolom tidak memengaruhi ID, langsung saja replace data
        input_id_index = list_id_stock.index(input_id)
        if input_column_name == "Merek":
            gudang_db[input_id_index][input_column_name] = new_value
            new_input_id = new_value[0:3].upper() + input_id[3:]
            gudang_db[input_id_index]["Kode"] = new_input_id

        elif input_column_name == "Tipe":
            gudang_db[input_id_index][input_column_name] = new_value
            new_input_id = input_id[0:3] + new_value[0] + input_id[4]
            gudang_db[input_id_index]["Kode"] = new_input_id

        else:
            gudang_db[input_id][input_column_name] = new_value

        continue_or_no()

    elif yes_no == 'n':
        main_menu()
    else:
        print("Input salah, ulangi")
        return update_stock_info(list_id_stock, input_id, input_column_name)

# Untuk memberi opsi kepada user apakah mereka ingin melanjutkan update atau tidak
def continue_or_no():
    user_input = input("Ingin mengupdate informasi dari barang lagi (y/n)?").lower()

    if user_input == "y":
        input_update()
    elif user_input == "n":
        main_menu()
    else:
        print("Input salah, ulangi")
        continue_or_no()



# =========================================================================================
# Fungsi Menu Delete
def menu_delete():
    global gudang_db
    input_delete()
    main_menu()

def input_delete():
    print(tabulate(gudang_db,headers = 'keys', tablefmt = 'pretty'))
    #global gudang_db
    list_id_stock = []

    input_id = input("Masukkan ID barang yang hendak di-delete: ").upper()

    for i in gudang_db:
        list_id_stock.append(i['Kode'])

    if input_id in list_id_stock:
        yes_no = input(f"Apakah anda ingin menghapus data {input_id} dari data stok {input_id} (y/n)? ")

        if yes_no == 'y':
            input_id_index = list_id_stock.index(input_id)
            gudang_db.pop(input_id_index)
        elif yes_no == "n":
            main_menu()
        else:
            print("Input salah, ulangi")
            input_delete()


# =========================================================================================
# Fungsi Menu Restock
def menu_restock():
    global gudang_db
    need_restock = []

    for i in gudang_db:
        if i["Stok"] == 0:
            need_restock.append(i)
    print("Berikut List Barang yang perlu direstock segera")
    print(tabulate(need_restock,headers = 'keys', tablefmt = 'pretty'))


# =========================================================================================
# Fungsi Menu Exit
def menu_exit():
    exit()

# Run the program from Main Menu
main_menu()
