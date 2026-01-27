isimler=["Yusuf","Ahmet","Mehmet","Yunus"]

def kontrol(degisken):
        return 'u' in degisken
    
print(list(map(kontrol,isimler)))
#[True, False, False,True]
print("#############################3")
print(list(filter(kontrol,isimler)))
#['Yusuf', 'Yunus']
#fonksiyonlar kullnaılackken () yazılmaz....




