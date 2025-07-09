import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Definisi variabel input
suhu = ctrl.Antecedent(np.arange(35, 42.1, 0.1), 'suhu')
durasi = ctrl.Antecedent(np.arange(0, 15, 1), 'durasi')
batuk = ctrl.Antecedent(np.arange(0, 11, 1), 'batuk')

# Output: tingkat keparahan
keparahan = ctrl.Consequent(np.arange(0, 101, 1), 'keparahan')

# Membership function suhu
suhu['rendah'] = fuzz.trimf(suhu.universe, [35, 35, 36.5])
suhu['normal'] = fuzz.trimf(suhu.universe, [36, 37, 38])
suhu['tinggi'] = fuzz.trimf(suhu.universe, [37.5, 40, 42.5])

# Membership function durasi sakit
durasi['sebentar'] = fuzz.trimf(durasi.universe, [0, 1, 3])
durasi['sedang'] = fuzz.trimf(durasi.universe, [2, 5, 8])
durasi['lama'] = fuzz.trimf(durasi.universe, [7, 10, 14])

# Membership function batuk
batuk['ringan'] = fuzz.trimf(batuk.universe, [0, 2, 4])
batuk['sedang'] = fuzz.trimf(batuk.universe, [3, 5, 7])
batuk['berat'] = fuzz.trimf(batuk.universe, [6, 8, 10])

# Membership function keparahan
keparahan['rendah'] = fuzz.trimf(keparahan.universe, [0, 25, 50])
keparahan['sedang'] = fuzz.trimf(keparahan.universe, [30, 50, 70])
keparahan['tinggi'] = fuzz.trimf(keparahan.universe, [60, 80, 100])

# Aturan fuzzy
rule1 = ctrl.Rule(suhu['normal'] & durasi['sebentar'] & batuk['ringan'], keparahan['rendah'])
rule2 = ctrl.Rule(suhu['tinggi'] & durasi['sedang'] & batuk['sedang'], keparahan['sedang'])
rule3 = ctrl.Rule(suhu['tinggi'] & durasi['lama'] & batuk['berat'], keparahan['tinggi'])
rule4 = ctrl.Rule(suhu['tinggi'] & batuk['berat'], keparahan['tinggi'])
rule5 = ctrl.Rule(suhu['normal'] & durasi['lama'] & batuk['sedang'], keparahan['sedang'])
rule6 = ctrl.Rule(suhu['rendah'] & batuk['ringan'], keparahan['rendah'])
rule7 = ctrl.Rule(suhu['tinggi'], keparahan['tinggi'])
rule8 = ctrl.Rule(suhu['tinggi'] & batuk['sedang'], keparahan['sedang'])

# Controller dan sistem inferensi
keparahan_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8])
keparahan_simulasi = ctrl.ControlSystemSimulation(keparahan_ctrl)

def evaluate_fuzzy(input_suhu, input_durasi, input_batuk):
    if not (35 <= input_suhu <= 42):
        raise ValueError("Suhu tubuh harus antara 35–42 °C")
    if not (0 <= input_durasi <= 14):
        raise ValueError("Durasi sakit harus antara 0–14 hari")
    if not (0 <= input_batuk <= 10):
        raise ValueError("Intensitas batuk harus antara 0–10")

    simulasi = ctrl.ControlSystemSimulation(keparahan_ctrl)
    simulasi.input['suhu'] = input_suhu
    simulasi.input['durasi'] = input_durasi
    simulasi.input['batuk'] = input_batuk

    try:
        simulasi.compute()
        nilai = simulasi.output['keparahan']
        print(f"[DEBUG] Hasil keparahan: {nilai}")
    except Exception as e:
        raise RuntimeError("Fuzzy inference gagal: " + str(e))

    if nilai < 40:
        tingkat = "Rendah"
    elif 40 <= nilai < 70:
        tingkat = "Sedang"
    else:
        tingkat = "Tinggi"

    return tingkat, nilai



