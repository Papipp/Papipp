from flask import Flask, render_template

class Product:
    def __init__(self, name, price, image, is_sale=False, old_price=None, rating=None):
        self.name = name
        self.price = price
        self.image = image
        self.is_sale = is_sale
        self.old_price = old_price
        self.rating = rating

# Data produk
products = [
    Product("Bergo Style", "Rp 120.000 - Rp 350.000", "https://github.com/Papipp/Papipp/blob/main/Gambar-krudung/hijab-bergo.jpg?raw=true"),
    Product("Special Item", "$18.00", "https://dummyimage.com/450x300/dee2e6/6c757d.jpg", is_sale=True, old_price="$20.00", rating=5),
    Product("Sale Item", "$25.00", "https://dummyimage.com/450x300/dee2e6/6c757d.jpg", is_sale=True, old_price="$50.00"),
    Product("Popular Item", "$40.00", "https://dummyimage.com/450x300/dee2e6/6c757d.jpg", rating=5),
]

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
