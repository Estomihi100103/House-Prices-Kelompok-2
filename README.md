# Prediksi Harga Rumah Menggunakan Algoritma LightGBM

## Deskripsi Proyek
Proyek merupakan proyek akhir untuk mata kuliah data mining pada program studi Sistem Informasi Institut Teknologi Del tahun ajaran 2024/2025. Proyek ini bertujuan untuk memprediksi harga rumah berdasarkan berbagai fitur properti menggunakan algoritma LightGBM. Tantangan ini berasal dari kompetisi Kaggle bertema **House Prices - Advanced Regression Techniques**, yang mengharuskan peserta untuk memprediksi harga rumah dengan menggunakan data dari Ames, Iowa. Metrik evaluasi utama yang digunakan adalah **Root Mean Squared Error (RMSE)** antara log harga prediksi dan harga aktual.

Proyek prediksi harga rumah ini termasuk dalam jenis proyek regresi. Dalam konteks machine learning, regresi adalah teknik yang digunakan untuk memprediksi nilai kontinu, seperti harga rumah, berdasarkan fitur-fitur tertentu.
Karena proyek ini berfokus pada prediksi harga, data yang digunakan harus berlabel, artinya setiap contoh data harus memiliki nilai target atau variabel yang ingin diprediksi. Dalam hal ini, variabel target adalah SalePrice, yaitu harga jual rumah.

## Metrik Evaluasi
**RMSE (Root Mean Squared Error)**: Metrik ini mengukur perbedaan antara nilai prediksi dan nilai aktual, diukur dalam satuan log harga properti. RMSE yang lebih rendah menunjukkan model yang lebih akurat.

## Data yang Digunakan
Dataset yang digunakan berasal dari kompetisi Kaggle **House Prices - Advanced Regression Techniques** dan memiliki berbagai atribut yang menggambarkan karakteristik fisik dan struktural sebuah properti. Berikut adalah beberapa kolom dalam dataset:

| No  | Atribut        | Non-Null Count | Tipe Data | Keterangan                                                                                       |
|-----|----------------|----------------|-----------|---------------------------------------------------------------------------------------------------|
| 1   | MSSubClass     | 1460           | int64     | Tipe bangunan yang terlibat dalam penjualan.                                                     |
| 2   | MSZoning       | 1460           | object    | Klasifikasi zona umum dari penjualan.                                                            |
| 3   | LotFrontage    | 1201           | float64   | Panjang garis depan tanah yang terhubung ke jalan.                                               |
| 4   | LotArea        | 1460           | int64     | Ukuran tanah dalam kaki persegi.                                                                 |
| 5   | Street         | 1460           | object    | Jenis akses jalan ke properti.                                                                   |
| 6   | Alley          | 91             | object    | Jenis akses gang ke properti.                                                                    |
| 7   | LotShape       | 1460           | object    | Bentuk umum properti.                                                                            |
| 8   | LandContour    | 1460           | object    | Kemiringan properti.                                                                             |
| 9   | Utilities      | 1460           | object    | Jenis utilitas yang tersedia.                                                                    |
| 10  | LotConfig      | 1460           | object    | Konfigurasi tanah.                                                                               |
| 11  | LandSlope      | 1460           | object    | Kemiringan tanah.                                                                                |
| 12  | Neighborhood   | 1460           | object    | Lokasi fisik dalam batas kota Ames.                                                              |
| 13  | Condition1     | 1460           | object    | Kedekatan dengan kondisi tertentu.                                                               |
| 14  | Condition2     | 1460           | object    | Kedekatan dengan kondisi tertentu (jika lebih dari satu ada).                                    |
| 15  | BldgType       | 1460           | object    | Tipe bangunan.                                                                                   |
| 16  | HouseStyle     | 1460           | object    | Gaya bangunan.                                                                                   |
| 17  | OverallQual    | 1460           | int64     | Menilai kualitas material dan penyelesaian rumah secara keseluruhan.                            |
| 18  | OverallCond    | 1460           | int64     | Menilai kondisi umum rumah.                                                                      |
| 19  | YearBuilt      | 1460           | int64     | Tahun rumah dibangun.                                                                            |
| 20  | YearRemodAdd   | 1460           | int64     | Tahun rumah direnovasi atau ditambahkan.                                                         |
| 21  | RoofStyle      | 1460           | object    | Tipe atap rumah.                                                                                 |
| 22  | RoofMatl       | 1460           | object    | Material atap rumah.                                                                             |
| 23  | Exterior1st    | 1460           | object    | Material pelapis luar utama rumah.                                                               |
| 24  | Exterior2nd    | 1460           | object    | Material pelapis luar sekunder rumah.                                                            |
| 25  | MasVnrType     | 588            | object    | Tipe veneer batu pada eksterior rumah.                                                           |
| 26  | MasVnrArea     | 1452           | float64   | Luas veneer batu pada eksterior rumah (dalam kaki persegi).                                      |
| 27  | ExterQual      | 1460           | object    | Menilai kualitas material eksterior rumah.                                                      |
| 28  | ExterCond      | 1460           | object    | Menilai kondisi material eksterior rumah.                                                       |
| 29  | Foundation     | 1460           | object    | Jenis fondasi rumah.                                                                             |
| 30  | BsmtQual       | 1423           | object    | Menilai tinggi basement rumah.                                                                  |
| 31  | BsmtCond       | 1423           | object    | Menilai kondisi basement rumah.                                                                 |
| 32  | BsmtExposure   | 1422           | object    | Menilai tingkat pencahayaan basement rumah.                                                     |
| 33  | BsmtFinType1   | 1423           | object    | Jenis penyelesaian basement tipe 1.                                                             |
| 34  | BsmtFinSF1     | 1460           | int64     | Luas penyelesaian basement tipe 1 (dalam kaki persegi).                                         |
| 35  | BsmtFinType2   | 1422           | object    | Jenis penyelesaian basement tipe 2.                                                             |
| 36  | BsmtFinSF2     | 1460           | int64     | Luas penyelesaian basement tipe 2 (dalam kaki persegi).                                         |
| 37  | BsmtUnfSF      | 1460           | int64     | Luas basement yang belum selesai (dalam kaki persegi).                                          |
| 38  | TotalBsmtSF    | 1460           | int64     | Total luas basement (dalam kaki persegi).                                                      |
| 39  | Heating        | 1460           | object    | Tipe sistem pemanas rumah.                                                                      |
| 40  | HeatingQC      | 1460           | object    | Menilai kualitas sistem pemanas rumah.                                                         |
| 41  | CentralAir     | 1460           | object    | Apakah rumah memiliki pendingin udara sentral (Y/N).                                            |
| 42  | Electrical     | 1459           | object    | Tipe sistem kelistrikan utama rumah.                                                            |
| 43  | 1stFlrSF       | 1460           | int64     | Luas lantai pertama (dalam kaki persegi).                                                      |
| 44  | 2ndFlrSF       | 1460           | int64     | Luas lantai kedua (dalam kaki persegi).                                                        |
| 45  | LowQualFinSF   | 1460           | int64     | Luas penyelesaian berkualitas rendah (dalam kaki persegi).                                      |
| 46  | GrLivArea      | 1460           | int64     | Luas area tinggal di atas permukaan tanah (dalam kaki persegi).                                 |
| 47  | BsmtFullBath   | 1460           | int64     | Jumlah kamar mandi penuh di basement.                                                           |
| 48  | BsmtHalfBath   | 1460           | int64     | Jumlah kamar mandi setengah di basement.                                                        |
| 49  | FullBath       | 1460           | int64     | Jumlah kamar mandi penuh di atas permukaan tanah.                                               |
| 50  | HalfBath       | 1460           | int64     | Jumlah kamar mandi setengah di atas permukaan tanah.                                            |
| 51  | BedroomAbvGr    | 1460           | int64     | Jumlah kamar tidur di atas permukaan tanah.                                                      |
| 52  | KitchenAbvGr    | 1460           | int64     | Jumlah dapur di atas permukaan tanah.                                                            |
| 53  | KitchenQual     | 1460           | object    | Menilai kualitas dapur.                                                                          |
| 54  | TotRmsAbvGrd    | 1460           | int64     | Total jumlah ruangan di atas permukaan tanah (tidak termasuk kamar mandi).                       |
| 55  | Functional      | 1460           | object    | Menilai fungsionalitas rumah (Tipe fungsionalitas).                                              |
| 56  | Fireplaces      | 1460           | int64     | Jumlah perapian di rumah.                                                                        |
| 57  | FireplaceQu     | 770            | object    | Menilai kualitas perapian (jika ada).                                                           |
| 58  | GarageType      | 1379           | object    | Tipe garasi rumah.                                                                               |
| 59  | GarageYrBlt     | 1379           | float64   | Tahun garasi dibangun.                                                                           |
| 60  | GarageFinish    | 1379           | object    | Kondisi akhir garasi (selesai atau belum selesai).                                               |
| 61  | GarageCars      | 1460           | int64     | Kapasitas garasi dalam jumlah mobil.                                                             |
| 62  | GarageArea      | 1460           | int64     | Luas garasi dalam kaki persegi.                                                                  |
| 63  | GarageQual      | 1379           | object    | Menilai kualitas garasi.                                                                        |
| 64  | GarageCond      | 1379           | object    | Menilai kondisi garasi.                                                                         |
| 65  | PavedDrive      | 1460           | object    | Apakah jalan menuju garasi sudah beraspal (Y/N).                                                |
| 66  | WoodDeckSF      | 1460           | int64     | Luas dek kayu dalam kaki persegi.                                                               |
| 67  | OpenPorchSF     | 1460           | int64     | Luas serambi terbuka dalam kaki persegi.                                                        |
| 68  | EnclosedPorch   | 1460           | int64     | Luas serambi tertutup dalam kaki persegi.                                                       |
| 69  | 3SsnPorch       | 1460           | int64     | Luas serambi tiga musim dalam kaki persegi.                                                     |
| 70  | ScreenPorch     | 1460           | int64     | Luas serambi dengan layar dalam kaki persegi.                                                   |
| 71  | PoolArea        | 1460           | int64     | Luas kolam renang dalam kaki persegi.                                                           |
| 72  | PoolQC          | 7              | object    | Menilai kualitas kolam renang (jika ada).                                                       |
| 73  | Fence           | 281            | object    | Jenis pagar rumah.                                                                               |
| 74  | MiscFeature     | 54             | object    | Fitur tambahan rumah yang tidak termasuk dalam kategori lain.                                    |
| 75  | MiscVal         | 1460           | int64     | Nilai moneter untuk fitur tambahan (dalam dolar).                                               |
| 76  | MoSold          | 1460           | int64     | Bulan saat rumah terjual.                                                                       |
| 77  | YrSold          | 1460           | int64     | Tahun saat rumah terjual.                                                                       |
| 78  | SaleType        | 1460           | object    | Tipe penjualan rumah.                                                                            |
| 79  | SaleCondition   | 1460           | object    | Kondisi penjualan rumah.                                                                         |
| 80  | SalePrice       | 1460           | int64     | Harga penjualan rumah (dalam dolar AS).                                                         |


## Pendekatan dan Algoritma yang Digunakan
Proyek ini menggunakan **LightGBM (Light Gradient Boosting Machine)** sebagai algoritma utama untuk membangun model prediksi harga rumah. LightGBM dipilih karena:

- **Kecepatan**: LightGBM dapat menangani dataset besar dengan efisien.
- **Kemampuan Mengelola Fitur Kategorikal dan Numerik**: LightGBM memiliki kemampuan untuk menangani fitur kategorikal dengan cara yang lebih efisien daripada banyak algoritma lain.
- **Akurasi**: LightGBM mampu memberikan akurasi yang baik pada banyak jenis masalah regresi dan klasifikasi, termasuk prediksi harga properti.

References: Ke, G., Meng, Q., Finley, T., Wang, T., Chen, W., Ma, W., ... & Liu, T. Y. (2017). Lightgbm: A highly efficient gradient boosting decision tree. Advances in neural information processing systems, 30.

## Tahapan Proyek
Berikut adalah tahapan utama dalam proyek ini:

### 1. Buisness Understanding
Proyek ini memberikan solusi berbasis teknologi bagi pasar real estate yang menghadapi tantangan dalam menyediakan estimasi harga properti yang akurat dan terkini di tengah persaingan yang ketat dan dinamika pasar yang terus berubah. Sangat penting untuk memahami semua variabel yang memengaruhi harga properti, termasuk lokasi, fitur fisik rumah, kondisi ekonomi lokal, dan tren pasar. Untuk mengatasi masalah ini, digunakan pendekatan analisis prediktif dengan memanfaatkan data properti historis yang mencakup fitur seperti luas tanah, jumlah kamar, lokasi geografis, kondisi fisik rumah, dan pola harga pasar lokal. Proyek ini berfokus pada pengembangan model prediksi harga properti berbasis machine learning yang dirancang untuk mengestimasi harga jual rumah (SalePrice). Hal ini membantu meningkatkan efisiensi dan transparansi di pasar real estate.
Model ini diharapkan dapat memberikan manfaat strategis bagi berbagai pihak yang terlibat dalam industri real estate, termasuk:
1.	Pembeli rumah: Untuk memperoleh estimasi harga yang wajar untuk properti yang diinginkan.
2.	Penjual rumah: Untuk menentukan harga jual yang kompetitif dan realistis.
3.	Agen properti dan pengembang: Untuk mendukung pengambilan keputusan dalam strategi pemasaran dan memahami tren pasar.

### 2. Data Understanding

### 3. Data Preparation

### 4. Modeling

### 5. Model Evaluation

### 6. Deployment

### 7. Evaluasi

## Hasil dan Evaluasi
Model ini dievaluasi menggunakan metrik RMSE yang dihitung pada skala logaritma dari harga properti. Hasil model dibandingkan dengan pengamatan nyata untuk properti dengan harga mahal dan murah. Model menunjukkan kemampuan yang baik dalam memprediksi harga rumah pada dataset yang diberikan, meskipun ada beberapa prediksi yang masih cukup jauh dari harga aktual, terutama untuk properti dengan harga sangat tinggi atau sangat rendah.

## Penggunaan Notebook

Untuk menjalankan kode ini, Anda perlu menginstal beberapa dependencies. Berikut adalah cara untuk memulai:

### Instalasi Dependencies:
Install dengan pip:

```bash
pip install -r requirements.txt
