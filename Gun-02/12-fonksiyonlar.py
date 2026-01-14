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
defaultParametreAlanFonksiyon()




