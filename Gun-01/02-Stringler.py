metin="Merhaba Dunya!!!!"
yeniDefgisken=metin.split()#Liste verir==>['Merhaba', 'Dunya!!!!']
print(yeniDefgisken)
print(type(yeniDefgisken))# type fonksiyonu ile deişkenin tipini öğrenziriz
print(metin.upper())



print(metin.replace("M","Y"))

#Class içinde olmayan metodlara fonksiyon denir.
#metodlarla fonksiyonlar arasındaki fark nedir?
#metodlar class içinde tanımlanır.
#Script dillerde class yapısı zorunlu değildir.

#Python'da herşey bir classdır.

metin=metin.lower()

print(metin) #merhaba dunya!!!!
print(metin[0])
#metin(baslangıc:bitis:kacarKacar)
print(metin[0:10:2]) #mraad
#iki nokta üst üste kullanılmazsa içine yazılan
#indeks yazılır
print(metin[:6]) #merhaba
print(metin[8:]) #dunya!!!!

print(len(metin))#17#len fonksiyonu metin içindeki karakter sayısını verir

#sonEleman=len(metin)-1
#print(metin[sonEleman])#!
print(metin[-1])#!#negatif indeksleme son elemanı verir


print(metin[::-1])
#!!!!aynud abahrem

