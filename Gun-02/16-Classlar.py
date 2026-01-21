class Insan():
  
   def __init__(self,isim :str,soyisim : str,yas :int): #self=this init de constructor
    self.isim=isim
    self.soyisim=soyisim
    self.yas=yas
       
   def bilgileriYaz(self):
       print(f"Kullanıcının ad : {self.isim} {self.soyisim}. Yasi{self.yas}" ) 


   
   def __len__(self):
      return self.yas


insan=Insan("Yusuf","Kurnaz",39)
insan.bilgileriYaz() 

metin="Hello Cuma"

print(len(insan))

