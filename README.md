# 💻 Sistem Pakar Diagnosa Penyakit ISPA

**Metode:** Forward Chaining & Logika Fuzzy
**Bahasa Pemrograman:** Python
**Tampilan:** GUI berbasis Tkinter + Export PDF

---

## 🧠 Deskripsi Singkat

Program ini adalah implementasi kecerdasan buatan (AI) yang menggabungkan **Sistem Pakar** berbasis rule dan **Logika Fuzzy** untuk mendiagnosis penyakit ISPA berdasarkan gejala yang dirasakan pengguna.

---

## 🔧 Teknologi & Library yang Digunakan

| Library        | Fungsi                                       |
| -------------- | -------------------------------------------- |
| `tkinter`      | GUI (interface user: form, checkbox, tombol) |
| `reportlab`    | Export hasil diagnosa ke PDF                 |
| `scikit-fuzzy` | Logika fuzzy untuk menilai tingkat keparahan |
| `json`         | Menyimpan rules/aturan sistem pakar          |
| `datetime`     | Mencatat waktu diagnosa dan export           |
| `os`           | Manajemen file & folder                      |

---

## 📂 Struktur Folder

```
sistem-pakar-ispa/
│
├── main.py               # Versi CLI
├── gui_app.py            # GUI utama
├── rules.json            # Aturan sistem pakar
├── output/               # Tempat file PDF tersimpan
└── utils/
    ├── rule_engine.py    # Logika forward chaining
    ├── fuzzy_logic.py    # Sistem fuzzy
    ├── pdf_export.py     # Export PDF
    └── utils.py          # Fungsi bantu (CLI)
```

---

## 🔄 Cara Kerja Program

### 1. Input dari Pengguna (GUI)

- Nama pasien
- Gejala (checkbox)
- Suhu tubuh (35–42 °C)
- Durasi sakit (0–14 hari)
- Intensitas batuk (0–10)

### 2. Diagnosa: Forward Chaining

- Gejala yang dipilih dicocokkan dengan **aturan (rules)** di file `rules.json`
- Jika cocok, hasil diagnosa dan saran ditampilkan

### 3. Fuzzy Logic

- Input numerik (suhu, durasi, batuk) diproses menggunakan fuzzy
- Output berupa tingkat keparahan: **Rendah**, **Sedang**, atau **Tinggi**

### 4. Export PDF (opsional)

- Hasil diagnosa dapat disimpan sebagai file PDF otomatis

---

## 📄 Penjelasan File `rules.json`

File `rules.json` berisi **aturan diagnosis penyakit** dalam bentuk struktur JSON array. Setiap rule memiliki 3 bagian:

```json
{
  "conditions": ["demam", "batuk", "pilek"],
  "diagnosis": "ISPA Ringan",
  "advice": "Istirahat cukup, minum air hangat, dan hindari udara dingin."
}
```

### Penjelasan:

- `"conditions"`: List gejala yang harus dimiliki pengguna agar rule ini cocok
- `"diagnosis"`: Hasil diagnosa jika rule ini terpenuhi
- `"advice"`: Saran penanganan untuk diagnosa tersebut

---

## 🖼️ Tampilan Program (GUI)

- Form input nama & suhu
- Checkbox gejala
- Input durasi & batuk
- Tombol **Diagnosa**
- Output hasil di bawahnya
- Tombol **Simpan ke PDF**

---

## ✅ Keunggulan Program

- 🔍 Akurat karena menggunakan kombinasi _rule-based_ dan _logika fuzzy_
- 🖥️ Bisa digunakan tanpa perlu coding (GUI interaktif)
- 💾 Menyimpan hasil ke PDF otomatis
- 📚 Dapat dikembangkan untuk penyakit lain (cukup ganti `rules.json`)

---

## 📌 Contoh Output PDF

```text
LAPORAN HASIL DIAGNOSA ISPA

Nama Pasien     : Ferdy Rahmat Ramdani Ramdani
Gejala          : demam, batuk, pilek
Diagnosa        : ISPA Ringan
Keparahan Fuzzy : Sedang (57.4)
Saran           : Istirahat cukup, perbanyak minum, konsultasi jika tak membaik
```

---

## 📎 Catatan Tambahan

- Program bisa dikembangkan menjadi aplikasi mobile/web
- Rule di `rules.json` bisa ditambahkan sesuai kebutuhan
- Sistem fuzzy bisa dikembangkan untuk mempertimbangkan lebih banyak faktor (misalnya usia pasien)

---

Kalau kamu mau, saya juga bisa bantu export ini ke file `README.md` atau `deskripsi_proyek.md`. Mau dibuatkan juga?
