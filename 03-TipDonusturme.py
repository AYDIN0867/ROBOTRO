sayi1="10"
sayi2=20

print(type(sayi1))#<class 'str'>
print(type(sayi2))#<class 'int'>

int(sayi1)#10
float(sayi1)#10.0
str(sayi2)
print("------------------------------------")
print(type(int(sayi1)))#<class 'int'>
print(type(float(sayi1)))#<class 'float'>     
print(type(str(sayi2)))#<class 'str'>



print((int(sayi1)))#10
print((float(sayi1)))#  10.0  
print((str(sayi2)))#20


isim="Yusuf"
yas=39
#print("Merhaba benim adim :"+isim+" ve yasim :"+yas)#Hata verir cunku yas int tipindedir str ilebirleştirilmeliddir
print("Merhaba benim adim :"+isim+" ve yasim :"+str(yas))#Doğru kullanım
print(f"Merhaba benim ismim {isim}\n Benim yasim {yas}")#f string kullanımı

