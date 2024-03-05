/*

Saya Nabilla Assyfa Ramadhani [2205297] 
mengerjakan Latihan
dalam mata Desain dan Pemograman Berorientasi Objek 
untuk keberkahanNya maka saya tidak melakukan kecurangan 
seperti yang telah dispesifikasikan. 
Aamiin

*/

// Deklarasi Library
#include <bits/stdc++.h>  // include semua library di cpp
#include "Mobil.cpp"
#include "Motor.cpp"
#include "TempatParkir.cpp"


using namespace std;

int main (){
    // variabel untuk menyimpan data kendaraan
    int tahun, kursi, pintu;
    string nomorPlat, merk, warna, kapasitas_tangki, jenis_motor; 

    cout << "\n";
    
    cout << "        UNIVERSITAS PENDIDIKAN INDONESIA" <<"\n\n";

    // Inisiasi tempat parkir
    TempatParkir tempat ("Parkiran UPI", 100, 30, 35); 

    int jenis = 0, query = 0;
    while (query != 1){
        cout << "================================================"<< endl;
        cout << "*        Selamat datang di Parkiran UPI        *" << endl;
        cout << "================================================"<< endl;
        cout << "  1. Pilih 1 untuk memasukan data parkir mobil " << endl;
        cout << "  2. Pilih 2 untuk memasukan data parkir motor " << endl;
        cout << "  2. Pilih 3 untuk Keluar dari program         " << endl;
        cout << "================================================"<< endl;

        cout << "Masukan nomor perintah :    ";
        cin >> jenis;

        cout << "\n";

        // Memasukan data kendaraan dengan jenis mobil
        if (jenis == 1){
            Mobil temp;
            cout << "*********** DATA MOBIL ************* "<< endl;
            cout << "Masukan nomor Plat Mobil   :  ";
            cin >> nomorPlat;
            cout << "Masukan Merk Mobil         :  ";
            cin >> merk;
            cout << "Masukan Tahun Produksi     :  ";
            cin >> tahun;
            cout << "Masukan Warna Mobil        :  ";
            cin >> warna;
            cout << "Masukan Jumlah Pintu Mobil :  ";
            cin >> pintu;
            cout << "Masukan Jumlah Kursi Mobil :  ";
            cin >> kursi;
            cout << "************************************ "<< endl;

            tempat.kendaraanMasuk(1);
            // menambah data kendaraan
            temp.setJum_kursi (kursi);
            temp.setJum_pintu (pintu);
            temp.setPlat (nomorPlat);
            temp.setMerk (merk);
            temp.setWarna (warna);
            temp.setTahun (tahun);

            if (tempat.addMobil(temp) == 1){
                query = 1;
            }

            cout << "\n";

        // Menambah data kendaraan dengan jenis motor
        } else if (jenis == 2){
            Motor temp;
            cout << "************** DATA MOBIL **************** "<< endl;
            cout << "Masukan nomor Plat Motor       :  ";
            cin >> nomorPlat;
            cout << "Masukan Merk Motor             :  ";
            cin >> merk;
            cout << "Masukan Tahun Produksi Motor   :  ";
            cin >> tahun;
            cout << "Masukan Warna Motor            :  ";
            cin >> warna;
            cout << "Masukan Kapasitas tangki motor :  ";
            cin >> kapasitas_tangki;
            cout << "Masukan Jenis Motor            :  ";
            cin >> jenis_motor;
            cout << "*************************************** "<< endl;

            tempat.kendaraanMasuk(1);
            
            temp.setKapasitas_tangki (kapasitas_tangki);
            temp.setJenis (jenis_motor);
            temp.setPlat (nomorPlat);
            temp.setMerk (merk);
            temp.setWarna (warna);
            temp.setTahun (tahun);

            if (tempat.addMotor(temp) == 1){
                query = 1;
            }
            
            cout << "\n";
        }else{
            query = 1;
        }
    }


    // Menampilkan informasi Parkiran
    cout << ("=================================")<< endl;
    cout << "!      Informasi Parkiran       !" << endl; 
    cout << ("=================================")<< endl;
    cout << "Nama Parkiran      :" << tempat.getNama_TempatParkir() << endl; 
    cout << "Luas Parkiran      :" << tempat.getluas_TempatParkir() << endl; 
    cout << "Kapasitas Parkiran :" << tempat.getKapasitas() << endl;
    cout << ("=================================")<< "\n\n";

    cout << "       Data Kendaraan yang tersimpan" << "\n\n";

    // panjang setiap kolom pada tabel
    int lenPlat = 12, lenwarna = 15, lenMerk = 10, lenKursi = 15, lenPintu = 15, lenTangki = 17, lenJenis_Motor = 16, lenTahun = 15;

    // Menampilkan data mobil yang terparkir
    cout << "Data Mobil :"<<endl;
    
    list <Mobil>list = tempat.getMobil();
    if (list.empty ()){   // kondisi jika list kosong
        cout << "  ~~ Parkiran Kosong ~~ " << "\n\n";
    }else{  // kondisi jika list tidak kosong
        // Menampilkan garis
        cout << "!-" << string(lenPlat, '-') << "-!-" << string(lenMerk, '-') << "-!-" << string(lenwarna, '-') << "-!-" << string(lenTahun, '-') << "-!-" << string(lenKursi, '-') << "-!-" << string(lenPintu, '-') << "!" << endl;

        // Menampilkan header tabel
        cout << "! " << left << setw(lenPlat) << "Nomor Plat" << " ! " << left << setw(lenMerk) << "Merk" << " ! " << left << setw(lenwarna) << "Warna" << " ! " << left << setw(lenTahun) << "Tahun Produksi" << " ! " << left << setw(lenKursi) << "Jumlah Kursi" << " ! " << left << setw(lenPintu) << "Jumlah Pintu" << "!" << endl;

        // Menampilkan garis
        cout << "!-" << string(lenPlat, '-') << "-!-" << string(lenMerk, '-') << "-!-" << string(lenwarna, '-') << "-!-" << string(lenTahun, '-') << "-!-" << string(lenKursi, '-') << "-!-" << string(lenPintu, '-') << "!" << endl;

        for (auto it = list.begin (); it != list.end(); it++){
            cout << "! " << setw(lenPlat) << it->getPlat() << " ! " << setw(lenMerk) << it->getMerk() << " ! " << setw(lenwarna) << it->getWarna() << " ! " << setw(lenTahun) << it->getTahun() << " ! " << setw(lenKursi) << it->getJum_kursi() << " ! " << setw(lenPintu) << it->getJum_pintu() << "! " << endl;
        }

        // Menampilkan garis
        cout << "!-" << string(lenPlat, '-') << "-!-" << string(lenMerk, '-') << "-!-" << string(lenwarna, '-') << "-!-" << string(lenTahun, '-') << "-!-" << string(lenKursi, '-') << "-!-" << string(lenPintu, '-') << "!" << "\n\n";
    }

    // MENAMPILKAN DATA MOTOR YANG TERPARKIR
    cout << "Data Motor :"<<endl;

    std:: list <Motor>list2 = tempat.getMotor();
    if (list2.empty ()){   // kondisi jika list kosong
        cout << "  ~~ Parkiran Kosong ~~ " << endl;
    }else{  // kondisi jika list tidak kosong
        // Menampilkan garis
        cout << "!-" << string(lenPlat, '-') << "-!-" << string(lenMerk, '-') << "-!-" << string(lenwarna, '-') << "-!-" << string(lenTahun, '-') << "-!-" << string(lenJenis_Motor, '-') << "-!-" << string(lenTangki, '-') << "!" << endl;

        // Menampilkan header tabel
        cout << "! " << left << setw(lenPlat) << "Nomor Plat" << " ! " << left << setw(lenMerk) << "Merk" << " ! " << left << setw(lenwarna) << "Warna" << " ! " << left << setw(lenTahun) << "Tahun Produksi" << " ! " << left << setw(lenJenis_Motor) << "Jenis Motor" << " ! " << left << setw(lenTangki) << "Kapasitas Tangki" << "!" << endl;

        // Menampilkan garis
        cout << "!-" << string(lenPlat, '-') << "-!-" << string(lenMerk, '-') << "-!-" << string(lenwarna, '-') << "-!-" << string(lenTahun, '-') << "-!-" << string(lenJenis_Motor, '-') << "-!-" << string(lenTangki, '-') << "!" << endl;

        

        for (auto it = list2.begin (); it != list2.end(); it++){
            cout << "! " << setw(lenPlat) << it->getPlat() << " ! " << setw(lenMerk) << it->getMerk() << " ! " << setw(lenwarna) << it->getWarna() << " ! " << setw(lenTahun) << it->getTahun() << " ! " << setw(lenJenis_Motor) << it->getJenis() << " ! " << setw(lenTangki) << it->getKapasitas_tangki() << "!" << endl;
        }

        // Menampilkan garis
        cout << "!-" << string(lenPlat, '-') << "-!-" << string(lenMerk, '-') << "-!-" << string(lenwarna, '-') << "-!-" << string(lenTahun, '-') << "-!-" << string(lenJenis_Motor, '-') << "-!-" << string(lenTangki, '-') << "!" << endl;
    }
    

    return 0;
}