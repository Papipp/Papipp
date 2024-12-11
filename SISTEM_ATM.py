 # Fungsi baca database
def read_data():
    accounts = {}
    try:
        with open('atm_data.txt', 'r') as file:
            for line in file:
                account_id, saldo = line.strip().split(',')
                accounts[account_id] = {'saldo': float(saldo)}
    except FileNotFoundError:
        pass  # Jika file tidak ada, kembalikan dictionary kosong
    return accounts

# Fungsi menulis isi database
def write_data(data):
    with open('atm_data.txt', 'w') as file:
        for account_id, account_info in data.items():
            file.write(f"{account_id},{account_info['saldo']}\n") 

# Fungsi untuk menampilkan menu
def pilihan_menu():
    print("====== ATM ======")
    print("=pilih Transaksi=")
    print("1. Cek Saldo") 
    print("2. Setor Uang")
    print("3. Tarik Uang")
    print("4. Keluar")
    print("=================")

# Fungsi cek saldo
def cek_saldo(account):
    print(f"Saldo Rekening Anda : {account['saldo']}")

# Fungsi setor uang
def setor_uang(account):
    while True:
        try:
            jumblah = float(input("Masukkan jumlah uang yang ingin disetor : "))
            if jumblah <= 0:
                print("Jumlah harus lebih besar dari 0.")
                continue
            account['saldo'] += jumblah
            print(f"Anda telah menyetor : {jumblah}")
            print(f"Saldo Rekening Anda sekarang : {account['saldo']}")
            break
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

# Fungsi tarik uang
def tarik_uang(account):
    while True:
        try:
            jumblah = float(input("Masukkan jumlah uang yang ingin ditarik : "))
            if jumblah <= 0:
                print("Jumlah harus lebih besar dari 0.")
                continue
            if jumblah > account['saldo']:
                print("Saldo Rekening Anda tidak cukup!")
            else:
                account['saldo'] -= jumblah
                print(f"Anda telah menarik: {jumblah}")
                print(f"Saldo Rekening Anda sekarang: {account['saldo']}")
                break
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

# Fungsi utama sistem ATM
def sistem_atm():
    # Membaca data pengguna
    accounts = read_data()
    
    # Input ID akun
    account_id = input("Masukkan ID Akun Anda: ")
    
    # Jika akun tidak ada, buat akun baru
    if account_id not in accounts:
        accounts[account_id] = {'saldo': 0}
        print("Akun baru telah dibuat.")
    
    account = accounts[account_id]

    while True:
        pilihan_menu()
        pilihan = input("Pilih Transaksi (1-4): ")

        if pilihan == '1':
            cek_saldo(account)
        elif pilihan == '2':
            setor_uang(account)
        elif pilihan == '3':
            tarik_uang(account)
        elif pilihan == '4':
            print("Terima kasih telah menggunakan ATM!")
            break
        else:
            print("Pilihan tidak valid! Silakan pilih antara 1-4.")

    # Menyimpan data kembali ke file databse
    write_data(accounts)

# Menjalankan sistem ATM
if __name__ == "__main__":
    sistem_atm()