class Product:
    def __init__(self, name, price, image_url, sale=False, rating=0):
        """
        Inisialisasi objek produk.

        :param name: Nama produk
        :param price: Harga produk (bisa dalam format range)
        :param image_url: URL gambar produk
        :param sale: Boolean apakah produk sedang diskon
        :param rating: Rating produk (0-5)
        """
        self.name = name
        self.price = price
        self.image_url = image_url
        self.sale = sale
        self.rating = rating

    def get_price_display(self):
        """Mengembalikan format harga produk, dengan harga diskon jika ada."""
        if isinstance(self.price, tuple):  # Jika harga adalah range (min, max)
            return f"Rp {self.price[0]:,} - Rp {self.price[1]:,}"
        return f"Rp {self.price:,}"

    def get_rating_stars(self):
        """Mengembalikan ikon bintang berdasarkan rating."""
        return "★" * self.rating + "☆" * (5 - self.rating)

# Contoh daftar produk untuk ditampilkan di toko
products = [
    Product("Bergo Style", (120000, 350000), 
            "https://github.com/Papipp/Papipp/blob/main/Gambar-krudung/hijab-bergo.jpg?raw=true", 
            sale=False, rating=4),
    Product("Special Item", 18000, "https://dummyimage.com/450x300/dee2e6/6c757d.jpg", 
            sale=True, rating=5),
    Product("Sale Item", 25000, "https://dummyimage.com/450x300/dee2e6/6c757d.jpg", 
            sale=True, rating=0),
    Product("Popular Item", 40000, "https://dummyimage.com/450x300/dee2e6/6c757d.jpg", 
            sale=False, rating=5),
    Product("Fancy Product", (120000, 280000), "https://dummyimage.com/450x300/dee2e6/6c757d.jpg", 
            sale=False, rating=3)
]
