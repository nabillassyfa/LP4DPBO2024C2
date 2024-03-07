

# Saya Nabilla Assyfa Ramadhani [2205297] 
# mengerjakan Latihan
# dalam mata kuliah Desain dan Pemograman Berorientasi Objek 
# untuk keberkahanNya maka saya tidak melakukan kecurangan 
# seperti yang telah dispesifikasikan. 
# Aamiin

# import libarary
from Mobil import Mobil
from Motor import Motor

class TempatParkir :
    __nama_TempatParkir =""  # variabel untuk menampung tempat penyimpanan kendaraan
    __luas_TempatParkir = 0  # variabel untuk menampung luas tempat penyimpanan kendaraan
    __banyak_kendaraan = 0   # variabel untuk menampung banyak kendaraan yang terparkir
    __kapasitas= 0           # variabel untuk menampung total kapasitas kendaraan yang dapat ditampung
    
    # constructor
    def __init__ (self, nama_TempatParkir, luas_TempatParkir, banyak_kendaraan, kapasitas):
        self.__nama_TempatParkir = nama_TempatParkir
        self.__luas_TempatParkir = luas_TempatParkir
        self.__banyak_kendaraan = banyak_kendaraan
        self.__kapasitas = kapasitas
        self.Mobil = []   # array of object untuk menampung data mobil yang terparkir
        self.Motor = []   # array of object untuk menampung data motor yang terparkir
   

    # Metode get dan set untuk setiap atribut TempatParkir

    def setNama_TempatParkir (self, nama):
        self.__nama_TempatParkir = nama
   
    def getNama_TempatParkir (self):
        return self.__nama_TempatParkir
   

    def setluas_TempatParkir (self, luas):
        self.__luas_TempatParkir = luas
   
    def getluas_TempatParkir (self):
        return self.__luas_TempatParkir
   

    def setKapasitas (self, kapasitas):
        self.__kapasitas = kapasitas
   
    def getKapasitas (self):
        return self.__kapasitas
   

    def setJumKendaraan (self, banyak_kendaraan):
        self.__banyak_kendaraan = banyak_kendaraan
   
    def getJumKendaraan (self):
        return self.__banyak_kendaraan
   

    # Fungsi untuk menambah daftar kendaraan dengan jenis mobil
    def addMobil (self, Mobil):
        if (self.__banyak_kendaraan < self.__kapasitas):   # kondisi masih ada ruang untuk parkir kendaraan
            self.Mobil.append(Mobil)            # menambahkan data mobil ke array of object

            print ("  ~~ Data berhasil ditambahkan ~~  " )  
            return 0   # return true
        else:   # kondisi tidak ada tempat untuk parkir
            print ("WARNING! Tempat Parkir Sudah Penuh")
            return 1  # return false untuk keluar dari program
       
    # fungsi untuk mendapatkan data mobil
    def getMobil (self):
        return self.Mobil
   

      # Fungsi untuk menambah daftar kendaraan dengan jenis motor
    def addMotor (self, Motor):
        if (self.__banyak_kendaraan < self.__kapasitas):   # kondisi masih ada ruang untuk parkir kendaraan
            self.Motor.append(Motor)
            print ("  ~~ Data berhasil ditambahkan ~~  ")
            return 0
        else:
            print ("Tempat Parkir Sudah Penuh")
            return 1  # return false untuk keluar dari program
            
    def getMotor (self):
        return self.Motor
    
    def hapusMobil (self, id_mobil):
        indeks = 0
        ketemu = 0
        while ketemu == 0 and indeks < len (self.Mobil):
            hapus = self.Mobil [indeks]
            if hapus.getPlat() == id_mobil : # kondisi id yang akan di ubah ada di dalam data
                self.Mobil.remove(hapus)     # menghapus data mobil yang keluar
                print () #menampilkan newline
                print (" ~~~ Data berhasil dihapus !  ~~~" )
                
                print ("Jumlah Kendaraan awal : ", self.getJumKendaraan())
                self.__banyak_kendaraan = self.__banyak_kendaraan - 1
                print ("Jumlah kendaraan akhir : ", self.getJumKendaraan())
                print ()
                ketemu = 1
                
            # iterasi
            indeks+=1
                
        if ketemu == 0:
            print("Kendaraan dengan nomor plat '{}' tidak ditemukan".format(id_mobil))
            print ()
        
    def hapusMotor (self, id_motor):
        indeks = 0
        ketemu = 0
        while ketemu == 0 and indeks < len (self.Motor):
            hapus = self.Motor [indeks]
            if hapus.getPlat() == id_motor : # kondisi id yang akan di ubah ada di dalam data
                self.Motor.remove(hapus)
                print () #menampilkan newline
                print (" ~~~ Data berhasil dihapus !  ~~~" )
                
                print ("Jumlah Kendaraan awal : ", self.getJumKendaraan())
                self.__banyak_kendaraan = self.__banyak_kendaraan - 1
                print ("Jumlah kendaraan akhir : ", self.getJumKendaraan())
                print ()
                
                ketemu = 1
            # iterasi
            indeks+=1
        if ketemu == 0:
           print("Kendaraan dengan nomor plat '{}' tidak ditemukan".format(id_motor))
           print ()


    def kendaraanMasuk (self, tambah):
        self.__banyak_kendaraan = self.__banyak_kendaraan + tambah
    
    # prosedur untuk menampilkan data parkiran
    def CetakParkiran (self):
        print("Nama Parkiran      :", self.getNama_TempatParkir() ) 
        print("Luas Parkiran      :", self.getluas_TempatParkir() ) 
        print("Kapasitas Parkiran :", self.getKapasitas() )