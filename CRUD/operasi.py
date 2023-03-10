from . import database
import time
import random
import string

def createData(penulis,judul,tahun):
    
    data = database.TEMPLATE.copy()
    data['data_add'] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data['pk'] = "".join(random.choice(string.ascii_uppercase)for i in range(10))
    data['penulis'] = penulis + database.TEMPLATE['penulis'][len('penulis'):]
    data['judul'] = judul + database.TEMPLATE['judul'][len('judul'):]
    data['tahun'] = tahun

    dataStr = f"{data['data_add']},{data['pk']},{data['penulis']},{data['judul']},{data['tahun']}\n"

    try :
        with open(database.DBNAME,'a',encoding="utf-8") as file :
            file.write(dataStr)
    except :
        print("Data tidak bisa dibuat, database error")


def readData():
    try :
        with open(database.DBNAME,'r+') as file :
            content = file.readlines()
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
    data['penulis'] = penulis + database.TEMPLATE['penulis'][len('penulis'):]
    data['judul'] = judul + database.TEMPLATE['judul'][len('judul'):]
    data['tahun'] = tahun

    dataStr = f"{data['data_add']},{data['pk']},{data['penulis']},{data['judul']},{data['tahun']}\n"

    try :
        with open(database.DBNAME,'w',encoding="utf-8") as file :
            file.write(dataStr)
    except :
        print("Data tidak bisa dibuat, database error")

    