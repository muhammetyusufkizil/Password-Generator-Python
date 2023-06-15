# Rastgele modülünü içe aktaralım
import random

# Şifrede kullanılacak karakterleri tanımlayalım
harfler = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
rakamlar = "0123456789"
semboller = "!@#$%^&*()_+-=[]{};:,./<>?"

# Kullanıcıdan şifrenin uzunluğunu ve karakter türlerini girmesini isteyelim
uzunluk = int(input("Şifrenizin uzunluğunu giriniz: "))
harf_sayisi = int(input("Şifrenizde kaç harf olsun? "))
rakam_sayisi = int(input("Şifrenizde kaç rakam olsun? "))
sembol_sayisi = int(input("Şifrenizde kaç sembol olsun? "))

# Şifreyi oluşturmak için boş bir liste tanımlayalım
sifre = []

# Rastgele harfler seçelim ve listeye ekleyelim
for i in range(harf_sayisi):
  sifre.append(random.choice(harfler))

# Rastgele rakamlar seçelim ve listeye ekleyelim
for i in range(rakam_sayisi):
  sifre.append(random.choice(rakamlar))

# Rastgele semboller seçelim ve listeye ekleyelim
for i in range(sembol_sayisi):
  sifre.append(random.choice(semboller))

# Listeyi karıştıralım
random.shuffle(sifre)

# Listeyi birleştirerek şifreyi oluşturalım
sifre = "".join(sifre)

# Şifreyi ekrana yazdıralım
print("Oluşturduğunuz şifre: " + sifre)
