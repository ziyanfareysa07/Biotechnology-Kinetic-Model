# Biotechnology-Kinetic-Model
**DESKRIPSI PROYEK**
Proyek ini dibuat untuk mensimulasikan dinamika suatu jalur metabolik menggunakan pendekatan Ordinary Differential Equations (ODE). Simulasi dilakukan dengan Python untuk mempelajari perubahan konsentrasi metabolit dan produk terhadap waktu.

Jalur metabolik yang dimodelkan :
X--> A --> B --> P
A : Byproduct
Pada model ini, metabolit A dibentuk dari substrat X, kemudian diubah menjadi metabolit B. Selanjutnya, metabolit B dikonversi menjadi produk akhir P. Selain itu, sebagian metabolit A dapat dialihkan menjadi produk samping B (_Byproduct_)

**TUJUAN**
- Memahami konsep pemodelan kinetika dalam sintesis biologis
- Menyusun persamaan diferensial berdasarkan jaringan metabolik
- Melakukan simulasi numerik menggunakan Python
- Memvisualisasikan perubahan konsentrasi metabolit terhadap waktu

**MODEL REAKSI**
**Reaksi Metabolik**
v1 : x--> A
v2 : A--> B
v3 : B--> P
v4 --> By product

**Persamaan Diferensial**
Laju perubahan konsentrasi setiap komponen dinyatakan sebagai:

d[A]/dt = v₁ − v₂ − v₄
d[B]/dt = v₂ − v₃
d[P]/dt = v₃
dengan:
v₁ = (V1max × X) / ((Km1 + X)(1 + P/Ki))
v₂ = k₂[A]
v₃ = k₃[B]
v₄ = k₄[A]

**Metode Simulasi**
Simulasi dilakukan menggunakan:
1. Python
2. NumPy
3. SciPy
4. Matplotlib
Persamaan diferensial diselesaikan secara numerik menggunakan fungsi solve_ivp() dari pustaka SciPy.

**Hasil Simulasi**
Hasil simulasi menunjukkan perubahan konsentrasi metabolit A, metabolit B, dan produk P terhadap waktu.
File visualisasi hasil simulasi dapat dilihat pada:
simulation_result.png

**Struktur Repository**
Biotechnology-Kinetic-Model
│
├── README.md
├── simulation.py
└── simulation_result.png
**Keterangan File :**
1. README.md → Dokumentasi proyek.
2. simulation.py → Kode program untuk simulasi model kinetika.
3. simulation_result.png → Grafik hasil simulasi.

**Cara Menjalankan Program**
1. Install Python 3.
2. Install library yang diperlukan:
pip install numpy scipy matplotlib
3. Jalankan program:
python simulation.py
4. Grafik hasil simulasi akan ditampilkan dan disimpan sebagai:
simulation_result.png

**Kesimpulan**
Model kinetika ini menunjukkan bagaimana konsentrasi metabolit berubah sepanjang waktu dalam suatu jalur metabolik. Pendekatan ODE memungkinkan analisis perilaku sistem biologis secara kuantitatif dan membantu memahami dinamika pembentukan produk dalam proses bioteknologi.

**Author**
Ziyan Fareysa Abharani
Program Studi Biologi
Universitas Gadjah Mada
