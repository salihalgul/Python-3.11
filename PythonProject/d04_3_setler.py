# Setler sadece bir grup veriyi tutar.
# Herhangi bir indexleri yoktur. Bütün veriler rastgele bir sıra ile saklanır
# Setler kendi içerisinde aynı veriyi birden fazla kere tutamaz
# Setler tuple gibi immutable yani değiştirilemezdir


ornek_set = {'Gece', 'Cengiz', 'Burhan', 'Pacchi', 'Pamuk', 'Sakız', 'Pacchi'}

print(ornek_set)

# Set içerisinden index ile bir şey çekmeye çalışırsak hata alırız
# print(ornek_set[2])

ornek_liste = ['ali', 'veli', 'mahmut', 'ali']
print(ornek_liste)

temizlenmis_liste = list(set(ornek_liste))
print(temizlenmis_liste)
