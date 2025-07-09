import json
import os

def load_rules(file_path=None):
    """Membaca dan memuat aturan dari file JSON di root project"""
    if file_path is None:
        # Ambil path relatif dari root project
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(base_dir, "rules.json")

    with open(file_path, "r") as file:
        return json.load(file)

def forward_chaining(user_symptoms, rules):
    """
    Menjalankan forward chaining untuk mencocokkan gejala user
    dengan rule yang ada dalam sistem pakar.
    """
    matched_rules = []

    for rule in rules:
        if all(symptom in user_symptoms for symptom in rule["conditions"]):
            matched_rules.append({
                "diagnosis": rule["diagnosis"],
                "advice": rule["advice"],
                "matched_conditions": rule["conditions"]
            })

    if not matched_rules:
        return {
            "diagnosis": "Tidak diketahui",
            "advice": "Gejala yang Anda masukkan tidak cukup untuk diagnosis. Silakan periksa kembali atau konsultasi ke dokter.",
            "matched_conditions": []
        }
    
    # Return rule dengan kondisi terbanyak yang cocok
    return max(matched_rules, key=lambda x: len(x["matched_conditions"]))
