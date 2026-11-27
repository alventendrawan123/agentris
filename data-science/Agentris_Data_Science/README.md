# Agentris — Data Science (A26-CS193)
Soto Batok & Penyetan Pak Tris.

## Cara menjalankan
Ekstrak ZIP, buka folder proyek di VS Code/Jupyter. Buat virtual environment bila perlu, jalankan `pip install -r requirements.txt`, pilih kernel Python, kemudian buka notebook berurutan 01–04.

- 01: collection & assessment, bisa langsung dijalankan.
- 02: kerangka cleaning dengan TODO; pengguna mengisi solusi, mengaktifkan ekspor kandidat setelah selesai.
- 03: pemeriksaan skema, nilai, harga, ID, subtotal, total dan rekonsiliasi; aktifkan review manual setelah mengecek log. Ekspor hanya ketika validasi lulus. Jika mengulang cleaning, jangan gunakan hasil processed lama sebelum validasi ulang.
- 04: EDA lima pertanyaan bisnis, menggunakan hasil processed. Ubah BULAN pada PB-05 sesuai kebutuhan.

## Dataset
File CSV raw/reference disalin tanpa perubahan dari Dataset_Agentris_RAW_Lengkap.zip. Penjualan gabungan 2694 baris (9 kolom), pengeluaran sintetis 471, penjualan primer 11, pengeluaran primer 13, menu 23. Simulasi Agustus–Oktober 2026. Satu transaksi bisa memiliki beberapa item; total_transaksi berulang. Hitung pemasukan dari subtotal tervalidasi dan frekuensi transaksi dari ID unik.

Data primer terpisah, jangan mengarang tanggal atau item yang hilang. Penjualan primer total acuan Rp285.000, pengeluaran primer Rp269.000 (konfirmasi skala ribuan). Jangan gunakan untuk rekap bulanan hingga tanggal lengkap terkonfirmasi. Data sintetis bukan data aktual. Tidak ada target machine learning/prediksi penjualan dalam pekerjaan ini.

## Direktori
- datasets/raw: data asli, jangan edit.
- datasets/reference: daftar harga menu UMKM.
- datasets/interim: kandidat cleaning, reject_log dan change_log.
- datasets/processed: CSV yang lulus validasi (kosong saat diserahkan).
- reports: ringkasan assessment, validasi, rekap dan grafik hasil EDA.

## Acuan
[Project Plan](https://docs.google.com/document/d/1UcQiyXj9haOqE3SA-vJlvonQcbb9T-EVeyxwEkJByoE/edit) · [Interview & Use Case](https://docs.google.com/document/d/1GBdc-kcfjPI32mygfm4fEtqxjs0U5G0uu0xoefymtIU/edit) · [Pertanyaan Bisnis](https://docs.google.com/spreadsheets/d/1r84YzGIF4A3hbOdy_7r8MqazMyDEKU-fbrjmSFbH-Ps/edit).
