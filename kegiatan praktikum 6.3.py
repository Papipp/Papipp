# 6.3.1 kegiatan praktikum 1: bekerja dengan list

bulan1 = ['januari','februari','maret','april','mei','juni']
bulan2 = ['juli','agustus','september','oktober','november','desember']

print('Jumlah elemen pada list bulan1 : ', len(bulan1))

tahun = bulan1 + bulan2
print('Jumlah elemen pada list tahun : ', len(tahun))
print(tahun)
print(tahun[2:5])
print(tahun[:6])
print(tahun[8:])
del tahun[2]
tahun.remove('desember')
print(tahun)
tahun.insert(2,'maret')
tahun.append('desember')
print(tahun)
tahun.reverse()
print(tahun) 

# 6.3.2 kegiatan praktikum 1: bekerja dengan Tupel
truk = ('hino', 3000, 2.5 , 130 )
merk, cc , berat , top_speed = truk
print(truk[0])
print(truk[:2])
print(truk[2:])
print(truk.index(3000))
print(2.5 in truk)
print('truk {} memiliki berat {} ton, kapasitas {} cc dan top speed {} km/jam'.
format(merk,berat,cc,top_speed))

# 6.3.3 kegiatan praktikum 1: bekerja dengan set
set_satu = {1,2,3}
set_dua = {4,5,6}
set_satu.add(4)
set_dua.add(7)
print(set_satu)
print(set_dua)
set_satu.update([5,6])
set_dua.update([8,9])
print(set_satu)
print(set_dua)
set_satu.discard(6)
set_dua.remove(4)
print(set_satu | set_dua)
print(set_satu & set_dua)
print(1 in set_satu) 

# 6.3.4 kegiatan praktikum 1: bekerja dengan Dictionaries
mahasiswa = {'nama':'Andika','umur':21}
mahasiswa['umur'] = 19
mahasiswa['alamat'] = 'Sragen'
mahasiswa['angkatan'] = 2020
print(mahasiswa)
print(mahasiswa.pop('angkatan'))
print(mahasiswa)
print('nama' in mahasiswa)
print(len(mahasiswa))
print(sorted(mahasiswa))
mahasiswa.clear()
print(mahasiswa)