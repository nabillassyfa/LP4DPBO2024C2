

# Saya Nabilla Assyfa Ramadhani [2205297] 
# mengerjakan Latihan
# dalam mata Desain dan Pemograman Berorientasi Objek 
# untuk keberkahanNya maka saya tidak melakukan kecurangan 
# seperti yang telah dispesifikasikan. 
# Aamiin

# import library
from Motor import Motor
from Mobil import Mobil
from TempatParkir import TempatParkir

# variabel untuk menyimpan data kendaraan
tahun = 0           #variabel untuk menyimpan tahun produksi suatu kendaraan
kursi = 0           #variabel untuk menyimpan jumlah kursi yang dimiliki mobil
pintu = 0           #variabel untuk menyimpan jumlah pintu yang dimiliki mobil
nomorPlat =""        #variabel untuk menyimpan plat nomor yang dimiliki oleh kendaraan
merk=""              #variabel untuk menyimpan merk dari suatu kendaraan
warna=""             #variabel untuk menyimpan warna kendaraan
kapasitas_tangki ="" #variabel untuk menyimpan data kapasitas tangki suatu motor
jenis_motor =""      #variabel untuk menampung jenis motor

# menampilkan new line
print ()
print("        UNIVERSITAS PENDIDIKAN INDONESIA ")
print ()  # menampilkan new line

# Inisiasi tempat parkir
tempat = TempatParkir ("Parkiran Motor UPI", 100, 30, 35)
tempat_mobil = TempatParkir ("Parkiran Mobil UPI", 300, 30, 40) 

jenis = 0         # variabel untuk menyimpan masukan user untuk program yang dipilih
query = 0         # variabel untuk menjalankan query program

# Program input data
while (query != 1):
    # MENAMPILKAN MENU 
    print("================================================")
    print("*        Selamat datang di Parkiran UPI        *")
    print("================================================")
    print("  1. Pilih 1 untuk memasukan data parkir mobil " )
    print("  2. Pilih 2 untuk memasukan data parkir motor " )
    print("  3. Pilih 3 untuk mengeluarkan kendaraan      " )
    print("  4. Pilih 4 untuk menampilkan data parkiran   " )
    print("  5. Pilih 5 untuk Keluar dari program         " )
    print("================================================")
    
    print ()  # menampilkan new line
    
    # Meminta masukan user untuk program yang akan dijalankan
    print("Masukan nomor perintah :    ", end="")
    jenis = int (input ())

    print()

    # Memasukan data kendaraan dengan jenis mobil
    if (jenis == 1):
        print("*********** DATA MOBIL ************* ")
        print("Masukan nomor Plat Mobil   :  ", end="") # Masukan user untuk nomor plat mobil
        nomorPlat = str (input ())
        print("Masukan Merk Mobil         :  ", end="") # Masukan user untuk merk mobil
        merk  = str (input ())
        print("Masukan Tahun Produksi     :  ", end="") # Masukan user untuk tahun produksi
        tahun  = int (input ())
        print("Masukan Warna Mobil        :  ", end="") # Masukan user untuk warna mobil
        warna  = str (input ())
        print("Masukan Jumlah Pintu Mobil :  ", end="") # Masukan user untuk jumlah pintu mobil
        pintu  = int (input ())
        print("Masukan Jumlah Kursi Mobil :  ", end="") # Masukan user untuk jumlah kursi mobil
        kursi  = int (input ())
        print("************************************ ")

        tempat_mobil.kendaraanMasuk(1)  # menambah data kendaraan
        
        # kondisi jika tempat parkir telah penuh
        if (tempat_mobil.addMobil(Mobil (pintu, kursi, nomorPlat, merk, tahun, warna)) == 1):
            query = 1  #keluar dari program

        print()

    # Menambah data kendaraan dengan jenis motor
    elif (jenis == 2):
        print("************** DATA MOBIL **************** ")
        print("Masukan nomor Plat Motor       :  ", end="")  # Masukan user untuk nomor plat motor
        nomorPlat  = str (input ())
        print("Masukan Merk Motor             :  ", end="")  # Masukan user untuk merk motor
        merk  = str (input ())
        print("Masukan Tahun Produksi Motor   :  ", end="")  # Masukan user untuk tahun produksi
        tahun  = int (input ())
        print("Masukan Warna Motor            :  ", end="")  # Masukan user untuk warna motor
        warna  = str (input ())
        print("Masukan Kapasitas tangki motor :  ", end="")  # Masukan user kapasitas tangki motor
        kapasitas_tangki  = str (input ())
        print("Masukan Jenis Motor            :  ", end="")  # Masukan user jenis motor
        jenis_motor  = str (input ())
        print("*************************************** ")

        tempat.kendaraanMasuk(1)  # menambah data kendaraan
        
        # kondisi jika tempat parkir telah penuh
        if (tempat.addMotor(Motor(kapasitas_tangki, jenis, nomorPlat, merk, tahun, warna)) == 1):
            query = 1   #keluar dari program
       
        
        print()
    elif (jenis == 3):
        perintah =""
        while (perintah != "K"):
            print ("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
            print ("|   Selamat datang di Parkiran UPI      |")
            print ("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
            print ("| C : kendaraan yang keluar jenis mobil |")
            print ("| M : kendaraan yang keluar jenis motor |")
            print ("| K : Keluar/batal                      |")
            print ("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
            print ()  # menampilkan new line
            
            
            print("Masukan jenis kendaraan yang akan keluar :    ", end="")
            perintah = str (input ())               # masukan user untuk jenis kendaraan yang akan keluar
            print ()  # menampilkan new line
            
            if (perintah == "C"):       # kondisi jika kendaraan yang keluar adalah mobil
                print ("Masukan plat nomor mobil yang keluar :   ", end="")  # memasukan nomor plat kendaraan
                plat = str (input ())
                tempat_mobil.hapusMobil(plat)
            elif (perintah == "M"):      # kondisi jika kendaraan yang keluar adalah motor
                print ("Masukan plat nomor motor yang keluar :   ", end="")   # memasukan nomor plat kendaraan
                plat = str (input ())
                tempat.hapusMotor(plat)
    elif (jenis == 4):
        # panjang setiap kolom pada tabel
        lenPlat = 12
        lenwarna = 15
        lenMerk = 10
        lenKursi = 15
        lenPintu = 15
        lenTangki = 16
        lenJenis_Motor = 16
        lenTahun = 15
        
        tampilan =""   # variabel untuk menampung perintah user dalam program menampilkan data
        while (tampilan != "K"):
            print ("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
            print ("|   Selamat datang di Parkiran UPI      |")
            print ("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
            print ("| PC : Menampilkan data mobil           |")
            print ("| PM : Menampilkan data motor           |")
            print ("| K  : Keluar/batal                     |")
            print ("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
            print ()  # menampilkan new line
            
            print("Masukan jenis data yang ingin anda lihat :    ", end="")
            tampilan = str (input ())
            
            if (tampilan == "PC"):  # kondisi jika user ingin menampilkan data kendaraan dengan jenis mobil
                # Menampilkan informasi Parkiran
                print(("================================="))
                print("!      Informasi Parkiran       !" ) 
                print(("================================="))
                tempat_mobil.CetakParkiran()
                print(("================================="))
                print ()            # menampilkan newline
                print(" Data Kendaraan yang tersimpan" )
                print ()            # menampilkan newline



                # Menampilkan data mobil yang terparkir
                print("Data Mobil :")
                print ()  # menampilkan new line

                list = tempat_mobil.getMobil()

                if (len(list) == 0):   # kondisi jika list kosong
                    print("  ~~ Parkiran Kosong ~~ " )
                else:  # kondisi jika list tidak kosong
                    # Menampilkan garis
                    # mencetak garis tabel
                    print ("!-{}-!-{}-!-{}-!-{}-!-{}!-{}-!".format('-' * lenPlat, '-' * lenMerk, '-' * lenwarna, '-' * lenTahun, '-' * lenKursi, '-' * lenPintu))

                    # Menampilkan header tabel
                    print ("! {:<{}} ! {:<{}} ! {:<{}} ! {:<{}} ! {:<{}}! {:<{}} ! ".format("Nomor Plat" , lenPlat, "Merk" , lenMerk, "Warna" , lenwarna, "Tahun Produksi" , lenTahun, "Jumlah Kursi" , lenKursi, "Jumlah Pintu" , lenPintu))
                    
                    
                    # Menampilkan garis
                    print ("!-{}-!-{}-!-{}-!-{}-!-{}!-{}-!".format('-' * lenPlat, '-' * lenMerk, '-' * lenwarna, '-' * lenTahun, '-' * lenKursi, '-' * lenPintu))

                # menampilkan data 
                    for mobil in list:
                        print ("! {:<{}} ! {:<{}} ! {:<{}} ! {:<{}} ! {:<{}}! {:<{}} ! ".format(mobil.getPlat() , lenPlat, mobil.getMerk() , lenMerk, mobil.getWarna(), lenwarna, mobil.getTahun(), lenTahun, mobil.getJum_kursi(), lenKursi, mobil.getJum_pintu(), lenPintu))
                

                    # Menampilkan garis
                    print ("!-{}-!-{}-!-{}-!-{}-!-{}!-{}-!".format('-' * lenPlat, '-' * lenMerk, '-' * lenwarna, '-' * lenTahun, '-' * lenKursi, '-' * lenPintu))
                    
            elif (tampilan == "PM"):   # kondisi jika user ingin menampilkan data kendaraan dengan jenis motor
                print(("================================="))
                print("!      Informasi Parkiran       !" ) 
                print(("================================="))
                tempat.CetakParkiran()
                print(("================================="))
                
                print ()            # menampilkan newline
                print(" Data Kendaraan yang tersimpan" )
                print ()            # menampilkan newline
                
                # MENAMPILKAN DATA MOTOR YANG TERPARKIR
                print("Data Motor :")
                print ()  # menampilkan new line

                list2 = tempat.getMotor()

                if (len(list2) == 0):   # kondisi jika list kosong
                    print("  ~~ Parkiran Kosong ~~ " )
                else:  # kondisi jika list tidak kosong
                    # Menampilkan garis
                    # mencetak garis tabel
                    print ("!-{}-!-{}-!-{}-!-{}-!-{}!-{}-!".format('-' * lenPlat, '-' * lenMerk, '-' * lenwarna, '-' * lenTahun, '-' * lenJenis_Motor, '-' * lenTangki))

                    # Menampilkan header tabel
                    print ("! {:<{}} ! {:<{}} ! {:<{}} ! {:<{}} ! {:<{}} ! {:<{}} ! ".format("Nomor Plat" , lenPlat, "Merk" , lenMerk, "Warna" , lenwarna, "Tahun Produksi" , lenTahun, "Jenis Motor" , lenKursi, "Kapasitas tangki" , lenPintu))
                    
                    
                    # Menampilkan garis
                    print ("!-{}-!-{}-!-{}-!-{}-!-{}!-{}-!".format('-' * lenPlat, '-' * lenMerk, '-' * lenwarna, '-' * lenTahun, '-' * lenJenis_Motor, '-' * lenTangki))

                # menampilkan data 
                    for motor in list2:
                        print ("! {:<{}} ! {:<{}} ! {:<{}} ! {:<{}} ! {:<{}} ! {:<{}}  ! ".format(motor.getPlat() , lenPlat, motor.getMerk() , lenMerk, motor.getWarna(), lenwarna, motor.getTahun(), lenTahun, motor.getJenis(), lenKursi, motor.getKapasitas_tangki(), lenPintu))
                

                    # Menampilkan garis
                    print ("!-{}-!-{}-!-{}-!-{}-!-{}!-{}-!".format('-' * lenPlat, '-' * lenMerk, '-' * lenwarna, '-' * lenTahun, '-' * lenJenis_Motor, '-' * lenTangki))  
    else:
        query = 1
   

