from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
#Produkkkk
class Produk(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    harga = db.Column(db.Float, nullable=False)
    stok = db.Column(db.Integer, nullable=False)

    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

    def __repr__(self):
        return f"Produk({self.nama}, Harga: {self.harga}, Stok: {self.stok})"

#userrrrrrrrrrr
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(20), nullable=False, default="customer")

    def __init__(self, nama, role="customer"):
        self.nama = nama
        self.role = role

    def __repr__(self):
        return f"User({self.nama}, Role: {self.role})"

#Keranjangg
class KeranjangBelanja:
    def __init__(self):
        self.items = []

    def tambah_produk(self, produk, jumlah):
        if produk.stok >= jumlah:
            produk.stok -= jumlah
            self.items.append((produk, jumlah))
        else:
            print("Stok tidak cukup!")

    def total_harga(self):
        return sum(p.harga * j for p, j in self.items)

#Transaksi
class Transaksi:
    def __init__(self, user, keranjang):
        self.user = user
        self.keranjang = keranjang

    def checkout(self):
        return f"Total belanja {self.user.nama}: Rp{self.keranjang.total_harga()}"
