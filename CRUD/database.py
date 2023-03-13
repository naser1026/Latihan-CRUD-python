from . import operasi
import os

DBNAME = "data.txt"
TEMPLATE = {
    'data_add' : "yyyy-mm-dd",
    'pk' : "xxxxxx",
    'penulis' : " "*100,
    'judul' : " "*100,
    'tahun' : "yyyy"
}

def initConsole():
    try :
        with open(DBNAME, "r",encoding = "utf-8") as file :
            pass
        print("\nDatabase Tersedia")
        os.system("pause")
    except :
        print("\nDatabase tidak ditemukan silahkan membuat data baru\n")
        print("\n"+"-"*92)
        print("Masukan data buku")
        penulis = input("\nPenulis\t: ")
        judul = input("Judul\t: ")
        while True :
            try :
                tahun = int(input("Tahun\t: "))
                if len(str(tahun)) == 4 :
                    break
                else :
                    print("Tahun tidak valid (yyyy)")
            except :
                print("Tahun tidak valid (yyyy)")
        operasi.createData(penulis,judul,tahun)