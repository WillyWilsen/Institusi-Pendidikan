# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Institut adalah institusi pendidikan yang telah berdiri sejak tahun 2000 dan memiliki reputasi lulusan yang baik. Namun, belakangan ini mereka menghadapi masalah serius yaitu tingginya angka dropout siswa. Masalah ini tidak hanya berdampak pada reputasi institusi, tetapi juga pada efektivitas sistem pendidikan yang diterapkan.

Untuk mengatasi hal ini, institusi ingin memanfaatkan data performa siswa guna mendeteksi secara dini siapa saja yang berisiko dropout. Selain itu, mereka juga membutuhkan dashboard interaktif yang memudahkan pemantauan dan pengambilan keputusan berbasis data.

### Permasalahan Bisnis

1. Tingginya angka dropout siswa yang memengaruhi reputasi institusi.
2. Belum adanya sistem deteksi dini untuk mengidentifikasi siswa berisiko.
3. Kurangnya pemanfaatan data siswa dalam pengambilan keputusan.
4. Tidak adanya dashboard untuk memantau performa siswa secara real-time.

### Cakupan Proyek

- Tujuan Proyek

  Membantu Jaya Jaya Institut dalam mengidentifikasi faktor-faktor yang berkontribusi terhadap dropout siswa serta memprediksi kemungkinan siswa dropout melalui pendekatan berbasis data dan model machine learning. Proyek ini juga mencakup pembuatan dashboard interaktif untuk memantau performa siswa secara real-time.

- Aktivitas yang Dilakukan

  - Pengumpulan dan pemahaman data: Mengunduh dan memahami struktur dataset dari sumber [Jaya Jaya Institut](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance).
  - Pembersihan & Eksplorasi Data (EDA): Menangani data hilang, mengeksplorasi hubungan antar variabel, dan mengubah tipe data numerik yang bersifat kategorikal menjadi tipe objek agar sesuai dengan teknik pemrosesan.
  - Pembangunan Model Machine Learning:

    - Melakukan encoding pada variabel kategorikal dan scaling pada variabel numerik untuk mempersiapkan data ke model.
    - Menerapkan teknik reduksi dimensi PCA untuk merangkum fitur-fitur yang berkorelasi tinggi menjadi fitur utama.
    - Melatih model klasifikasi Logistic Regression menggunakan data training.
    - Mengevaluasi performa model menggunakan confusion matrix.

  - Pembuatan business dashboard: Menyajikan hasil EDA dan prediksi model dalam bentuk visualisasi yang mudah dipahami oleh pihak manajemen institusi.

- Batasan Proyek

  - Dataset yang digunakan terbatas pada data historis yang disediakan.
  - Model machine learning hanya dibangun sebagai prototype prediksi, belum diintegrasikan ke sistem operasional institusi.
  - Analisis hanya dilakukan berdasarkan variabel-variabel yang tersedia dalam dataset.

- Output

  - Dashboard interaktif untuk monitoring performa siswa dan status dropout (dari hasil EDA dan model).
  - Laporan Analisis & Prediksi yang memuat:
    - Insight dari data eksploratif.
    - Penjelasan model machine learning dan hasil evaluasinya.
    - Rekomendasi action untuk pencegahan dropout siswa.

### Persiapan

Sumber data: [Jaya Jaya Institut](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance)

Setup environment:

1. Persiapan Virtual Environment

   Linux:

   ```
   python -m venv venv
   source venv/bin/activate
   ```

   Windows:

   ```
   python -m venv venv
   venv\Scripts\activate
   ```

2. Instalasi Dependensi

   ```
   pip install -r requirements.txt
   ```

3. Menjalankan Metabase untuk Dashboard

   ```
   docker run -p 3000:3000 --name metabase metabase/metabase
   ```

## Business Dashboard

Dashboard ini dirancang untuk membantu pihak manajemen dan staf akademik Jaya Jaya Institut dalam memahami performa siswa secara keseluruhan, mengidentifikasi pola-pola yang berkaitan dengan risiko dropout, dan mengambil tindakan cepat terhadap siswa yang terindikasi berisiko tinggi.

Beberapa visualisasi yang tersedia di dashboard antara lain:

- Rata-rata umur enrollment berdasarkan status
- Rata-rata gdp berdasarkan status
- Rata-rata curricular unit semester 1 berdasarkan status
- Rata-rata curricular unit semester 2 berdasarkan status

Kredensial:

- email: `root@mail.com`
- password: `root123`

## Menjalankan Sistem Machine Learning

Prototype sistem machine learning ini dirancang untuk memprediksi risiko dropout siswa di Jaya Jaya Institut menggunakan model Logistic Regression. Pada tahap awal, seluruh data numerik yang sebenarnya bersifat kategorikal diubah terlebih dahulu menjadi tipe data objek agar dapat diproses dengan tepat. Selanjutnya, dilakukan preprocessing dengan menerapkan scaling pada fitur numerik agar memiliki skala yang seragam, dan encoding pada fitur kategorikal untuk mengubah nilai kategori menjadi format numerik yang dapat diterima oleh model. Karena terdapat 10 kolom yang memiliki korelasi tinggi satu sama lain, dilakukan reduksi dimensi menggunakan Principal Component Analysis (PCA) untuk merangkum informasi tersebut menjadi 3 fitur utama yang paling berpengaruh. Pipeline ini menggabungkan preprocessing, PCA, dan model Logistic Regression dalam satu alur yang terintegrasi. Data kemudian dibagi menjadi data latih dan data uji untuk melatih model dan mengukur performanya secara objektif. Model berhasil mencapai akurasi sebesar 71% pada data uji, yang menunjukkan kemampuan model dalam memprediksi siswa yang berpotensi dropout dengan cukup baik. Setelah model dilatih, sistem dapat digunakan untuk memprediksi status siswa baru dengan memberikan hasil berupa prediksi kelas.

Cara menjalankan:

```
streamlit run institusi_pendidikan_app.py
```

Link:

https://institusi-pendidikan.streamlit.app/

## Conclusion

Berdasarkan hasil eksplorasi, visualisasi, dan pelatihan data, didapatkan kesimpulan sebagai berikut:

- Sistem machine learning berhasil dikembangkan untuk memprediksi risiko dropout siswa di Jaya Jaya Institut.
- Model Logistic Regression dengan PCA menghasilkan akurasi sebesar 71%, menunjukkan performa yang cukup baik.
- Teknik preprocessing meliputi pengubahan tipe data kategorikal, scaling numerik, dan encoding berhasil meningkatkan kualitas data input model.
- Reduksi dimensi dengan PCA efektif merangkum 10 fitur berkorelasi menjadi 3 fitur utama yang paling berpengaruh.
- Dashboard interaktif memudahkan institusi memonitor performa siswa dan risiko dropout secara real-time.
- Sistem memungkinkan pihak institusi memberikan intervensi lebih cepat dan tepat sasaran untuk siswa berisiko dropout.
- Proyek ini berkontribusi pada pengurangan angka dropout dan peningkatan kualitas lulusan Jaya Jaya Institut.

### Rekomendasi Action Items

Berikut beberapa rekomendasi action items yang dapat dilakukan Jaya Jaya Institut untuk mengatasi masalah dropout dan mencapai target mereka:

- Mengimplementasikan sistem monitoring berbasis dashboard secara rutin untuk memantau risiko dropout siswa sehingga pihak akademik dapat melakukan intervensi lebih awal.
- Memberikan bimbingan dan dukungan khusus kepada siswa yang teridentifikasi berisiko dropout berdasarkan hasil prediksi model machine learning.
- Melakukan evaluasi dan perbaikan kurikulum atau metode pembelajaran untuk meningkatkan keterlibatan dan motivasi siswa, terutama di kelompok yang rentan dropout.
- Mengadakan pelatihan bagi staf dan dosen untuk mengenali tanda-tanda siswa yang berisiko dan cara memberikan dukungan yang efektif.
- Memperluas pengumpulan data dan feedback dari siswa untuk mengidentifikasi faktor-faktor baru yang mungkin mempengaruhi dropout dan terus memperbaiki model prediksi.
- Mengintegrasikan sistem prediksi ke dalam platform akademik agar proses identifikasi risiko dapat berjalan otomatis dan real-time.

