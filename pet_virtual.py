class Pet:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis
        self.tingkat_lapar = 40  # Skala 0 - 100 (makin tinggi berarti makin lapar)
        self.energi = 70         # Skala 0 - 100 (makin tinggi berarti makin bertenaga)

    def makan(self):
        self.tingkat_lapar -= 25
        if self.tingkat_lapar < 0:
            self.tingkat_lapar = 0
        print(f"[MAKAN] Nyam! {self.nama} si {self.jenis} makan dengan lahap.")

    def bermain(self):
        if self.energi >= 20:
            self.energi -= 20
            self.tingkat_lapar += 15
            print(f"[MAIN] {self.nama} asyik bermain bola dan melompat-lompat!")
        else:
            print(f"[LEMAS] {self.nama} terlalu mengantuk dan lemas untuk diajak main.")

    def tidur(self):
        self.energi += 40
        if self.energi > 100:
            self.energi = 100
        print(f"[TIDUR] Zzz... {self.nama} tidur nyenyak. Energi kembali pulih.")

    def cek_status(self):
        print(f"\n--- KONDISI: {self.nama} ({self.jenis}) ---")
        print(f"Tingkat Lapar : {self.tingkat_lapar}/100")
        print(f"Energi        : {self.energi}/100")
        print("--------------------------------------\n")


# ==========================================
# SIMULASI & PENGUJIAN OBJEK LEBIH PANJANG
# ==========================================

# --- PENGUJIAN 1: Peliharaan Anjing (Milo) ---
print(">>> SIMULASI PELIHARAAN 1 <<<")
pet1 = Pet("Milo", "Anjing")
pet1.cek_status()

# Aktivitas pagi: bermain
pet1.bermain()
pet1.bermain()
pet1.cek_status()

# Aktivitas siang: lapar, lalu diberi makan
pet1.makan()
pet1.cek_status()

# Aktivitas sore: bermain sampai kehabisan tenaga
pet1.bermain()
pet1.bermain()  # Energi tidak cukup, aksi ditolak
pet1.cek_status()

# Aktivitas malam: istirahat tidur
pet1.tidur()
pet1.cek_status()


# --- PENGUJIAN 2: Peliharaan Kucing (Luna) ---
print(">>> SIMULASI PELIHARAAN 2 <<<")
pet2 = Pet("Luna", "Kucing")
pet2.cek_status()

# Luna langsung makan dan tidur di awal
pet2.makan()
pet2.tidur()
pet2.cek_status()

# Luna bertenaga penuh, diajak bermain beberapa kali
pet2.bermain()
pet2.bermain()
pet2.cek_status()