import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

# =======================
# VERİTABANI
# =======================
class BankaSistemi:
    def __init__(self):
        self.conn = sqlite3.connect('banka.db')
        self.cursor = self.conn.cursor()
        self.kurulum_yap()

    def kurulum_yap(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS musteriler (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ad TEXT,
            tip TEXT,
            kimlik_no TEXT,
            bakiye REAL
        )
        """)
        self.conn.commit()

    # Müşteri ekleme
    def musteri_ekle(self, ad, tip, kimlik):
        self.cursor.execute(
            "INSERT INTO musteriler(ad, tip, kimlik_no, bakiye) VALUES(?,?,?,?)",
            (ad, tip, kimlik, 0)
        )
        self.conn.commit()

    # Para işlemi
    def para_islem(self, m_id, miktar):
        self.cursor.execute(
            "UPDATE musteriler SET bakiye = bakiye + ? WHERE id = ?",
            (miktar, m_id)
        )
        self.conn.commit()

    # Müşteri silme
    def musteri_sil(self, m_id):
        self.cursor.execute(
            "DELETE FROM musteriler WHERE id = ?",
            (m_id,)
        )
        self.conn.commit()

    # Tüm müşterileri getir
    def musterileri_getir(self):
        self.cursor.execute("SELECT * FROM musteriler")
        return self.cursor.fetchall()


# =======================
# GUI
# =======================
class BankaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Banka Yönetim Sistemi")
        self.root.geometry("700x550")
        self.root.configure(bg="#f0f0f0")

        self.sistem = BankaSistemi()

        # =======================
        # GİRİŞ ALANLARI
        # =======================

        tk.Label(root, text="Ad Soyad", bg="#f0f0f0", font=("Arial", 11)).pack()
        self.ad_entry = tk.Entry(root, width=30)
        self.ad_entry.pack(pady=3)

        tk.Label(root, text="TC / Vergi No", bg="#f0f0f0", font=("Arial", 11)).pack()
        self.kimlik_entry = tk.Entry(root, width=30)
        self.kimlik_entry.pack(pady=3)

        tk.Label(root, text="Müşteri ID", bg="#f0f0f0", font=("Arial", 11)).pack()
        self.id_entry = tk.Entry(root, width=30)
        self.id_entry.pack(pady=3)

        tk.Label(root, text="Tutar", bg="#f0f0f0", font=("Arial", 11)).pack()
        self.tutar_entry = tk.Entry(root, width=30)
        self.tutar_entry.pack(pady=3)

        # =======================
        # BUTONLAR
        # =======================

        tk.Button(
            root,
            text="Bireysel Ekle",
            command=self.bireysel_ekle,
            bg="#4CAF50",
            fg="white",
            width=20
        ).pack(pady=5)

        tk.Button(
            root,
            text="Tüzel Ekle",
            command=self.tuzel_ekle,
            bg="#2196F3",
            fg="white",
            width=20
        ).pack(pady=5)

        tk.Button(
            root,
            text="Para Yatır / Çek",
            command=self.para_islem,
            bg="#FF9800",
            fg="white",
            width=20
        ).pack(pady=5)

        # MÜŞTERİ SİLME BUTONU
        tk.Button(
            root,
            text="Müşteri Sil",
            command=self.musteri_sil,
            bg="darkred",
            fg="white",
            width=20
        ).pack(pady=5)

        tk.Button(
            root,
            text="Müşterileri Göster",
            command=self.musterileri_goster,
            bg="#9C27B0",
            fg="white",
            width=20
        ).pack(pady=5)

        # ÇIKIŞ BUTONU
        tk.Button(
            root,
            text="Çıkış",
            command=root.quit,
            bg="black",
            fg="white",
            width=20
        ).pack(pady=10)

        # =======================
        # TABLO
        # =======================

        self.tree = ttk.Treeview(
            root,
            columns=("ID", "Ad", "Tip", "Kimlik", "Bakiye"),
            show="headings",
            height=10
        )

        self.tree.heading("ID", text="ID")
        self.tree.heading("Ad", text="Ad Soyad")
        self.tree.heading("Tip", text="Müşteri Tipi")
        self.tree.heading("Kimlik", text="TC / Vergi No")
        self.tree.heading("Bakiye", text="Bakiye")

        self.tree.column("ID", width=50)
        self.tree.column("Ad", width=180)
        self.tree.column("Tip", width=120)
        self.tree.column("Kimlik", width=150)
        self.tree.column("Bakiye", width=100)

        self.tree.pack(fill="both", expand=True, pady=10)

    # =======================
    # FONKSİYONLAR
    # =======================

    # Bireysel müşteri ekle
    def bireysel_ekle(self):
        ad = self.ad_entry.get()
        tc = self.kimlik_entry.get()

        if ad == "" or tc == "":
            messagebox.showerror("Hata", "Boş alan bırakmayın!")
            return

        self.sistem.musteri_ekle(ad, "Bireysel", tc)

        messagebox.showinfo("Başarılı", "Bireysel müşteri eklendi")

        self.temizle()
        self.musterileri_goster()

    # Tüzel müşteri ekle
    def tuzel_ekle(self):
        ad = self.ad_entry.get()
        vergi = self.kimlik_entry.get()

        if ad == "" or vergi == "":
            messagebox.showerror("Hata", "Boş alan bırakmayın!")
            return

        self.sistem.musteri_ekle(ad, "Tüzel", vergi)

        messagebox.showinfo("Başarılı", "Tüzel müşteri eklendi")

        self.temizle()
        self.musterileri_goster()

    # Para yatırma / çekme
    def para_islem(self):
        try:
            m_id = int(self.id_entry.get())
            tutar = float(self.tutar_entry.get())

            self.sistem.para_islem(m_id, tutar)

            messagebox.showinfo("Başarılı", "İşlem tamamlandı")

            self.temizle()
            self.musterileri_goster()

        except:
            messagebox.showerror("Hata", "Geçerli değer gir!")

    # Müşteri silme
    def musteri_sil(self):
        try:
            m_id = int(self.id_entry.get())

            cevap = messagebox.askyesno(
                "Onay",
                f"{m_id} ID numaralı müşteri silinsin mi?"
            )

            if cevap:
                self.sistem.musteri_sil(m_id)

                messagebox.showinfo("Başarılı", "Müşteri silindi")

                self.temizle()
                self.musterileri_goster()

        except:
            messagebox.showerror("Hata", "Geçerli ID gir!")

    # Müşterileri tabloya yaz
    def musterileri_goster(self):

        # Tablo temizleme
        for i in self.tree.get_children():
            self.tree.delete(i)

        veriler = self.sistem.musterileri_getir()

        for veri in veriler:
            self.tree.insert("", "end", values=veri)

    # Entry temizleme
    def temizle(self):
        self.ad_entry.delete(0, tk.END)
        self.kimlik_entry.delete(0, tk.END)
        self.id_entry.delete(0, tk.END)
        self.tutar_entry.delete(0, tk.END)


# =======================
# MAIN
# =======================
if __name__ == "__main__":
    root = tk.Tk()
    app = BankaGUI(root)
    root.mainloop()
