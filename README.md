Saya Nabilla Assyfa Ramadhani [2205297] mengerjakan Latihan dalam mata kuliah Desain dan Pemograman Berorientasi Objek untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin

<br><br>
# Desain Kelas
### Hierarchical Inheritance
 ![alt text](https://github.com/nabillassyfa/LP4DPBO2024C2/blob/main/Diagram.jpg)<br>
 Car and motorcycle is a vehicle. Kelas motor dan mobil memiliki inheritance dengan kelas kendaraan, karena mobil dan motor merupakan jenis dari kendaraan. Selain itu, definisi Kendaraan yakni alat transportasi dari satu daerah ke daerah lain. Motor
 dan mobil dapat digunakan untuk bertransportasi, sehingga dapat disimpukan bahwa kendaraan, mobil, dan motor merupakan objek yang sama. Atribut yang ada pada kelas kendaraan
 dapat digunakan oleh kelas anak yakni kelas Motor dan Mobil.<br>

 ### Penggabungan Kelas Parkir dan Garasi
 #### Definisi Garasi
 Garasi adalah bangunan yang dirancang untuk menyimpan kendaraan.

 #### Definisi Tempat Parkir
 Tempat Parkir adalah tempat di mana kendaraan dapat diparkir atau disimpan untuk sementara waktu, biasanya dapat berupa area terbuka maupun area tertutup.

 ada beberapa alasan sehingga saya memutuskan menggabungkan kedua kelas tersebut
 alasan - alasan itu antaralain :
 1. Atribut yang sama : baik garasi maupun tempat parkir memiliki luas tempat, jumlah kapasitas kendaraan yang dapat ditampung, nama tempat parkir/garasi, daftar kendaraan yang sedang terparkir, dan lain nya.
 2. Fungsi yang sama : Baik garasi maupun tempat parkir memiliki fungsi yang sama yakni tempat untuk menyimpan kendaraan, baik itu mobil, motor, sepedan dan sebagainya.
 3. Struktural : garasi memiliki struktur bangunan tertutup dengan atap untuk melindungi kendaraan dari perubahan cuaca cuaca, dewasa ini
    tempat parkir juga memiliki struktur bangunan tertutup dengan atap dan gerbang tiket untuk melindungi kendaraan
    dari perubahan cuaca maupun maling.

### Composite
Umumnya tempat parkir memiliki kendaraan yang terparkir, karena berdasarkan fungsi nya tempat parkir merupakan sebuah tempat untuk menyimpan kendaraan. Sehingga dapat disimpulkan
bahwa tempat parkir memiliki hubungan composite dengan kendaraan.
    
 
# Desain Program
Program ini menggunakan 2 bahasa yakni C++, dan PYTHON. Dalam desain program ini, saya menggunakan hirarchical Inheritance untuk membuat kelas - kelas yang merepresentasikan Kendaraan, Mobil, dan Motor, selain itu,
saya juga menggunakan composite untuk menghubungkan antara tempat parkir dengan kendaraan.

<br> Adapun rincian kelas - kelas tersebut antara lain:<br>
### Kelas Kendaraan
1. Kelas ini memiliki atribut <br>
   a. Plat nomor    : Atribut ini digunakan untuk menyimpan Plat nomor kendaraan.<br>
   b. Merk  : Atribut ini digunakan untuk menyimpan Merk kendaraan.<br>
   c. Tahun_produksi : Atribut ini digunakan untuk menyimpan tahun produksi dari kendaraan. <br>
   e. Warna  : Atribut ini digunakan untuk menyimpan warna kendaraan. <br>
2. Kelas ini memiliki metode sebagai berikut :<br>
   a. Konstruktor  : Metode konstruktor digunakan untuk menginisialisasi objek ketika dibuat. Pada kelas Product, konstruktor akan menerima parameter yang diperlukan seperti ID, nama, brand, dan harga.<br>
   b. Getter       : Metode getter digunakan untuk mendapatkan nilai dari atribut tertentu. <br>
   c. Setter       : Metode setter digunakan untuk mengatur nilai atribut tertentu. <br>
3. Kelas ini merupakan Parent dari kelas Mobil dan Motor
<br>

### Kelas Mobil
1. Kelas ini memiliki atribut <br>
   a. Jumlah_kursi   : Atribut ini digunakan untuk menyimpan jumlah kursi yang dimiliki mobil.<br>
   b. Jumlah_pintu  : Atribut ini digunakan untuk menyimpan jumlah pintu yang dimiliki mobil.<br>
2. Kelas ini memiliki metode sebagai berikut :<br>
   a. Konstruktor  : Metode konstruktor digunakan untuk menginisialisasi objek ketika dibuat.<br>
   b. Getter       : Metode getter digunakan untuk mendapatkan nilai dari atribut tertentu. <br>
   c. Setter       : Metode setter digunakan untuk mengatur nilai atribut tertentu. <br>
3. Kelas ini merupakan Sub Class dari kelas Kendaraan.
<br>

### Kelas Motor
1. Kelas ini memiliki atribut <br>
   a. Jenis_motor   : Atribut ini digunakan untuk menyimpan Jenis sebuah motor.<br>
   b. Kapasitas_tangki  : Atribut ini digunakan untuk menyimpan kapasitas tangki motor.<br>
2. Kelas ini memiliki metode sebagai berikut :<br>
   a. Konstruktor  : Metode konstruktor digunakan untuk menginisialisasi objek ketika dibuat.<br>
   b. Getter       : Metode getter digunakan untuk mendapatkan nilai dari atribut tertentu. <br>
   c. Setter       : Metode setter digunakan untuk mengatur nilai atribut tertentu. <br>
3. Kelas ini merupakan Sub Class dari kelas Kendaraan.
<br>

### Kelas Tempat Parkir
1. Kelas ini memiliki atribut <br>
   a. Nama Tempat parkir  : Atribut ini digunakan untuk menyimpan nama baik untuk tempat parkir, garasi, dan lainnya.<br>
   b. Luas  : Atribut ini digunakan untuk menyimpan luas sebuah tempat untuk memarkirkan kendaraan.<br>
   c. Kapasitas : Atribut ini digunakan untuk menyimpan kapasitas tempat yang digunakan untuk menyimpan kendaraan.<br>
   d. Jumlah kendaraan : Atribut ini digunakan untuk menyimpan jumlah kendaraan yang terparkir.<br>
   e. List Motor : Atribut ini digunakan untuk menyimpan list motor yang terparkir di tempat.<br>
   f. List Mobil : Atribut ini digunakan untuk menyimpan list mobil yang terparkir di tempat.<br>
2. Kelas ini memiliki metode sebagai berikut :<br>
   a. Konstruktor  : Metode konstruktor digunakan untuk menginisialisasi objek ketika dibuat.<br>
   b. Getter       : Metode getter digunakan untuk mendapatkan nilai dari atribut tertentu. <br>
   c. Setter       : Metode setter digunakan untuk mengatur nilai atribut tertentu. <br>
   d. Add          : Metode Add digunakan untuk menambahkan data kendaraan baik itu motor maupun mobil.<br>
   e. Kendaraan Masuk : Metode kendaraan masuk ini berupa sebuah prosedur untuk menghitung banyaknya kendaraan yang terparkir, baik itu motor maupun mobil.<br>
3. Kelas ini merupakan composite dari kelas kendaraan.
<br>


# Penjelasan alur
#### Penjelasan alur C++
1. User diminta untuk memilih program yang akan dijalankan, adapun urutan programnya adalah sebagai berikut:<br>
   a. Memilih nomor 1 untuk memasukan data parkir mobil <br>
   b. Memilih nomor 2 untuk memasukan data parkir motor <br>
   c. Memilih nomor 3 untuk mengakhiri program pemasukan data <br>
3. Jika user memilih program nomor 1 dan 2, user akan diminta mengisi data kendaraan yang diparkirkan, baik itu data kendaraan mobil maupun motor. <br> 
4. Jika tempat parkir sudah melebihi kapasitas, maka user tidak bisa mengisi program pengisian data. Sehingga akan langsung keluar dari program pemasukan data, dan menampilkan data kendaraan yang terparkir. <br>
5. Jika user memilih program nomor 3, maka program pemasukkan data akan selesai kemudian menampilkan data kendaraan yang terparkir.<br>

#### Penjelasan alur Python
1. User diminta untuk memilih program yang akan dijalankan, adapun urutan programnya adalah sebagai berikut:<br>
   a. Memilih nomor 1 untuk memasukan data parkir mobil <br>
   b. Memilih nomor 2 untuk memasukan data parkir motor <br>
   c. Memilih nomor 3 untuk mengeluarkan kendaraan <br>
   d. Memilih nomor 4 untuk menampilkan data <br>
   c. Memilih nomor 5 untuk mengakhiri program <br>
2. Jika user memilih program nomor 1 dan 2, user akan diminta mengisi data kendaraan yang diparkirkan.  Jika tempat parkir sudah melebihi kapasitas, maka user tidak bisa mengisi program pengisian data. Sehingga akan langsung keluar dari program pemasukan data.<br>
3. Jika user memilih program nomor 3, user akan diminta untuk memilih kendaraan apa yang akan keluar dari parkiran, adapun urutan nya sebagai berikut:<br>
   a. Memilih 'C' jika mobil yang keluar <br>
   b. Memilih 'M' jika motor yang keluar <br>
   c. Memilih 'K' untuk keluar dari program <br>
   Setelah user memilih kendaraan yang akan keluar, user akan diminta untuk memasukkan nomor plat kendaraan yang keluar, agar data kendaraan dapat terhapus.<br>
4. Jika user memilih nomor 4, maka user akan diminta untuk memilih jenis kendaraan yang datanya akan ditampilkan. Adapun urutannya sebagai berikut:<br>
   a. Memilih 'PC' untuk menampilkan data mobil <br>
   b. Memilih 'PM' untuk menampilkan data motor <br>
   c. Memilih 'K' untuk keluar dari program <br>
5. Jika user memilih nomor 5, maka program akan selesai dan keluar.<br>


# Dokumentasi Program
![alt text](https://github.com/nabillassyfa/LP4DPBO2024C2/blob/main/C%2B%2B/Screenshot/SS%20cpp%20(1).png)
<br>
Pengisian data kendaraan berupa motor dan mobil.<br>
Jika kapasitas tempat parkir masih tersedia, maka penambahan data akan berhasil.<br><br><br>
![alt text](https://github.com/nabillassyfa/LP4DPBO2024C2/blob/main/C%2B%2B/Screenshot/SS%20cpp%20(2).png)
<br>
Jika kapasitas tempat parkir sudah penuh, maka program pemasukkan data akan berhenti dan menampilkan data kendaraan yang terparkir.
