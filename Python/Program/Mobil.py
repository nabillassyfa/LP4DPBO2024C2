

# Saya Nabilla Assyfa Ramadhani [2205297] 
# mengerjakan Latihan
# dalam mata Desain dan Pemograman Berorientasi Objek 
# untuk keberkahanNya maka saya tidak melakukan kecurangan 
# seperti yang telah dispesifikasikan. 
# Aamiin

from Kendaraan import Kendaraan 


class Mobil (Kendaraan):
    
    __jum_kursi = 0
    __jum_pintu = 0

    # Constructor

    def __init__ (self, jum_pintu, jum_kursi,  nomor_plat,  merk, tahun,  warna) : 
        super().__init__(nomor_plat, merk, tahun, warna)
        self.__jum_kursi = jum_kursi
        self.__jum_pintu = jum_pintu
    

    # Metode set dan get untuk atribut Mobil
    def setJum_kursi (self, kursi):
       self.__jum_kursi = kursi
    

    def getJum_kursi (self):
        return self.__jum_kursi
    

    def setJum_pintu (self, pintu):
       self.__jum_pintu = pintu
    

    def getJum_pintu (self):
        return self.__jum_pintu

    

