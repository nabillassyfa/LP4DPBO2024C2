

# Saya Nabilla Assyfa Ramadhani [2205297] 
# mengerjakan Latihan
# dalam mata Desain dan Pemograman Berorientasi Objek 
# untuk keberkahanNya maka saya tidak melakukan kecurangan 
# seperti yang telah dispesifikasikan. 
# Aamiin


class Kendaraan :
    __nomor_plat =""   # variabel untuk menampung nomor plat kendaraan
    __merk =""          # variabel untuk menampung merk kendaraan
    __tahun_produksi= 0 # variabel untuk menampung tahun produksi suatu kendaraan
    __warna=""          # variabel untuk menampung nama kendaraan
        
        
    #constructor
    def __init__(self, nomor_plat,  merk, tahun,  warna):
       self.__nomor_plat = nomor_plat
       self.__merk = merk
       self.__tahun_produksi = tahun
       self.__warna = warna
    

    # Metode get dan set untuk setiap atribut kendaraan
    
    # metode set plat
    def setPlat (self, nomor):
       self.__nomor_plat = nomor
    # metode get plat
    def getPlat (self):
        return self.__nomor_plat
    

    def setMerk (self, merk):
       self.__merk = merk
       
    def getMerk (self):
        return self.__merk
    

    def setTahun (self, tahun):
       self.__tahun_produksi = tahun
       
    def getTahun (self):
        return self.__tahun_produksi
    

    def setWarna (self, warna):
       self.__warna = warna
   
    def getWarna (self):
        return self.__warna

    


