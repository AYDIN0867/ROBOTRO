myList=["Yusuf",39,True,5.9]
print(myList)
print(type(myList)) #<class 'list'>
print(type(myList[0]))#<class 'str'>
print(type(myList[1]))#<class 'int'>
print(type(myList[2]))#class 'bool'>
print(type(myList[3]))#class 'float'>

myList.append("Wise Quarter")
print(myList)
myList.append(42)
myList.append(False)
print(myList)

if 42 in myList:
    print("Evet, gercekten var")
else:
    print("Hayir, kesinlikle yok")
    #Evet, gercekten var
nums=[1, 10 , 5 , 8]

print(sorted(nums)) #[1, 5, 8, 10]
  
del myList[2]

print(myList)

yeniListe=list(range(10,50))
print(yeniListe)


urunler=["Bilgisayar","Zil","Laptop","Monitor"]
print(sorted(urunler)) #['Bilgisayar', 'Laptop', 'Monitor', 'Zil']

yeniUrunler=[]
print(type(yeniUrunler))
yepYeniürünler=list()
print(type(yepYeniürünler))






