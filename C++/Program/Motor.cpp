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

class Motor : public Kendaraan {
    private:
        string jenis_motor;
        string kapasitas_tangki;

    public:
    // Constructor
    Motor (){

    }

    Motor (string jenis, string kapasitas, string nomor_plat, string merk, int tahun, string warna) : Kendaraan(nomor_plat, merk, tahun, warna){
        this->jenis_motor = jenis;
        this->kapasitas_tangki = kapasitas;
    }

    // Metode set dan get untuk atribut motor
    void setJenis (string jenis){
        this->jenis_motor = jenis;
    }

    string getJenis (){
        return this->jenis_motor;
    }

    void setKapasitas_tangki (string tangki){
        this->kapasitas_tangki = tangki;
    }

    string getKapasitas_tangki (){
        return this->kapasitas_tangki;
    }

    // Destructor
    ~Motor (){

    }
};
