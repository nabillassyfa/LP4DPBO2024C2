/*

Saya Nabilla Assyfa Ramadhani [2205297] 
mengerjakan Latihan
dalam mata Desain dan Pemograman Berorientasi Objek 
untuk keberkahanNya maka saya tidak melakukan kecurangan 
seperti yang telah dispesifikasikan. 
Aamiin

*/

// Menggunakan pragma once agar header file hanya di-include satu kali
#pragma once

// Memasukan library yang digunakan
#include <iostream>
#include <string>


// Deklarasi namespace
using namespace std;

class Kendaraan {
    private :
        string nomor_plat;
        string merk;
        int tahun_produksi;
        string warna;

    public :

    //constructor
    Kendaraan (){

    }

    Kendaraan (string nomor_plat, string merk, int tahun, string warna){
        this->nomor_plat = nomor_plat;
        this->merk = merk;
        this->tahun_produksi = tahun;
        this->warna = warna;
    }

    // Metode get dan set untuk setiap atribut kendaraan

    void setPlat (string nomor){
        this->nomor_plat = nomor;
    }

    string getPlat (){
        return this->nomor_plat;
    }

    void setMerk (string merk){
        this->merk = merk;
    }

    string getMerk (){
        return this->merk;
    }

    void setTahun (int tahun){
        this->tahun_produksi = tahun;
    }

    int getTahun (){
        return this->tahun_produksi;
    }

    void setWarna (string warna){
        this->warna = warna;
    }

    string getWarna (){
        return this->warna;
    }


    //Destreuctor
    ~Kendaraan (){

    }


};