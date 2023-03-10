from . import operasi

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
        with open (DBNAME,'r') as file :
            file.read(DBNAME)
    except :
        print("\nDatabase tidak ditemukan silahkan membuat data baru\n")
        operasi.createFirstData()