from . import database
import time
import random
import string
import os

def deleteData(noBuku):
    try :
        with open(database.DBNAME,"r") as file :
            counter = 0
            while True :
                content = file.readline()
                if len(content) == 0 :
                    break
                elif counter == (noBuku - 1) :
                    pass
                else :
                    with open("dataTemp.txt","a", encoding = "utf-8") as tempFile :
                        tempFile.write(content)
                counter += 1
    except :
        print("Tidak bisa menghapus data, database error")
    os.remove(database.DBNAME)
    os.rename("dataTemp.txt",database.DBNAME)



def updateData(noBuku,dataAdd,pk,penulis,judul,tahun):

    data = database.TEMPLATE.copy()
    data['data_add'] = dataAdd
    data['pk'] = pk
    data['penulis'] = penulis + (" "*(len(database.TEMPLATE['penulis']) - len(penulis)) )
    data['judul'] = judul + (" "*(len(database.TEMPLATE['judul']) - len(judul)) )
    data['tahun'] = tahun

    dataStr = f"{data['data_add']},{data['pk']},{data['penulis']},{data['judul']},{data['tahun']}\n"
    panjangData = len(dataStr)
    dataSeek = panjangData * (noBuku - 1) + (noBuku-1)
    try :
        with open(database.DBNAME, "r+", encoding = "utf-8") as file :
            file.seek(dataSeek)
            file.write(dataStr)
    except :
        print("Data tidak bisa diubah, database error")
    os.system("cls")
    print("\n\n==========Data berhasil diupdate==========")
    os.system("pause")
def createData(penulis,judul,tahun):
    
    data = database.TEMPLATE.copy()
    data['data_add'] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data['pk'] = "".join(random.choice(string.ascii_uppercase)for i in range(10))
    data['penulis'] = penulis + (" "*(len(database.TEMPLATE['penulis']) - len(penulis)) )
    data['judul'] = judul + (" "*(len(database.TEMPLATE['judul']) - len(judul)) )
    data['tahun'] = tahun

    dataStr = f"{data['data_add']},{data['pk']},{data['penulis']},{data['judul']},{data['tahun']}\n"

    try :
        with open(database.DBNAME,'a',encoding="utf-8") as file :
            file.write(dataStr)
    except :
        print("Data tidak bisa dibuat, database error")


def readData(**kwargs):
    try :
        with open(database.DBNAME,'r+') as file :
            content = file.readlines()
            jumlahBuku = len(content)
            if "jmlhBuku" in kwargs :
                return jumlahBuku
            if "index" in kwargs :
                return content[kwargs["index"]]
            else :
                return content
    except :
        print("Data tidak dapat dibaca, database error")

def createFirstData():
    penulis = input("Penulis\t: ")
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
    data = database.TEMPLATE.copy()
    data['data_add'] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data['pk'] = "".join(random.choice(string.ascii_uppercase)for i in range(10))
    data['penulis'] = penulis + (" "*(len(database.TEMPLATE['penulis']) - len(penulis)) )
    data['judul'] = judul + (" "*(len(database.TEMPLATE['judul']) - len(judul)) )
    data['tahun'] = tahun

    dataStr = f"{data['data_add']},{data['pk']},{data['penulis']},{data['judul']},{data['tahun']}\n"

    try :
        with open(database.DBNAME,'w',encoding="utf-8") as file :
            file.write(dataStr)
    except :
        print("Data tidak bisa dibuat, database error")