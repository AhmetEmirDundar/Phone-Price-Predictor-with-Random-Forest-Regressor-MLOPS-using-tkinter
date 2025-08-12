# 📱 Telefon Fiyat Tahmin Uygulaması

Bu proje, makine öğrenmesi kullanarak telefon fiyatlarını tahmin eden kullanıcı dostu bir masaüstü uygulamasıdır. Tkinter kullanılarak geliştirilmiş olan uygulama, Random Forest algoritması ile %88.9 doğruluk oranında fiyat tahmini yapabilmektedir.

## 🚀 Özellikler

- **Kullanıcı Dostu Arayüz**: Modern ve sezgisel tkinter tabanlı GUI
- **Yüksek Doğruluk**: Random Forest algoritması ile %88.9 R² skoru
- **Gerçek Zamanlı Tahmin**: Anında fiyat tahmini sonuçları
- **Kapsamlı Veri Seti**: 407 farklı telefon modeli ile eğitilmiş
- **Çoklu Özellik Desteği**: Depolama, RAM, ekran boyutu, kamera ve batarya
- **Hata Yönetimi**: Kullanıcı dostu hata mesajları ve validasyon

## 📋 Gereksinimler

### Python Sürümü
- Python 3.7 veya üzeri

### Gerekli Kütüphaneler
```
pandas>=1.3.0
numpy>=1.21.0
scikit-learn>=1.0.0
tkinter (Python ile birlikte gelir)
```

## 🛠️ Kurulum

### 1. Projeyi İndirin
```bash
git clone <repository-url>
cd PhonePricePrediction
```

### 2. Gerekli Kütüphaneleri Yükleyin
```bash
pip install pandas numpy scikit-learn
```

### 3. Uygulamayı Çalıştırın
```bash
python main.py
```

## 📊 Veri Seti

Uygulama, aşağıdaki özelliklere sahip 407 telefon modeli ile eğitilmiştir:

| Özellik | Açıklama | Değer Aralığı |
|---------|----------|----------------|
| **Depolama** | Dahili depolama kapasitesi | 32 GB - 1024 GB |
| **RAM** | Çalışma belleği | 2 GB - 16 GB |
| **Ekran Boyutu** | Ekran çapraz boyutu | 4.7" - 7.6" |
| **Kamera Sayısı** | Arka kamera sayısı | 1 - 5 |
| **Toplam MP** | Tüm kameraların toplam megapikseli | 12 - 200+ |
| **Batarya** | Batarya kapasitesi | 1821 - 6000 mAh |

## 🎯 Kullanım

### 1. Uygulamayı Başlatın
```bash
python main.py
```

### 2. Telefon Özelliklerini Girin
- **Depolama**: Dropdown menüden GB cinsinden seçin
- **RAM**: Dropdown menüden GB cinsinden seçin
- **Ekran Boyutu**: Inch cinsinden sayısal değer girin
- **Kamera Sayısı**: Dropdown menüden kamera sayısını seçin
- **Toplam MP**: Sayısal değer girin
- **Batarya**: mAh cinsinden sayısal değer girin

### 3. Tahmin Yapın
"🚀 FİYAT TAHMİNİ YAP" butonuna tıklayın

### 4. Sonucu Görün
Sağ panelde tahmin edilen fiyat ve girilen özellikler görüntülenir

## 🔧 Teknik Detaylar

### Model Mimarisi
- **Algoritma**: Random Forest Regressor
- **Preprocessing**: StandardScaler ile özellik normalizasyonu
- **Cross-validation**: 5-fold cross-validation
- **Hyperparameter Tuning**: GridSearchCV ile optimize edilmiş

### Model Performansı
```
Training Set:
- R² Score: 0.951
- RMSE: 64.83
- MAE: 42.71

Test Set:
- R² Score: 0.889
- RMSE: 84.48
- MAE: 57.60
```

### Özellik Mühendisliği
- **Camera Count**: Kamera sayısı hesaplaması
- **Total MP**: Toplam megapiksel hesaplaması
- **Veri Temizleme**: Eksik değerler ve anomali tespiti

## 📁 Proje Yapısı

```
PhonePricePrediction/
├── main.py                 # Ana uygulama dosyası
├── phone_data.csv         # Eğitim veri seti
├── phone_price.pkl        # Eğitilmiş model ve preprocessor
├── PhonePricePrediction.ipynb  # Model geliştirme notebook'u
└── README.md              # Bu dosya
```

## 🎨 Arayüz Özellikleri

### Sol Panel
- Form giriş alanları
- Dropdown menüler ve text input'lar
- Büyük ve belirgin tahmin butonu
- Hover efektleri

### Sağ Panel
- Tahmin sonuçları
- Veri seti istatistikleri
- Fiyat aralığı bilgisi
- Model sayısı ve marka bilgisi

## 🚨 Hata Yönetimi

- **Dosya Bulunamadı**: Model veya veri dosyası eksikse uyarı
- **Geçersiz Giriş**: Sayısal olmayan değerler için hata mesajı
- **Eksik Alan**: Boş bırakılan zorunlu alanlar için uyarı
- **Model Hatası**: Tahmin sırasında oluşan hatalar için bilgilendirme

## 🔮 Gelecek Geliştirmeler

- [ ] Daha fazla telefon özelliği ekleme
- [ ] Farklı makine öğrenmesi algoritmaları
- [ ] Model performans karşılaştırması
- [ ] Veri görselleştirme grafikleri
- [ ] Export/Import özellikleri
- [ ] Çoklu dil desteği

## 🤝 Katkıda Bulunma

1. Bu repository'yi fork edin
2. Feature branch oluşturun (`git checkout -b feature/AmazingFeature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some AmazingFeature'`)
4. Branch'inizi push edin (`git push origin feature/AmazingFeature`)
5. Pull Request oluşturun

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakın.

## 📞 İletişim

Proje hakkında sorularınız için:
- GitHub Issues: [Proje Issues Sayfası]
- Email: [your-email@example.com]

## 🙏 Teşekkürler

- Scikit-learn ekibine makine öğrenmesi kütüphanesi için
- Tkinter geliştiricilerine GUI framework için
- Veri setini paylaşan topluluk üyelerine

---

**Not**: Bu uygulama eğitim amaçlı geliştirilmiştir. Gerçek fiyat tahminleri için ek doğrulama ve test önerilir.

