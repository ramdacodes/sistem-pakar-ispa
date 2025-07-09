from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from datetime import datetime
import os

def generate_pdf(
    filename="hasil_diagnosa.pdf",
    nama_user="Pasien",
    gejala=[],
    diagnosis="Tidak diketahui",
    saran="-",
    keparahan="Rendah"
):
    # Folder output
    output_dir = os.path.join(os.getcwd(), "output")
    os.makedirs(output_dir, exist_ok=True)

    file_path = os.path.join(output_dir, filename)
    c = canvas.Canvas(file_path, pagesize=A4)
    width, height = A4

    # ==================== HEADER ====================
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width / 2, height - 50, "LAPORAN HASIL DIAGNOSA ISPA")

    c.setLineWidth(1)
    c.setStrokeColor(colors.grey)
    c.line(50, height - 60, width - 50, height - 60)

    c.setFont("Helvetica", 10)
    c.drawString(50, height - 80, f"Tanggal Cetak: {datetime.now().strftime('%d %B %Y, %H:%M')}")

    # ==================== INFORMASI PASIEN ====================
    y = height - 120
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Informasi Pasien")
    c.setFont("Helvetica", 11)
    y -= 20
    c.drawString(60, y, f"Nama: {nama_user}")
    y -= 20
    c.drawString(60, y, f"Gejala: {', '.join(gejala)}")

    # ==================== HASIL DIAGNOSA ====================
    y -= 40
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Hasil Diagnosa")
    c.setFont("Helvetica", 11)
    y -= 20
    c.drawString(60, y, f"Diagnosa: {diagnosis}")
    y -= 20
    c.drawString(60, y, f"Tingkat Keparahan (Fuzzy): {keparahan}")

    # ==================== SARAN ====================
    y -= 40
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Saran Penanganan")
    y -= 20
    text = c.beginText(60, y)
    text.setFont("Helvetica", 11)
    text.setLeading(16)  # jarak antar baris
    for line in saran.split('\n'):
        text.textLine(line)
    c.drawText(text)

    # ==================== TANDA TANGAN ====================
    y = 150
    c.setFont("Helvetica", 11)
    c.drawString(width - 200, y, "Petugas Diagnosa")
    c.line(width - 200, y - 5, width - 80, y - 5)
    c.drawString(width - 200, y - 20, "(...................................)")

    # ==================== FOOTER ====================
    c.setFont("Helvetica-Oblique", 9)
    c.setFillColor(colors.grey)
    c.drawString(50, 40, "Dokumen ini dicetak otomatis oleh Sistem Pakar ISPA - Kecerdasan Buatan")

    c.save()
    return file_path
