from datetime import datetime

def format_tanggal():
    """Mengembalikan tanggal dan waktu sekarang dalam format string"""
    return datetime.now().strftime('%d-%m-%Y %H:%M')

def print_header(judul):
    """Mencetak judul dengan garis pembatas"""
    print("\n" + "=" * 50)
    print(judul.upper())
    print("=" * 50)

def print_colored(text, color="default"):
    """Mencetak teks berwarna di terminal"""
    colors = {
        "default": "\033[0m",
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "cyan": "\033[96m",
        "bold": "\033[1m"
    }
    reset = "\033[0m"
    print(colors.get(color, colors["default"]) + text + reset)

def input_float(prompt, min_val=0.0, max_val=100.0):
    """Minta input float dengan validasi batas bawah & atas"""
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print_colored(f"Nilai harus antara {min_val} dan {max_val}", "yellow")
        except ValueError:
            print_colored("Masukkan angka desimal yang valid.", "red")

def input_int(prompt, min_val=0, max_val=100):
    """Minta input integer dengan validasi"""
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print_colored(f"Nilai harus antara {min_val} dan {max_val}", "yellow")
        except ValueError:
            print_colored("Masukkan angka bulat yang valid.", "red")

def input_list_gejala(prompt):
    """Minta input list gejala dari user, dipisah koma"""
    teks = input(prompt)
    return [g.strip().lower() for g in teks.split(",") if g.strip()]
