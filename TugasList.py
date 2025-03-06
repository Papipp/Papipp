#Daftar penumpang yang ingin berlibur
penumpang = ["William", "Kate", "Anderson", "Jame", "Mady", ]

#Jones ikut bergabung
penumpang.append("Jones")
print("orang yang ada didalam kereta :", penumpang)

# c) Mengganti "Anderson" dengan "Grace"
index_anderson = penumpang.index("Anderson")
penumpang[index_anderson] = "Grace"
print("penumpang ketika Grace diagntikan :", penumpang)

# d) Memeriksa apakah ada orang yang bernama "Thompson"
ada_thompson = "Thompson" in penumpang

# e) Mengurutkan list sesuai nama orang
penumpang.sort()

# f) Menampilkan siapa saja 6 orang tersebut menggunakan perulangan
print("Daftar penumpang yang berlibur ke Yogyakarta:")
for orang in penumpang:
    print(orang)

# g) Mengosongkan list secara keseluruhan
penumpang.clear()

# Menampilkan hasil pemeriksaan
print("\nApakah ada penumpang bernama 'Thompson'? :", ada_thompson)
print("Daftar penumpang setelah perjalanan:", penumpang)