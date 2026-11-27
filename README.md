# Agentris

Agentris membantu Pak Tommy mencatat transaksi Soto Batok & Penyetan Pak Tris dan melihat rekap usaha lewat dasbor serta chat.

Untuk menyiapkan aplikasi, ikuti [panduan memulai](docs/START.md).

## Hasil Data Science

- **Rumusan masalah dan pertanyaan bisnis.** Catatan uang masuk dan belanja perlu direkap pada periode yang sama. Tim merumuskan lima pertanyaan tentang pemasukan bulanan, pengeluaran bulanan, selisihnya, tanggal dengan transaksi terbanyak, dan menu terlaris berdasarkan unit terjual. [Buka dokumen pertanyaan bisnis](https://docs.google.com/spreadsheets/d/1r84YzGIF4A3hbOdy_7r8MqazMyDEKU-fbrjmSFbH-Ps/edit).
- **Pembersihan data.** Dari 2.694 baris penjualan dan 471 baris pengeluaran sintetis, proses pembersihan menghasilkan 2.573 detail penjualan dari 1.148 nota dan 457 catatan pengeluaran. Hasilnya melewati 26 pemeriksaan dalam [laporan validasi](data-science/reports/validation_report.csv).
- **Analisis dan rekomendasi untuk warung.** Pada simulasi Oktober 2026, pemasukan tercatat Rp8.501.500 dan pengeluaran Rp3.691.500, sehingga selisihnya Rp4.810.000. Soto ayam menempati posisi pertama dengan 115 unit. Agar rekap dapat dipakai untuk keputusan warung, Pak Tommy perlu mencatat pemasukan dan biaya secara rutin serta menyimpan nama menu dan jumlahnya pada setiap nota. [Buka notebook EDA](data-science/notebooks/04_eda_analisis_dan_rekomendasi.ipynb).

Angka di atas menunjukkan cara kerja analisis pada data uji. Lihat hasil tiap bulan, asal data, dan cara menjalankan notebook di [panduan Data Science](data-science/README.md).
