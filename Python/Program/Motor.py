

# Saya Nabilla Assyfa Ramadhani [2205297] 
# mengerjakan Latihan
# dalam mata Desain dan Pemograman Berorientasi Objek 
# untuk keberkahanNya maka saya tidak melakukan kecurangan 
# seperti yang telah dispesifikasikan. 
# Aamiin

from Kendaraan import Kendaraan

class Motor (Kendaraan) :
    __jenis_motor =""
    __kapasitas_tangki=""

    
    # Constructor

    def __init__(self,jenis,  kapasitas,  nomor_plat,  merk,  tahun,  warna) :
        super().__init__(nomor_plat, merk, tahun, warna)
        self.__jenis_motor = jenis
        self.__kapasitas_tangki = kapasitas
    

    # Metode set dan get untuk atribut motor
    def setJenis (self, jenis):
       self.__jenis_motor = jenis
    

    def getJenis (self):
        return self.__jenis_motor
    

    def setKapasitas_tangki (self, tangki):
       self.__kapasitas_tangki = tangki
    

    def getKapasitas_tangki (self):
        return self.__kapasitas_tangki

