# Prediksi Harga Rumah Menggunakan Algoritma LightGBM

## Deskripsi Proyek
Proyek merupakan proyek akhir untuk mata kuliah data mining pada program studi Sistem Informasi Institut Teknologi Del tahun ajaran 2024/2025. Proyek ini bertujuan untuk memprediksi harga rumah berdasarkan berbagai fitur properti menggunakan algoritma LightGBM. Tantangan ini berasal dari kompetisi Kaggle bertema **House Prices - Advanced Regression Techniques**, yang mengharuskan peserta untuk memprediksi harga rumah dengan menggunakan data dari Ames, Iowa. Metrik evaluasi utama yang digunakan adalah **Root Mean Squared Error (RMSE)** antara log harga prediksi dan harga aktual.

Proyek prediksi harga rumah ini termasuk dalam jenis proyek regresi. Dalam konteks machine learning, regresi adalah teknik yang digunakan untuk memprediksi nilai kontinu, seperti harga rumah, berdasarkan fitur-fitur tertentu.
Karena proyek ini berfokus pada prediksi harga, data yang digunakan harus berlabel, artinya setiap contoh data harus memiliki nilai target atau variabel yang ingin diprediksi. Dalam hal ini, variabel target adalah SalePrice, yaitu harga jual rumah.

## Metrik Evaluasi
**RMSE (Root Mean Squared Error)**: Metrik ini mengukur perbedaan antara nilai prediksi dan nilai aktual, diukur dalam satuan log harga properti. RMSE yang lebih rendah menunjukkan model yang lebih akurat.

## Data yang Digunakan
Dataset yang digunakan berasal dari kompetisi Kaggle **House Prices - Advanced Regression Techniques** dan memiliki berbagai atribut yang menggambarkan karakteristik fisik dan struktural sebuah properti. Berikut adalah beberapa kolom penting dalam dataset:

- **SalePrice**: Harga jual properti dalam dolar AS, merupakan variabel target yang ingin diprediksi.
- **MSSubClass**: Kelas bangunan.
- **MSZoning**: Klasifikasi zona umum.
- **LotFrontage**: Panjang lahan yang terhubung ke jalan dalam kaki linear.
- **LotArea**: Ukuran lahan dalam kaki persegi.
- **Street**: Jenis akses jalan.
- **Alley**: Jenis akses gang.
- **LotShape**: Bentuk umum dari properti.
- **LandContour**: Kemiringan dari properti.
- **Utilities**: Jenis utilitas yang tersedia.
- **LotConfig**: Konfigurasi lot.
- **LandSlope**: Kemiringan properti.
- **Neighborhood**: Lokasi fisik properti dalam batas kota Ames.
- **Condition1**: Kedekatan dengan jalan utama atau rel kereta api.
- **Condition2**: Kedekatan dengan jalan utama atau rel kereta api (jika ada lebih dari satu).
- **BldgType**: Tipe bangunan.
- **HouseStyle**: Gaya bangunan.
- **OverallQual**: Kualitas material dan finishing secara keseluruhan.
- **OverallCond**: Rating kondisi keseluruhan properti.
- **YearBuilt**: Tahun pembangunan asli.
- **YearRemodAdd**: Tahun renovasi.
- **RoofStyle**: Tipe atap.
- **RoofMatl**: Material atap.
- **Exterior1st**: Penutup luar bangunan.
- **MasVnrType**: Tipe veneer batu.
- **MasVnrArea**: Area veneer batu dalam kaki persegi.
- **BsmtQual**: Tinggi basement.
- **BsmtCond**: Kondisi umum basement.
- **BsmtExposure**: Dinding basement yang memiliki akses keluar atau tingkat taman.
- **BsmtFinType1 & 2**: Kualitas dan tipe area basement yang selesai.
- **Heating**: Tipe pemanas.
- **GarageType**: Lokasi garasi.
- **GarageCars**: Kapasitas mobil di garasi.
- **WoodDeckSF**: Luas deck kayu dalam kaki persegi.
- **PoolQC**: Kualitas kolam renang.
- **MoSold**: Bulan penjualan properti.
- **SaleType**: Jenis penjualan.
- **SaleCondition**: Kondisi penjualan.

## Pendekatan dan Algoritma yang Digunakan
Proyek ini menggunakan **LightGBM (Light Gradient Boosting Machine)** sebagai algoritma utama untuk membangun model prediksi harga rumah. LightGBM dipilih karena:

- **Kecepatan**: LightGBM dapat menangani dataset besar dengan efisien.
- **Kemampuan Mengelola Fitur Kategorikal dan Numerik**: LightGBM memiliki kemampuan untuk menangani fitur kategorikal dengan cara yang lebih efisien daripada banyak algoritma lain.
- **Akurasi**: LightGBM mampu memberikan akurasi yang baik pada banyak jenis masalah regresi dan klasifikasi, termasuk prediksi harga properti.

References: Ke, G., Meng, Q., Finley, T., Wang, T., Chen, W., Ma, W., ... & Liu, T. Y. (2017). Lightgbm: A highly efficient gradient boosting decision tree. Advances in neural information processing systems, 30.

## Tahapan Proyek
Berikut adalah tahapan utama dalam proyek ini:

### 1. Buisness Understanding

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
