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
#include <bits/stdc++.h>  
#include <string>
#include "Motor.cpp"
#include "Mobil.cpp"


// Deklarasi namespace
using namespace std;

class TempatParkir {
    private :
        string nama_TempatParkir;
        int luas_TempatParkir;
        int banyak_kendaraan;
        int kapasitas;
        // List untuk menampung data kendaraan yang terparik dengan jenis mobil dan motor
        list <Mobil> Daftar_Mobil;
        list <Motor> Daftar_Motor;

    public :

    //constructor
    TempatParkir (){

    }

    TempatParkir (string nama_TempatParkir, int luas_TempatParkir, int banyak_kendaraan, int kapasitas){
        this->nama_TempatParkir = nama_TempatParkir;
        this->luas_TempatParkir = luas_TempatParkir;
        this->banyak_kendaraan = banyak_kendaraan;
        this->kapasitas = kapasitas;
    }

    // Metode get dan set untuk setiap atribut TempatParkir

    void setNama_TempatParkir (string nama){
        this->nama_TempatParkir = nama;
    }

    string getNama_TempatParkir (){
        return this->nama_TempatParkir;
    }

    void setluas_TempatParkir (int luas){
        this->luas_TempatParkir = luas;
    }

    int getluas_TempatParkir (){
        return this->luas_TempatParkir;
    }

    void setKapasitas (string daftar_kendaraan){
        this->kapasitas = kapasitas;
    }

    int getKapasitas (){
        return this->kapasitas;
    }

    void setJumKendaraan (string daftar_kendaraan){
        this->banyak_kendaraan = banyak_kendaraan;
    }

    int getJumKendaraan (){
        return this->banyak_kendaraan;
    }

    // Fungsi untuk menambah daftar kendaraan dengan jenis mobil
    int addMobil (Mobil mobil){
        if (this->banyak_kendaraan < this->kapasitas){
            this->Daftar_Mobil.push_back(mobil);

            cout << "  ~~ Data berhasil ditambahkan ~~  " <<endl;
            return 0;
        }else{
            cout << "WARNING! Tempat Parkir Sudah Penuh" <<endl;
            return 1;
        }
    }

    list <Mobil> getMobil (){
        return this->Daftar_Mobil;
    }

      // Fungsi untuk menambah daftar kendaraan dengan jenis motor
    int addMotor (Motor motor){
        if (this->banyak_kendaraan < this->kapasitas){
            this->Daftar_Motor.push_back(motor);
            cout << "  ~~ Data berhasil ditambahkan ~~  " <<endl;
            return 0;
        }else{
            cout << "Tempat Parkir Sudah Penuh" <<endl;
            return 1;
            
        }
    }

    list <Motor> getMotor (){
        return this->Daftar_Motor;
    }

    void kendaraanMasuk (int tambah){
        this->banyak_kendaraan = this->banyak_kendaraan + tambah;
    }

    //Destreuctor
    ~TempatParkir (){

    }


};