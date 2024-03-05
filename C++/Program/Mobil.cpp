/*

Saya Nabilla Assyfa Ramadhani [2205297] 
mengerjakan Latihan
dalam mata Desain dan Pemograman Berorientasi Objek 
untuk keberkahanNya maka saya tidak melakukan kecurangan 
seperti yang telah dispesifikasikan. 
Aamiin

*/
#pragma once

// Memasukan library yang digunakan
#include <iostream>
#include <string>
#include "Kendaraan.cpp"


// Deklarasi namespace
using namespace std;

class Mobil : public Kendaraan {
    private:
        int jum_kursi;
        int jum_pintu;

    public:
    // Constructor
    Mobil (){

    }

    Mobil (int jum_pintu, int jum_kursi, string nomor_plat, string merk, int tahun, string warna) : Kendaraan(nomor_plat, merk, tahun, warna){
        this->jum_kursi = jum_kursi;
        this->jum_pintu = jum_pintu;
    }

    // Metode set dan get untuk atribut Mobil
    void setJum_kursi (int kursi){
        this->jum_kursi = kursi;
    }

    int getJum_kursi (){
        return this->jum_kursi;
    }

    void setJum_pintu (int pintu){
        this->jum_pintu = pintu;
    }

    int getJum_pintu (){
        return this->jum_pintu;
    }

    // Destructor
    ~Mobil (){

    }
};
