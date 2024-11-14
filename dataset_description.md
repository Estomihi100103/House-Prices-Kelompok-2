# Deskripsi Atribut Dataset Rumah

## MSSubClass
Menunjukkan tipe bangunan yang terlibat dalam penjualan.

- **20**: 1-LOKASI 1 LANTAI 1946 & LEBIH BARU SEMUA GAYA
- **30**: 1-LOKASI 1 LANTAI 1945 & LEBIH TUA
- **40**: 1-LOKASI 1 LANTAI DENGAN LOT SEDIAAN ATTIC SEMUA USIA
- **45**: 1-LOKASI 1,5 LANTAI - BELUM DIPERBAIKI SEMUA USIA
- **50**: 1-LOKASI 1,5 LANTAI - DIPERBAIKI SEMUA USIA
- **60**: 2 LANTAI 1946 & LEBIH BARU
- **70**: 2 LANTAI 1945 & LEBIH TUA
- **75**: 2,5 LANTAI SEMUA USIA
- **80**: SPLIT ATAU MULTI-TINGKAT
- **85**: SPLIT FOYER
- **90**: DUPLEKS - SEMUA GAYA DAN USIA
- **120**: 1-LOKASI PUD (Perkembangan Unit Terencana) - 1946 & LEBIH BARU
- **150**: 1-LOKASI 1,5 LANTAI PUD - SEMUA USIA
- **160**: 2 LANTAI PUD - 1946 & LEBIH BARU
- **180**: PUD - MULTI-TINGKAT - TERMASUK SPLIT LEV/FOYER
- **190**: KONVERSI 2 KELUARGA - SEMUA GAYA DAN USIA

## MSZoning
Menunjukkan klasifikasi zona umum dari penjualan.

- **A**: Pertanian
- **C**: Komersial
- **FV**: Desa Terapung Residensial
- **I**: Industri
- **RH**: Kepadatan Tinggi Residensial
- **RL**: Kepadatan Rendah Residensial
- **RP**: Parkir Kepadatan Rendah Residensial
- **RM**: Kepadatan Medium Residensial

## LotFrontage
Panjang garis depan tanah yang terhubung ke jalan.

## LotArea
Ukuran tanah dalam kaki persegi.

## Street
Jenis akses jalan ke properti.

- **Grvl**: Kerikil
- **Pave**: Aspal

## Alley
Jenis akses gang ke properti.

- **Grvl**: Kerikil
- **Pave**: Aspal
- **NA**: Tidak ada akses gang

## LotShape
Bentuk umum properti.

- **Reg**: Teratur
- **IR1**: Sedikit tidak teratur
- **IR2**: Cukup tidak teratur
- **IR3**: Tidak teratur

## LandContour
Kemiringan properti.

- **Lvl**: Rata-rata/Level
- **Bnk**: Tepi - Kenaikan cepat dan signifikan dari tingkat jalan ke bangunan
- **HLS**: Lereng - Kemiringan signifikan dari sisi ke sisi
- **Low**: Depresi

## Utilities
Jenis utilitas yang tersedia.

- **AllPub**: Semua utilitas publik (E, G, W, & S)
- **NoSewr**: Listrik, Gas, dan Air (Tangki Septik)
- **NoSeWa**: Listrik dan Gas Saja
- **ELO**: Hanya Listrik

## LotConfig
Konfigurasi tanah.

- **Inside**: Lot dalam
- **Corner**: Lot sudut
- **CulDSac**: Ujung jalan buntu
- **FR2**: Hadapan pada 2 sisi properti
- **FR3**: Hadapan pada 3 sisi properti

## LandSlope
Kemiringan tanah.

- **Gtl**: Kemiringan ringan
- **Mod**: Kemiringan sedang
- **Sev**: Kemiringan tajam

## Neighborhood
Lokasi fisik dalam batas kota Ames.

- **Blmngtn**: Bloomington Heights
- **Blueste**: Bluestem
- **BrDale**: Briardale
- **BrkSide**: Brookside
- **ClearCr**: Clear Creek
- **CollgCr**: College Creek
- **Crawfor**: Crawford
- **Edwards**: Edwards
- **Gilbert**: Gilbert
- **IDOTRR**: Iowa DOT dan Jalur Kereta Api
- **MeadowV**: Meadow Village
- **Mitchel**: Mitchell
- **Names**: North Ames
- **NoRidge**: Northridge
- **NPkVill**: Northpark Villa
- **NridgHt**: Northridge Heights
- **NWAmes**: Northwest Ames
- **OldTown**: Old Town
- **SWISU**: Selatan & Barat Universitas Negeri Iowa
- **Sawyer**: Sawyer
- **SawyerW**: Sawyer West
- **Somerst**: Somerset
- **StoneBr**: Stone Brook
- **Timber**: Timberland
- **Veenker**: Veenker

## Condition1
Kedekatan dengan kondisi tertentu.

- **Artery**: Berdampingan dengan jalan arteri
- **Feedr**: Berdampingan dengan jalan penghubung
- **Norm**: Normal
- **RRNn**: Dalam 200' dari Jalur Kereta Api Utara-Selatan
- **RRAn**: Berdampingan dengan Jalur Kereta Api Utara-Selatan
- **PosN**: Dekat fitur positif di luar lokasi—taman, jalur hijau, dll.
- **PosA**: Berdampingan dengan fitur positif di luar lokasi
- **RRNe**: Dalam 200' dari Jalur Kereta Api Timur-Barat
- **RRAe**: Berdampingan dengan Jalur Kereta Api Timur-Barat

## Condition2
Kedekatan dengan kondisi tertentu (jika lebih dari satu ada).

- **Artery**: Berdampingan dengan jalan arteri
- **Feedr**: Berdampingan dengan jalan penghubung
- **Norm**: Normal
- **RRNn**: Dalam 200' dari Jalur Kereta Api Utara-Selatan
- **RRAn**: Berdampingan dengan Jalur Kereta Api Utara-Selatan
- **PosN**: Dekat fitur positif di luar lokasi—taman, jalur hijau, dll.
- **PosA**: Berdampingan dengan fitur positif di luar lokasi
- **RRNe**: Dalam 200' dari Jalur Kereta Api Timur-Barat
- **RRAe**: Berdampingan dengan Jalur Kereta Api Timur-Barat

## BldgType
Tipe bangunan.

- **1Fam**: Rumah Tinggal Terpisah
- **2FmCon**: Konversi Dua Keluarga; awalnya dibangun sebagai rumah tinggal satu keluarga
- **Duplx**: Dupleks
- **TwnhsE**: Unit Sudut Townhouse
- **TwnhsI**: Unit Dalam Townhouse

## HouseStyle
Gaya bangunan.

- **1Story**: Satu lantai
- **1.5Fin**: Satu setengah lantai: lantai kedua selesai
- **1.5Unf**: Satu setengah lantai: lantai kedua belum selesai
- **2Story**: Dua lantai
- **2.5Fin**: Dua setengah lantai: lantai kedua selesai
- **2.5Unf**: Dua setengah lantai: lantai kedua belum selesai
- **SFoyer**: Split Foyer
- **SLvl**: Split Level

## OverallQual
Menilai kualitas material dan penyelesaian rumah secara keseluruhan.

- **10**: Sangat Baik
- **9**: Baik
- **8**: Sangat Baik
- **7**: Baik
- **6**: Di atas rata-rata
- **5**: Rata-rata
- **4**: Di bawah rata-rata
- **3**: Cukup
- **2**: Buruk
- **1**: Sangat Buruk

## OverallCond
Menilai kondisi umum rumah.

- **10**: Sangat Baik
- **9**: Baik
- **8**: Sangat Baik
- **7**: Baik
- **6**: Di atas rata-rata
- **5**: Rata-rata
- **4**: Di bawah rata-rata
- **3**: Cukup
- **2**: Buruk
- **1**: Sangat Buruk

## YearBuilt
Tanggal konstruksi asli.

## YearRemodAdd
Tanggal renovasi (sama dengan tanggal konstruksi jika tidak ada renovasi atau tambahan).

## RoofStyle
Jenis atap.

- **Flat**: Datar
- **Gable**: Atap Gable
- **GableM**: Atap Gable Dimodifikasi
- **Hip**: Atap Hip
- **Mansard**: Atap Mansard
- **Shed**: Atap Shed

## RoofMatl
Bahan penutup atap.

- **ClyTile**: Tile Tanah Liat
- **GrvTile**: Tile Gerigi
- **CompShg**: Shingle Komposit
- **Membran**: Membran
- **Metal**: Logam
- **Roll**: Roll (Atap Bitumen)
- **Tar&Grv**: Tar & Gravel
- **WdShake**: Kayu Shake
- **WdShngl**: Kayu Shingle

## Exterior1st
Penutup luar pada rumah.

- **AsbShng**: Sirap Asbes
- **AsphShn**: Sirap Aspal
- **BrkComm**: Bata Umum
- **BrkFace**: Bata Fasad
- **CBlock**: Blok Sinder
- **CemntBd**: Papan Semen
- **HdBoard**: Papan Keras
- **ImStucc**: Stuko Imitasi
- **MetalSd**: Dinding Logam
- **Other**: Lainnya
- **Plywood**: Plywood
- **PreCast**: Precast (Beton Pracetak)
- **Stone**: Batu
- **Stucco**: Stuko
- **VinylSd**: Dinding Vinyl
- **Wd Sdng**: Dinding Kayu
- **WdShing**: Sirap Kayu

## Exterior2nd
Penutup luar pada rumah (jika menggunakan lebih dari satu bahan).

- **AsbShng**: Sirap Asbes
- **AsphShn**: Sirap Aspal
- **BrkComm**: Bata Umum
- **BrkFace**: Bata Fasad
- **CBlock**: Blok Sinder
- **CemntBd**: Papan Semen
- **HdBoard**: Papan Keras
- **ImStucc**: Stuko Imitasi
- **MetalSd**: Dinding Logam
- **Other**: Lainnya
- **Plywood**: Plywood
- **PreCast**: Precast (Beton Pracetak)
- **Stone**: Batu
- **Stucco**: Stuko
- **VinylSd**: Dinding Vinyl
- **Wd Sdng**: Dinding Kayu
- **WdShing**: Sirap Kayu

## MasVnrType
Jenis veneer masonry (penutup batu atau bata).

- **BrkCmn**: Bata Umum
- **BrkFace**: Bata Fasad
- **CBlock**: Blok Sinder
- **None**: Tidak ada
- **Stone**: Batu

## MasVnrArea
Luas veneer masonry dalam satuan kaki persegi.

## ExterQual
Menilai kualitas bahan pada bagian luar rumah.

- **Ex**: Sangat Baik
- **Gd**: Baik
- **TA**: Rata-rata/Terstandarisasi
- **Fa**: Cukup
- **Po**: Buruk

## ExterCond
Menilai kondisi saat ini dari bahan pada bagian luar rumah.

- **Ex**: Sangat Baik
- **Gd**: Baik
- **TA**: Rata-rata/Terstandarisasi
- **Fa**: Cukup
- **Po**: Buruk

# Deskripsi Atribut Dataset Rumah

## Foundation
Jenis fondasi.

- **BrkTil**: Bata & Ubin
- **CBlock**: Blok Sinder
- **PConc**: Beton Cor
- **Slab**: Lempengan
- **Stone**: Batu
- **Wood**: Kayu

## BsmtQual
Menilai tinggi basement.

- **Ex**: Sangat Baik (100+ inci)
- **Gd**: Baik (90-99 inci)
- **TA**: Rata-rata (80-89 inci)
- **Fa**: Cukup (70-79 inci)
- **Po**: Buruk (<70 inci)
- **NA**: Tidak Ada Basement

## BsmtCond
Menilai kondisi umum basement.

- **Ex**: Sangat Baik
- **Gd**: Baik
- **TA**: Rata-rata - sedikit kelembapan diizinkan
- **Fa**: Cukup - terdapat kelembapan atau retak atau penurunan
- **Po**: Buruk - retak parah, penurunan, atau kebasahan
- **NA**: Tidak Ada Basement

## BsmtExposure
Mengacu pada tembok walkout atau level taman.

- **Gd**: Paparan Baik
- **Av**: Paparan Rata-rata (split levels atau foyers umumnya diberi nilai rata-rata atau lebih)
- **Mn**: Paparan Minimum
- **No**: Tidak Ada Paparan
- **NA**: Tidak Ada Basement

## BsmtFinType1
Penilaian area basement yang sudah selesai.

- **GLQ**: Kamar Layak Huni Baik
- **ALQ**: Kamar Layak Huni Rata-rata
- **BLQ**: Kamar Layak Huni di Bawah Rata-rata
- **Rec**: Ruang Rekreasi Rata-rata
- **LwQ**: Kualitas Rendah
- **Unf**: Belum Selesai
- **NA**: Tidak Ada Basement

## BsmtFinSF1
Luas tipe 1 basement yang selesai dalam satuan kaki persegi.

## BsmtFinType2
Penilaian area basement yang sudah selesai (jika terdapat lebih dari satu tipe).

- **GLQ**: Kamar Layak Huni Baik
- **ALQ**: Kamar Layak Huni Rata-rata
- **BLQ**: Kamar Layak Huni di Bawah Rata-rata
- **Rec**: Ruang Rekreasi Rata-rata
- **LwQ**: Kualitas Rendah
- **Unf**: Belum Selesai
- **NA**: Tidak Ada Basement

## BsmtFinSF2
Luas tipe 2 basement yang selesai dalam satuan kaki persegi.

## BsmtUnfSF
Luas area basement yang belum selesai dalam satuan kaki persegi.

## TotalBsmtSF
Total luas area basement dalam satuan kaki persegi.

## Heating
Jenis pemanas.

- **Floor**: Pemanas Lantai
- **GasA**: Tungku udara panas berbahan bakar gas
- **GasW**: Pemanas air panas atau uap berbahan bakar gas
- **Grav**: Tungku gravitasi
- **OthW**: Pemanas air panas atau uap selain gas
- **Wall**: Tungku Dinding

## HeatingQC
Kualitas dan kondisi pemanas.

- **Ex**: Sangat Baik
- **Gd**: Baik
- **TA**: Rata-rata/Standar
- **Fa**: Cukup
- **Po**: Buruk

# Deskripsi Atribut Dataset Rumah

## CentralAir
Sistem pendingin udara pusat.

- **N**: Tidak Ada
- **Y**: Ada

## Electrical
Sistem kelistrikan.

- **SBrkr**: Pemutus Sirkuit Standar & Romex
- **FuseA**: Kotak Sekring di atas 60 AMP dan semua kabel Romex (Rata-rata)
- **FuseF**: Kotak Sekring 60 AMP dan sebagian besar kabel Romex (Cukup)
- **FuseP**: Kotak Sekring 60 AMP dan sebagian besar kabel kenop & tabung (Buruk)
- **Mix**: Campuran

## 1stFlrSF
Luas lantai pertama dalam satuan kaki persegi.

## 2ndFlrSF
Luas lantai kedua dalam satuan kaki persegi.

## LowQualFinSF
Luas area dengan kualitas penyelesaian rendah (semua lantai) dalam satuan kaki persegi.

## GrLivArea
Luas area tinggal di atas tanah dalam satuan kaki persegi.

## BsmtFullBath
Jumlah kamar mandi penuh di basement.

## BsmtHalfBath
Jumlah kamar mandi setengah di basement.

## FullBath
Jumlah kamar mandi penuh di atas tanah.

## HalfBath
Jumlah kamar mandi setengah di atas tanah.

## Bedroom
Jumlah kamar tidur di atas tanah (tidak termasuk kamar tidur di basement).

## Kitchen
Jumlah dapur di atas tanah.

## KitchenQual
Kualitas dapur.

- **Ex**: Sangat Baik
- **Gd**: Baik
- **TA**: Rata-rata
- **Fa**: Cukup
- **Po**: Buruk

## TotRmsAbvGrd
Jumlah total ruangan di atas tanah (tidak termasuk kamar mandi).

## Functional
Fungsi rumah (diasumsikan tipikal kecuali ada pengurangan).

- **Typ**: Fungsi Tipikal
- **Min1**: Pengurangan Minor 1
- **Min2**: Pengurangan Minor 2
- **Mod**: Pengurangan Sedang
- **Maj1**: Pengurangan Mayor 1
- **Maj2**: Pengurangan Mayor 2
- **Sev**: Rusak Parah
- **Sal**: Hanya untuk Diselamatkan

## Fireplaces
Jumlah perapian.

## FireplaceQu
Kualitas perapian.

- **Ex**: Sangat Baik - Perapian Batu Berkualitas Tinggi
- **Gd**: Baik - Perapian Batu di lantai utama
- **TA**: Rata-rata - Perapian Prefabrikasi di area utama atau Perapian Batu di basement
- **Fa**: Cukup - Perapian Prefabrikasi di basement
- **Po**: Buruk - Tungku Ben Franklin
- **NA**: Tidak Ada Perapian

## GarageType
Lokasi garasi.

- **2Types**: Lebih dari satu jenis garasi
- **Attchd**: Terhubung ke rumah
- **Basment**: Garasi di Basement
- **BuiltIn**: Dibangun dalam (Garasi bagian dari rumah - biasanya ada ruangan di atas garasi)
- **CarPort**: Car Port
- **Detchd**: Terpisah dari rumah
- **NA**: Tidak Ada Garasi

## GarageYrBlt
Tahun garasi dibangun.

## GarageFinish
Penyelesaian interior garasi.

- **Fin**: Selesai
- **RFn**: Selesai Kasar
- **Unf**: Belum Selesai
- **NA**: Tidak Ada Garasi

## GarageCars
Ukuran garasi dalam kapasitas mobil.

## GarageArea
Ukuran garasi dalam satuan kaki persegi.

## GarageQual
Kualitas garasi.

- **Ex**: Sangat Baik
- **Gd**: Baik
- **TA**: Rata-rata
- **Fa**: Cukup
- **Po**: Buruk
- **NA**: Tidak Ada Garasi

# Deskripsi Atribut Dataset Rumah

## GarageCond
Kondisi garasi.

- **Ex**: Sangat Baik
- **Gd**: Baik
- **TA**: Rata-rata
- **Fa**: Cukup
- **Po**: Buruk
- **NA**: Tidak Ada Garasi

## PavedDrive
Jenis jalan masuk ke garasi.

- **Y**: Beraspal
- **P**: Sebagian Beraspal
- **N**: Tanah/Kerikil

## WoodDeckSF
Luas dek kayu dalam satuan kaki persegi.

## OpenPorchSF
Luas teras terbuka dalam satuan kaki persegi.

## EnclosedPorch
Luas teras tertutup dalam satuan kaki persegi.

## 3SsnPorch
Luas teras untuk tiga musim dalam satuan kaki persegi.

## ScreenPorch
Luas teras yang dilengkapi layar (screen) dalam satuan kaki persegi.

## PoolArea
Luas kolam renang dalam satuan kaki persegi.

## PoolQC
Kualitas kolam renang.

- **Ex**: Sangat Baik
- **Gd**: Baik
- **TA**: Rata-rata
- **Fa**: Cukup
- **NA**: Tidak Ada Kolam Renang

## Fence
Kualitas pagar.

- **GdPrv**: Privasi Bagus
- **MnPrv**: Privasi Minimal
- **GdWo**: Kualitas Kayu Bagus
- **MnWw**: Kualitas Kayu/Kawat Minimal
- **NA**: Tidak Ada Pagar

## MiscFeature
Fitur tambahan yang tidak dicakup dalam kategori lain.

- **Elev**: Elevator
- **Gar2**: Garasi Kedua (jika belum dijelaskan dalam bagian garasi)
- **Othr**: Lainnya
- **Shed**: Gudang (lebih dari 100 kaki persegi)
- **TenC**: Lapangan Tenis
- **NA**: Tidak Ada

## MiscVal
Nilai ($) dari fitur tambahan.

## MoSold
Bulan terjual (MM).

## YrSold
Tahun terjual (YYYY).

## SaleType
Jenis penjualan.

- **WD**: Sertifikat Jaminan - Konvensional
- **CWD**: Sertifikat Jaminan - Tunai
- **VWD**: Sertifikat Jaminan - Pinjaman VA
- **New**: Rumah baru dibangun dan dijual
- **COD**: Sertifikat Pengadilan/Estate
- **Con**: Kontrak 15% Uang Muka, syarat reguler
- **ConLw**: Kontrak Uang Muka Rendah dan bunga rendah
- **ConLI**: Kontrak Bunga Rendah
- **ConLD**: Kontrak Uang Muka Rendah
- **Oth**: Lainnya

## SaleCondition
Kondisi penjualan.

- **Normal**: Penjualan Normal
- **Abnorml**: Penjualan Tidak Normal - tukar, penyitaan, penjualan cepat
- **AdjLand**: Pembelian Lahan Berdampingan
- **Alloca**: Alokasi - dua properti terkait dengan sertifikat terpisah, biasanya kondominium dengan unit garasi
- **Family**: Penjualan antar anggota keluarga
- **Partial**: Rumah belum selesai ketika terakhir kali dinilai (berkaitan dengan Rumah Baru)
