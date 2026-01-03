## 🏗️ Gambaran Umum Arsitektur

Kode pada proyek ini telah direfaktor agar lebih rapi dan mudah dipahami, dengan memisahkan tanggung jawab tiap bagian kode ke dalam file yang berbeda.

Walaupun struktur proyek dibuat sederhana (tanpa banyak folder), setiap file memiliki peran yang jelas. Pemisahan ini bertujuan agar kode:
- Lebih mudah dibaca
- Lebih mudah dirawat
- Lebih mudah dikembangkan ke depannya

Pendekatan ini dipilih agar tetap sesuai dengan skala aplikasi dan tidak berlebihan untuk exercise ini.

---

## 📄 Penjelasan Tiap File

Walaupun hanya terdiri dari beberapa file `.py`, masing-masing file memiliki tanggung jawab yang berbeda.

### `api.py` — Endpoint API

File ini berisi:
- Definisi endpoint FastAPI
- Penanganan request dan response
- Validasi input dari user

File ini hanya mengurus komunikasi HTTP dan tidak berisi logika utama aplikasi.

---

### `models.py` — Model Data

File ini berisi model Pydantic yang digunakan untuk:
- Validasi data input
- Menentukan struktur data request dan response

Dengan memisahkan model data, struktur input menjadi lebih jelas dan mudah diubah jika dibutuhkan.

---

### `rag.py` — Alur Logika Aplikasi

File ini berisi logika utama aplikasi RAG:
- Menjalankan proses pencarian data (retrieve)
- Menghasilkan jawaban (answer)
- Mengatur alur kerja menggunakan LangGraph

File ini fokus pada alur aplikasi dan tidak bergantung langsung pada FastAPI atau database tertentu.

---

### `embeddings.py` — Embedding Service

File ini bertugas mengubah teks menjadi vektor embedding.

Pemisahan ini membuat kode lebih fleksibel, sehingga metode embedding dapat diganti di kemudian hari tanpa mengubah bagian lain dari aplikasi.

---

### `store.py` — Penyimpanan Data

File ini mengatur cara menyimpan dan mengambil dokumen:
- Menggunakan Qdrant jika tersedia
- Menggunakan penyimpanan in-memory sebagai fallback

Dengan cara ini, aplikasi tetap bisa berjalan walaupun database eksternal tidak tersedia.

---

### `main.py` — Inisialisasi Aplikasi

File ini adalah titik awal aplikasi:
- Menginisialisasi semua komponen
- Menghubungkan antar bagian aplikasi
- Menjalankan FastAPI

File ini tidak berisi logika bisnis, hanya mengatur bagaimana aplikasi dijalankan.

---

## 🎯 Alasan Pemisahan Kode

Pemisahan kode dilakukan agar setiap file memiliki satu tanggung jawab utama:

- Endpoint API → `api.py`
- Struktur data → `models.py`
- Alur aplikasi → `rag.py`
- Metode embedding → `embeddings.py`
- Penyimpanan data → `store.py`
- Konfigurasi aplikasi → `main.py`

Dengan pendekatan ini, perubahan pada satu bagian tidak memengaruhi bagian lain.

---

## ✅ Kesimpulan

Refactor ini bertujuan untuk membuat kode:
- Lebih mudah dibaca dan dipahami
- Lebih terstruktur
- Lebih siap untuk dikembangkan


Struktur dibuat sederhana dan proporsional dengan kebutuhan exercise, tanpa menambahkan fitur baru atau kompleksitas yang tidak diperlukan.
