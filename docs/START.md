# Panduan Memulai (Getting Started) — Agentris

Dokumen ini menjelaskan struktur monorepo **Agentris**, pembagian tanggung jawab tiap tim, serta langkah-langkah yang perlu dilakukan saat pertama kali `git clone` maupun saat melakukan `git pull` pembaruan.

---

## 1. Struktur Monorepo & Pembagian Tim

```text
agentris/
├── apps/
│   ├── client/              # [FS] Frontend (React + Vite + Tailwind CSS)
│   │   ├── src/
│   │   │   ├── apis/
│   │   │   ├── components/
│   │   │   ├── hooks/
│   │   │   ├── pages/
│   │   │   ├── utils/
│   │   │   ├── App.jsx
│   │   │   ├── index.css
│   │   │   └── main.jsx
│   │   ├── index.html
│   │   ├── package.json
│   │   └── vite.config.js
│   │
│   ├── server/              # [FS] Backend API (Node.js + Express + PostgreSQL)
│   │   ├── src/
│   │   │   ├── controllers/
│   │   │   ├── exceptions/
│   │   │   ├── middlewares/
│   │   │   ├── routes/
│   │   │   ├── services/
│   │   │   ├── utils/
│   │   │   └── index.js
│   │   ├── .env
│   │   └── package.json
│   │
│   └── ai-service/          # [AE] AI Service (Python)
│       ├── app/
│       ├── .env
│       └── requirements.txt
│
├── data-science/            # [DS] Eksperimen Data, Dataset & Notebook
│   ├── data/
│   └── notebooks/
│
├── docs/                    # Dokumentasi project
└── README.md
```

### Pembagian Bagian

| Tim | Folder | Tech Stack & Isi Utama |
| :--- | :--- | :--- |
| **FS (Full-Stack)** | `apps/client` & `apps/server` | Frontend React + Vite + Tailwind CSS (`client`) dan Backend Express + PostgreSQL (`server`). |
| **AE (AI Engineer)** | `apps/ai-service` | Service AI berbasis Python (`app/`, `requirements.txt`, `.env`). |
| **DS (Data Science)** | `data-science` | Pengolahan data dan notebook eksperimen (`data/`, `notebooks/`). |
| **Semua Tim** | `docs` | Dokumentasi bersama (termasuk panduan ini). |

---

## 2. Prasyarat

Pastikan perangkat sudah terpasang:
- **Git**
- **Node.js (LTS)** & **npm** — wajib untuk bagian **FS** (`apps/client` & `apps/server`)
- **Python 3.12+** & **pip** — wajib untuk bagian **AE** (`apps/ai-service`) & **DS** (`data-science`)

---

## 3. Langkah Awal Setelah `git clone`

### A. Clone Repository
```bash
git clone <URL_REPOSITORY>
cd agentris
```

### B. Amankan File `.env` Sebelum Mengisi Kredensial
Di repository ini, `apps/server/.env` dan `apps/ai-service/.env` ikut di-commit dalam keadaan **kosong** sebagai template struktur awal.

> **Penting:** Karena file `.env` tersebut sudah ter-track oleh Git, sekadar menambahkan `.env` ke `.gitignore` setelah clone **tidak otomatis menghentikan Git melacak perubahannya**.

Sebelum mengisi API key, password database, atau secret apa pun di `.env`, pilih salah satu langkah berikut:

1. **Abaikan perubahan `.env` di lokal masing-masing** *(tanpa mengubah riwayat Git)*:
   ```bash
   git update-index --skip-worktree apps/server/.env apps/ai-service/.env
   ```
   *(Jika nanti perlu melacak ulang, gunakan `--no-skip-worktree`.)*

2. **Hentikan pelacakan `.env` untuk seluruh repo** *(jika tim sepakat menghapus `.env` dari index Git)*:
   Tambahkan `.env` ke `.gitignore`, lalu jalankan:
   ```bash
   git rm --cached apps/server/.env apps/ai-service/.env
   ```

### C. Setup per Bagian

#### 1. FS — Frontend (`apps/client`)
```bash
cd apps/client
npm install
npm run dev
```
Perintah lain yang tersedia di `apps/client`:
- `npm run lint` — cek ESLint
- `npm run build` — build produksi Vite

#### 2. FS — Backend (`apps/server`)
```bash
cd apps/server
npm install
```
Isi variabel environment yang dibutuhkan di `apps/server/.env` (setelah mengamankan tracking Git di langkah B), lalu jalankan server:
```bash
node src/index.js
```
Atau dengan auto-reload selama pengembangan menggunakan `nodemon`:
```bash
npx nodemon src/index.js
```
*(Catatan: script `"dev"` / `"start"` belum ditambahkan di `apps/server/package.json`.)*

#### 3. AE — AI Service (`apps/ai-service`)
```bash
cd apps/ai-service
python -m venv venv
```
Aktifkan virtual environment:
- **Windows (PowerShell):**
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```
- **Windows (CMD):**
  ```cmd
  venv\Scripts\activate.bat
  ```
- **macOS / Linux:**
  ```bash
  source venv/bin/activate
  ```

Setelah `venv` aktif, install dependency dan isi `apps/ai-service/.env`:
```bash
pip install -r requirements.txt
```

#### 4. DS — Data Science (`data-science`)
```bash
cd data-science
python -m venv venv
```
Aktifkan `venv` (cara sama seperti di atas), lalu install library analisis/notebook yang dibutuhkan (atau jalankan `pip install -r requirements.txt` apabila file `requirements.txt` sudah tersedia di folder ini).

---

## 4. Langkah Saat `git pull` Pembaruan

Setiap kali menarik perubahan terbaru dari remote:

```bash
git pull
```

Perhatikan file apa saja yang berubah pada output `git pull`:

1. **Jika `apps/client/package.json` atau `apps/client/package-lock.json` berubah:**
   ```bash
   cd apps/client
   npm install
   ```
2. **Jika `apps/server/package.json` atau `apps/server/package-lock.json` berubah:**
   ```bash
   cd apps/server
   npm install
   ```
3. **Jika `apps/ai-service/requirements.txt` berubah:**
   Pastikan `venv` di `apps/ai-service` sudah aktif, lalu jalankan:
   ```bash
   cd apps/ai-service
   pip install -r requirements.txt
   ```
4. **Jika hanya file kode yang berubah** (`.jsx`, `.js`, `.css`, `.py`, `.ipynb`, `.md`, dll.):
   **Tidak perlu** menjalankan `npm install` atau `pip install` ulang—langsung jalankan aplikasi seperti biasa.
5. **Jika ada penambahan variabel environment baru:**
   Periksa pengumuman tim atau dokumentasi terkait, lalu tambahkan variabel barunya ke `.env` lokal masing-masing.

---

## 5. Aturan Singkat Sebelum `git commit` & `git push`

- **Jangan pernah commit** folder `node_modules/`, `venv/`, `.venv/`, `__pycache__/`, `dist/`, maupun file `.env` yang sudah berisi kredensial/API key.
- Jika kamu menambahkan library baru:
  - **FS:** pastikan `package.json` dan `package-lock.json` ikut di-commit.
  - **AE / DS:** pastikan `requirements.txt` diperbarui (mis. `pip freeze > requirements.txt`) dan ikut di-commit agar anggota tim lain bisa langsung sinkron.
