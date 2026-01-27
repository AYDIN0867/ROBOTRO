def ekranaMerhabaYaz():
    print("Merhaba")

ekranaMerhabaYaz() #Merhaba

def ekranaYaz(cumle):
    print("Merhaba "+cumle)

ekranaYaz("Ramazan")#Merhaba Ramazan

def karesiAl(sayi:int)-> int:
    return sayi **2
print (karesiAl(123)) #15129 Tab scope u belirler ve çok önemlidir 
#Dikkat edilmelidir...



def defaultParametreAlanFonksiyon(isim="ramazan"):
    print(f"Merhaba {isim}")
defaultParametreAlanFonksiyon("Yusuf") #Merhaba Yusuf
defaultParametreAlanFonksiyon() #Merhaba ramazan

def sayilariTopal(sayi1,sayi2):
    print(sayi1+sayi2)

sayilariTopal(10,40)#50


def birden_cok_sayi_topla(*sayiar):
    toplam=0
    for s in sayiar:
        toplam+=s
    print(toplam) 

birden_cok_sayi_topla(10,20,30,5)#65 float olabilir ama double yok...        




