# House Price Prediction & Analysis 🏠

Bu proje, ünlü **King County** konut veri setini kullanarak ev fiyatlarını tahmin etmek ve veri analizi yapmak amacıyla geliştirilmiştir. Proje kapsamında veri temizleme, aykırı değer (outlier) analizi ve harita üzerinde görselleştirme çalışmaları yapılmıştır.

## 🚀 Proje İçeriği
* **Veri Analizi:** Ev özelliklerinin fiyat üzerindeki etkisinin incelenmesi.
* **Outlier (Aykırı Değer) Analizi:** `outlier_comparison.py` dosyası ile veri temizliği öncesi ve sonrası performans karşılaştırması.
* **Görselleştirme:** `interactive_map.html` dosyası ile evlerin konumlarının interaktif harita üzerinde gösterimi.
* **Makine Öğrenmesi:** Fiyat tahmini için regresyon modellerinin uygulanması.

## 📂 Dosya Açıklamaları
* `main_analysis.py`: Ana modelleme ve analiz kodları.
* `outlier_comparison.py`: Veri setindeki aykırı değerlerin temizlenmesinin modele etkisini gösteren analiz.
* `interactive_map.html`: Folium kütüphanesi ile oluşturulmuş, bölgelere göre fiyat dağılımını gösteren harita çıktısı. (İndirip tarayıcıda açabilirsiniz).
* `kc_house_data.csv`: Analizde kullanılan ham veri seti.

## 🛠️ Kullanılan Kütüphaneler
* **Python**
* **Pandas & NumPy** (Veri İşleme)
* **Matplotlib & Seaborn** (Grafikleştirme)
* **Scikit-learn** (Makine Öğrenmesi Modelleri)
* **Folium** (Harita Görselleştirme)

## 📊 Sonuçlar
Model, veri temizliği yapıldıktan sonra fiyat tahminlerinde daha yüksek doğruluk oranına ulaşmıştır. Harita görselleştirmesi, sahil şeridindeki evlerin fiyatlarının daha yüksek olduğunu doğrulamaktadır.

## 👨‍💻 Geliştirici
**Hasan Köstek**
