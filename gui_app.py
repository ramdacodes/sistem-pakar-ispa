import tkinter as tk
from tkinter import messagebox
from utils.rule_engine import load_rules, forward_chaining
from utils.fuzzy_logic import evaluate_fuzzy
from utils.pdf_export import generate_pdf
from datetime import datetime

# Daftar gejala yang tersedia
GEJALA_LIST = [
    "demam", "batuk", "pilek", "sakit tenggorokan",
    "sesak napas", "sakit kepala"
]

class ISPAApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Pakar Diagnosa ISPA - GUI")
        self.root.geometry("800x800")
        self.root.resizable(False, False)

        self.rules = load_rules()
        self.gejala_vars = {}
        
        self.build_interface()

    def build_interface(self):
        # Nama
        tk.Label(self.root, text="Nama Anda:", font=("Arial", 12)).pack()
        self.nama_entry = tk.Entry(self.root, font=("Arial", 12))
        self.nama_entry.pack(pady=5)

        # Gejala
        tk.Label(self.root, text="Pilih Gejala yang Dirasakan:", font=("Arial", 12, "bold")).pack(pady=5)
        for gejala in GEJALA_LIST:
            var = tk.BooleanVar()
            cb = tk.Checkbutton(self.root, text=gejala.capitalize(), variable=var, font=("Arial", 11))
            cb.pack(anchor="w", padx=50)
            self.gejala_vars[gejala] = var

        # Input lainnya
        self.suhu_entry = self.labeled_input("Suhu tubuh (°C):")
        self.durasi_entry = self.labeled_input("Durasi sakit (hari):")
        self.batuk_entry = self.labeled_input("Intensitas batuk (0–10):")

        # Tombol
        tk.Button(self.root, text="Diagnosa", font=("Arial", 12, "bold"),
                  bg="#4CAF50", fg="white", command=self.diagnosa).pack(pady=10)

        self.output_text = tk.Text(self.root, height=10, font=("Arial", 11))
        self.output_text.pack(pady=5)

        tk.Button(self.root, text="Simpan ke PDF", font=("Arial", 11),
                  command=self.simpan_pdf).pack(pady=5)

    def labeled_input(self, label, default=""):
        tk.Label(self.root, text=label, font=("Arial", 12)).pack()
        entry = tk.Entry(self.root, font=("Arial", 12))
        entry.insert(0, default)
        entry.pack(pady=2)
        return entry

    def diagnosa(self):
        nama = self.nama_entry.get().strip()
        if not nama:
            messagebox.showwarning("Validasi", "Nama tidak boleh kosong.")
            return

        try:
            suhu = float(self.suhu_entry.get())
            durasi = int(self.durasi_entry.get())
            batuk = int(self.batuk_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Input suhu, durasi, dan batuk harus berupa angka.")
            return

        # Ambil gejala yang dipilih
        gejala_user = [g for g, var in self.gejala_vars.items() if var.get()]
        if not gejala_user:
            messagebox.showwarning("Validasi", "Pilih minimal satu gejala.")
            return

        # Diagnosa & fuzzy
        hasil = forward_chaining(gejala_user, self.rules)
        keparahan, nilai_fuzzy = evaluate_fuzzy(suhu, durasi, batuk)

        # Simpan untuk PDF nanti
        self.last_result = {
            "nama": nama,
            "gejala": gejala_user,
            "diagnosis": hasil["diagnosis"],
            "saran": hasil["advice"],
            "keparahan": f"{keparahan} ({nilai_fuzzy:.2f})"
        }

        # Tampilkan
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, f"Nama: {nama}\n")
        self.output_text.insert(tk.END, f"Gejala: {', '.join(gejala_user)}\n")
        self.output_text.insert(tk.END, f"Hasil Diagnosa: {hasil['diagnosis']}\n")
        self.output_text.insert(tk.END, f"Tingkat Keparahan (Fuzzy): {keparahan} ({nilai_fuzzy:.2f})\n")
        self.output_text.insert(tk.END, f"Saran: {hasil['advice']}\n")

    def simpan_pdf(self):
        if not hasattr(self, 'last_result'):
            messagebox.showinfo("Info", "Silakan lakukan diagnosa terlebih dahulu.")
            return

        file_path = generate_pdf(
            filename=f"diagnosa_{self.last_result['nama'].lower().replace(' ', '_')}-{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.pdf",
            nama_user=self.last_result['nama'],
            gejala=self.last_result['gejala'],
            diagnosis=self.last_result['diagnosis'],
            saran=self.last_result['saran'],
            keparahan=self.last_result['keparahan']
        )
        messagebox.showinfo("Berhasil", f"Hasil diagnosa disimpan ke:\n{file_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ISPAApp(root)
    root.mainloop()
