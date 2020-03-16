found = False

percobaan = 1
tebakan   = 500
listTebakan = [500, 250, 125, 63, 32, 16, 8, 4, 2, 1]

def ketemu():
    global found
    print("Yeay! Aku berhasil menemukan angka kamu! Angkamu pasti:", tebakan, "(jangan bohong ya! :p)")
    found = True


def lebihBesar():
    global percobaan, tebakan
    tebakan += listTebakan[percobaan]
    percobaan += 1

    if(tebakan == 1000):
        print("Wah Sudah hampir melewati batas!")
        ketemu()

    if(percobaan == 10): ketemu()

def lebihKecil():
    global percobaan, tebakan
    tebakan -= listTebakan[percobaan]
    percobaan+=1

    if(tebakan == 0):
        print("Wah Sudah hampir melewati batas!")
        ketemu()

    if(percobaan == 10): ketemu()



while(not(found)):

    print("Percobaan ke - ", percobaan, end=" \n")
    
    if(percobaan < 1):
        print("Silahkan pilih angka antara 0 - 1000", end="\n")
        print("Aku akan menebaknya dalam maks. 10 tebakan!", end="\n")
    
    
    print("Apakah angka kamu", tebakan, " ?")

    # print("note : h=lebih besar | l=lebih kecil")
    check = input("Jawabanmu? (h/l) = ")
    
    if(percobaan == 10): ketemu()

    if(check == 'h'): lebihBesar()
    elif(check == 'l'): lebihKecil()
    else:print("command not found!")

    print("\n\n")