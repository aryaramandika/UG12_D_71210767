bil1 = int(input("Masukkan awal deret : "))
bil2 = int(input("Masukkan akhir deret : "))
x = []
if (bil1 + 1) % 2 == 0:
     for i in range (bil1+1,bil2,2):
         if i % 3 == 0 or i % 7 == 0: continue
         print ( i , end = " " )
else:
     for i in range (bil1 , bil2 , 2):
         if i % 3 == 0 or i % 7 == 0 : continue
         print (i , end = " ")