from flask import Flask, render_template, request, redirect, url_for
from models import db, Produk, User

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# Buat database pertama kali
with app.app_context():
    db.create_all()

@app.route("/")
def index():
    produk_list = Produk.query.all()
    return render_template("index.html", produk_list=produk_list)

@app.route("/tambah_produk", methods=["POST"])
def tambah_produk():
    nama = request.form["nama"]
    harga = float(request.form["harga"])
    stok = int(request.form["stok"])

    produk_baru = Produk(nama, harga, stok)
    db.session.add(produk_baru)
    db.session.commit()

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
