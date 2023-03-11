from . import database,operasi


def deleteConsole():
	readConsole()
	jumlahBuku = operasi.readData(jmlhBuku = True)
	print(jumlahBuku)
	while True :
		while True :
			try :
				noBuku = int(input(f"Pilih buku yang akan dihapus\t: "))
				if noBuku > 0 and noBuku <= jumlahBuku :
					break
				else :
					print(f"No buku tidak ditemukan (1 - {jumlahBuku})")
			except :
				print("Pilihan harus angka")
		
		dataBuku = operasi.readData(index = noBuku - 1)
		dataBreak = dataBuku.split(",")
		dataAdd = dataBreak[0]
		pk = dataBreak[1]
		penulis = dataBreak[2]
		judul = dataBreak[3]
		tahun = dataBreak[4][:-1]
		print("="*92)
		print(f"\n1.Penulis\t: {penulis:.20}\n2.Judul\t\t: {judul:.20}\n3.Tahun\t\t: {tahun:.4}")
		print("-"*92)
		while True : 
			try :
				isDone = str.lower(input("\nApakah yakin akan dihapus (y/n)? "))
				if isDone == "n" or isDone == "y" :
					break
				else :
					print("Jawaban tidak valid")
			except :
				print("Jawaban harus huruf")
		if isDone == "y" :
			break
	operasi.deleteData(noBuku)





def updateConsole() :
	jumlahBuku = operasi.readData(jmlhBuku = True)
	readConsole()
	while True :
		try :
			noBuku = int(input(f"Pilih buku yang akan diupdate\t: "))
			if noBuku > 0 and noBuku <= jumlahBuku :
				break
			else :
				print(f"No buku tidak ditemukan (1 - {jumlahBuku})")
		except :
			print("Pilihan harus angka")
	dataBuku = operasi.readData(index = noBuku - 1)
	dataBreak = dataBuku.split(",")
	dataAdd = dataBreak[0]
	pk = dataBreak[1]
	penulis = dataBreak[2]
	judul = dataBreak[3]
	tahun = dataBreak[4][:-1]

	print(f"\n1.Penulis\t: {penulis:.20}\n2.Judul\t\t: {judul:.20}\n3.Tahun\t\t: {tahun:.4}")
	while True :
		while True :
			try :
				pilihNo = int(input('Pilih data yang akan diubah (1,2,3)\t: '))
				print("-"*92)
				if pilihNo <= 3 and pilihNo > 0 :
					break
				else :
					print("Pilihan tidak sesuai")
			except :
				print("Pilihan harus angka")
		match pilihNo :
			case 1 : penulis = input("Penulis\t: ")
			case 2 : judul = input("Judul\t: ")
			case 3 :
				while True :
					try :
						tahun = int(input("Tahun\t: "))
						if len(str(tahun)) == 4 :
						    break
						else :
						    print("Tahun tidak valid (yyyy)")
					except :
						print("Tahun tidak valid (yyyy)")
		
		print("-"*92)	
		print("\nData berhasil diupdate")
		print(f"1.Penulis\t: {penulis:.20}\n2.Judul\t\t: {judul:.20}\n3.Tahun\t\t: {str(tahun):.4}")

		while True : 
			try :
				isDone = str.lower(input("Apakah data sudah sesuai (y/n)? "))
				if isDone == "n" or isDone == "y" :
					break
				else :
					print("Jawaban tidak valid")
			except :
				print("Jawaban harus huruf")
		if isDone == "y" :
			break
	operasi.updateData(noBuku,dataAdd,pk,penulis,judul,tahun)

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
	print("\n"+"-"*92)

def createConsole():
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

