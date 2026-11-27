# Agentris · Data Science (A26-CS193)

Analisis pencatatan transaksi Soto Batok & Penyetan Pak Tris.

## Rumusan masalah dan pertanyaan bisnis

Catatan uang masuk dan belanja Pak Tommy tersebar di beberapa catatan sehingga rekap periode tertentu perlu dihitung kembali. Tim menyusun lima pertanyaan untuk membantu Pak Tommy melihat kondisi pencatatan warung. [Agentris - Rumusan Masalah dan Pertanyaan Bisnis](https://docs.google.com/spreadsheets/d/1r84YzGIF4A3hbOdy_7r8MqazMyDEKU-fbrjmSFbH-Ps/edit#gid=970777601).

| ID | Pertanyaan | Cara menghitung |
| :--- | :--- | :--- |
| PB-01 | Berapa pemasukan yang tercatat setiap bulan? | Jumlahkan subtotal tiap baris penjualan dalam bulan tersebut. |
| PB-02 | Berapa pengeluaran yang tercatat setiap bulan? | Jumlahkan nominal catatan pengeluaran pada bulan yang sama. |
| PB-03 | Berapa selisih tiap bulan? | Kurangi pengeluaran dari pemasukan dalam periode yang sama. |
| PB-04 | Kapan jumlah transaksi penjualan tertinggi? | Hitung ID nota unik per tanggal dan tampilkan semua tanggal yang berbagi nilai tertinggi. |
| PB-05 | Menu apa yang paling banyak terjual pada periode pilihan? | Jumlahkan unit terjual per menu pada bulan yang dipilih. |

## Sumber dan hasil pembersihan data

Data raw dan daftar referensi 23 menu berasal dari `Dataset_Agentris_RAW_Lengkap.zip`. Mufid membersihkan data simulasi penjualan dan pengeluaran untuk Agustus–Oktober 2026. Satu nota penjualan bisa berisi beberapa menu, sehingga jumlah baris penjualan berbeda dari jumlah nota.

| Dataset sintetis | Baris awal | Duplikat dihapus | Baris dikarantina | Baris bersih |
| :--- | ---: | ---: | ---: | ---: |
| Penjualan | 2.694 | 43 | 78 | 2.573 |
| Pengeluaran | 471 | 7 | 7 | 457 |

Data bersih mencakup 1.148 nota penjualan dan 457 catatan pengeluaran. Laporan mencatat 26 pemeriksaan yang lulus, termasuk format tanggal, ID unik, kecocokan harga menu, dan kesesuaian subtotal dengan total nota. [Ringkasan cleaning](reports/cleaning_summary.csv) · [Laporan validasi](reports/validation_report.csv).

Sumber primer terdiri dari 11 entri pemasukan dan 13 entri pengeluaran dari catatan WhatsApp, dengan total acuan masing-masing Rp285.000 dan Rp269.000. Tanggal lengkap dan rincian menu per penjualan belum cukup untuk rekap aktual pada periode yang sama. Data primer disimpan terpisah dari CSV simulasi.

## Exploratory Data Analysis

Notebook 04 memeriksa struktur data, cakupan tanggal, distribusi, dan hubungan antarvariabel. Aturan IQR menandai 55 nota penjualan dan 11 pengeluaran simulasi. Nilai tersebut ditinjau berdasarkan jumlah unit dan jenis belanja, lalu tetap dipakai dalam rekap. [Notebook EDA](notebooks/04_exploratory_data_analysis.ipynb).

## Analisis dan rekomendasi untuk warung

Tabel berikut merangkum hasil simulasi. Selisih menunjukkan uang masuk dikurangi uang keluar yang tercatat.

| Bulan | Pemasukan | Pengeluaran | Selisih tercatat |
| :--- | ---: | ---: | ---: |
| Agustus 2026 | Rp9.193.000 | Rp3.879.000 | Rp5.314.000 |
| September 2026 | Rp8.795.500 | Rp3.051.500 | Rp5.744.000 |
| Oktober 2026 | Rp8.501.500 | Rp3.691.500 | Rp4.810.000 |

Pada data uji, jumlah tertinggi adalah 20 nota sehari pada 7, 10, 11, dan 16 Oktober 2026. Pada bulan yang sama, soto ayam menempati posisi pertama dengan 115 unit terjual. Angka ini menjelaskan cara membaca rekap. Hasil penjualan warung perlu dihitung dari transaksi nyata yang lengkap.

Saran untuk Pak Tommy adalah mencatat tanggal dan nominal pemasukan serta belanja secara rutin, menyimpan nama menu dan jumlahnya pada setiap nota, dan mencatat hari tutup. Setelah catatan nyata cukup lengkap, rekap menu dapat membantu menyiapkan stok bahan, sedangkan jumlah nota per hari bisa membantu menyusun jadwal persiapan. [Notebook analisis dan rekomendasi](notebooks/05_analisis_dan_rekomendasi.ipynb).

## Cara menjalankan

Dari folder akar repo, aktifkan lingkungan Python dan pasang dependensi.

```bash
python -m pip install -r data-science/requirements.txt
```

Buka folder `data-science/notebooks` di VS Code atau Jupyter. Pakai kernel dari lingkungan Python yang sama, lalu pilih Run All pada notebook 04 atau 05. Keduanya membaca langsung CSV bersih di `datasets/processed`. Di notebook 05, `BULAN` menentukan bulan untuk peringkat menu.

| Notebook | Isi |
| :--- | :--- |
| [01 · Pengumpulan dan pemeriksaan awal](notebooks/01_data_collection_assessment.ipynb) | Sumber, struktur, dan keterbatasan data. |
| [02 · Pembersihan dan transformasi](notebooks/02_data_cleaning_transformation.ipynb) | Normalisasi, penanganan duplikasi, dan ekspor kandidat. |
| [03 · Validasi data](notebooks/03_data_validation.ipynb) | Pemeriksaan kandidat dan ekspor CSV yang lulus setelah verifikasi log perubahan dan karantina. |
| [04 · Exploratory Data Analysis](notebooks/04_exploratory_data_analysis.ipynb) | Profil data, distribusi, IQR, dan pola penjualan harian. |
| [05 · Analisis dan rekomendasi](notebooks/05_analisis_dan_rekomendasi.ipynb) | Lima pertanyaan bisnis, tiga grafik Seaborn, uji rekap, dan saran untuk warung. |

Jalankan 01–03 berurutan jika ingin mengulang proses pengolahan data. Setelah mengubah data atau aturan pembersihan, periksa ulang laporan validasi sebelum memakai CSV hasilnya di notebook 04 dan 05.

## Direktori dan acuan

- `datasets/raw` menyimpan catatan yang diterima dan data simulasi sebelum dibersihkan.
- `datasets/reference` menyimpan daftar menu warung.
- `datasets/interim` menyimpan kandidat, karantina, dan log perubahan.
- `datasets/processed` menyimpan dua CSV simulasi yang telah lulus validasi.
- `reports` menyimpan ringkasan pemeriksaan awal, pembersihan, dan validasi.

[Project Plan](https://docs.google.com/document/d/1UcQiyXj9haOqE3SA-vJlvonQcbb9T-EVeyxwEkJByoE/edit?tab=t.dt3ov0qga5qj) · [Wawancara dan Use Case](https://docs.google.com/document/d/1GBdc-kcfjPI32mygfm4fEtqxjs0U5G0uu0xoefymtIU/edit?tab=t.zd0fojid3xfk) · [Asah Capstone Playbook](https://docs.google.com/document/d/1JeUlc-66WRNdwm8gQ1PQF1VZ8AArca48sI982I1Z00A/edit?tab=t.0)
