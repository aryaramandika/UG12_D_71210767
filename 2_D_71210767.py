a = input("Hi Kiko, Silahkan Masukkan hari yang ingin Anda telusuri: ")
monday = ("kelas ke-1 Algorima Graf","kelas ke-3 Sistem Operasi","kelas ke-4 PAK")
tuesday = ("kelas ke-2 Matematika Teknik","kelas ke-4 Bhs Indonesia","kelas ke-6 PKN")
wednesday = ("kelas ke-2 Sistem Basis Data","kelas ke-4 Praktikum Sistem Basis Data")
thursday = ("kelas ke-1 IMK","kelas ke-3 LogMat","kelas ke-4 Praktekkom")

if a == "senin" :
    for i in range(len(monday)):
        print(monday[i])
elif a == "selasa" :
    for i in range(len(tuesday)):
        print(tuesday[i])
elif a == "rabu" :
    for i in range(len(wednesday)):
        print(wednesday[i])
elif a == "kamis" :
    for i in range(len(thursday)):
        print(thursday[i])
elif a == "jumat" :
    print("Hari Jumat Anda tidak ada kelas")