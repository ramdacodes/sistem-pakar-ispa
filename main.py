from utils.utils import (
    print_header, print_colored,
    input_float, input_int, input_list_gejala
)

from utils.rule_engine import load_rules, forward_chaining
from utils.fuzzy_logic import evaluate_fuzzy
from utils.pdf_export import generate_pdf

def main():
    print_header("Sistem Pakar Diagnosa ISPA")

    # 1. Input dari user
    nama_user = input("Masukkan nama Anda: ")
    gejala_user = input_list_gejala("Masukkan gejala (pisahkan dengan koma): ")
    suhu = input_float("Masukkan suhu tubuh (°C): ", 35.0, 42.0)
    durasi = input_int("Berapa hari sakit berlangsung?: ", 0, 14)
    batuk = input_int("Seberapa parah batuk? (0–10): ", 0, 10)

    # 2. Forward chaining (diagnosa)
    rules = load_rules()
    hasil = forward_chaining(gejala_user, rules)

    # 3. Fuzzy logic (keparahan)
    keparahan, nilai_fuzzy = evaluate_fuzzy(suhu, durasi, batuk)

    # 4. Tampilkan hasil ke layar
    print_header("HASIL DIAGNOSA")
    print_colored(f"Nama: {nama_user}", "cyan")
    print_colored(f"Gejala: {', '.join(gejala_user)}", "cyan")
    print_colored(f"Diagnosa: {hasil['diagnosis']}", "green")
    print_colored(f"Tingkat Keparahan (Fuzzy): {keparahan} ({nilai_fuzzy:.2f})", "yellow")
    print_colored(f"Saran: {hasil['advice']}", "blue")

    # 5. Export ke PDF?
    simpan = input("\nIngin simpan hasil diagnosa ke PDF? (y/n): ").strip().lower()
    if simpan == "y":
        filename = f"diagnosa_{nama_user.lower().replace(' ', '_')}.pdf"
        file_path = generate_pdf(
            filename=filename,
            nama_user=nama_user,
            gejala=gejala_user,
            diagnosis=hasil["diagnosis"],
            saran=hasil["advice"],
            keparahan=keparahan
        )
        print_colored(f"\n✅ Hasil telah disimpan ke: {file_path}", "green")
    else:
        print_colored("❌ Tidak disimpan ke PDF.", "red")

if __name__ == "__main__":
    main()
