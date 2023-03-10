from . import database,operasi

def readConsole():
	# Header
	index = "NO"
	nama = "NAMA"
	judul = "JUDUL"
	tahun = "TAHUN"
	print("\n"+"="*92)
	print(f"{index:3}|{nama:40}|{judul:40}|{tahun:5}|")
	print("-"*92)

	# Isi Data
	dataFile = operasi.readData()
	for index,data in enumerate(dataFile) :
		dataBreak = data.split(",")
		DATAADD = dataBreak[0]
		PK = dataBreak[1]
		PENULIS = dataBreak[2]
		JUDUL = dataBreak[3]
		TAHUN = dataBreak[4][:-1]
		print(f"{index+1:<3}|{PENULIS:.40}|{JUDUL:.40}|{TAHUN:5}|")
	# Footer
	print("\n\n"+"-"*92)

def createConsole():
	print("Masukan data buku")
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
	operasi.createData(penulis,judul,tahun)

