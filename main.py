import os
import CRUD as CRUD
os.system("cls")
print("========================================================")
print("SELAMAT DATANG DIPROGRAM DATABASE PERPUSTAKAAN SEDERHANA")
print("--------------created by Naser Setiawan-----------------")
CRUD.initConsole()

while True : 
    os.system("cls")
    print("========================================================")
    print("--------------created by Naser Setiawan-----------------")
    print("SELAMAT DATANG DIPROGRAM DATABASE PERPUSTAKAAN SEDERHANA\n")
    print("1.Read Data")
    print("2.Create Data")
    print("3.Update Data")
    print("4.Delete Data")
    while True :
        try : 
            user_option = int(input("Pilih Opsi\t: "))
            if user_option <= 4 :
                break
            print("Opsi tidak valid (1,2,3,4) ")
        except :
            print("Opsi tidak valid (1,2,3,4) ")

    match user_option :
        case 1 : CRUD.readConsole()
        case 2 : CRUD.createConsole()
        case 3 : CRUD.updateConsole()
        case 4 : print("DELETE")
    
    while True :
        try :
            is_lanjut = str.lower(input("Apakah Sudah Selesai (y/n)? "))
            if is_lanjut == "y" or is_lanjut == "n" :
                break
            else :
                print("Jawaban tidak valid")
        except :
            print("Jawaban tidak valid")
    if is_lanjut == "y" :
        break



