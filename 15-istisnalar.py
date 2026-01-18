#sayi1=input("Lütfen bir sayı giriniz...")
#sayi2=input("Lütfen bir sayı daha giriniz...")

#print(int(sayi1)+ int(sayi2))
import random
from random import randint

while True:
    try:

        sayi1=int(input("Lütfen bir sayı giriniz..."))
        sayi2=int(input("Lütfen bir sayı daha giriniz...") )
        print(sayi1+ sayi2)
        break
    except:
        print("Lütfen sayı girin....")
     
        

        # değişiklik yok diyor nasıl olur

        print(randint(0,3))
        
      


