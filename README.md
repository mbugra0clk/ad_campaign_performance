# 📌 Viral İçerik Tahmini (Classification) Projesi

## 📖 Proje Açıklaması
Bu proje, sosyal medya reklam kampanyalarının performansını analiz ederek **hangi içeriklerin viral olabileceğini** tahmin etmeyi amaçlamaktadır. Engagement Rate hesaplanarak, viral içeriklerin belirlenmesi sağlanmıştır.

## 📂 Kullanılan Veri Seti
- **Dosya Adı:** ad_campaign_performance.csv
- **Özellikler:**
  - **Clicks** → Reklam tıklamaları
  - **Conversions** → Dönüşümler (satın alma, kayıt vb.)
  - **Budget** → Reklam bütçesi (USD)
  - **Engagement Rate (Etkileşim Oranı)** → `(Clicks + Conversions) / Budget`
  - **Viral (Hedef Değişken)** → Engagement Rate ≥ 75. yüzdelik dilimde ise 1, aksi halde 0 olarak belirlendi

## 🔍 Yapılan Analizler
### 1️⃣ Engagement Rate Hesaplama
- Engagement Rate, `(Clicks + Conversions) / Budget` formülüyle hesaplandı.
- Viral içerikler belirlenirken **75. yüzdelik dilim** eşik olarak kullanıldı.
- Viral içerikler **1**, normal içerikler **0** olarak etiketlendi.

### 2️⃣ Veri Kaydetme ve Çıktı Kontrolü
- Viral içeriklerin dağılımı analiz edildi.
- Güncellenmiş veri seti `updated_ad_campaigns.csv` olarak kaydedildi.

## 📊 Elde Edilen Sonuçlar
- Viral içerikler belirlenerek kampanya başarısı ölçüldü.
- Engagement Rate yüksek olan içeriklerin belirli özellikleri incelendi.
- Viral içerik oranı ve dağılımı analiz edildi.
- Sonuç olarak %75 lik viral video oluşurulmuş.
![Figure_2](https://github.com/user-attachments/assets/1353a945-5801-4504-bf11-6ee9749d8563)


## 🚀 Nasıl Kullanılır?
1. **Veri Setini Yükleyin:** `ad_campaign_performance.csv` dosyasını proje klasörüne ekleyin.
2. **Python betiklerini çalıştırın:**
   ```python
   import pandas as pd
   
   # CSV dosyanızı yükleyin
   df = pd.read_csv("ad_campaign_performance.csv")
   
   # Engagement Rate hesaplama
   df["Engagement_Rate"] = (df["Clicks"] + df["Conversions"]) / df["Budget"]
   
   # Viral içerik eşiğini belirleme (75. yüzdelik dilim)
   viral_threshold = df["Engagement_Rate"].quantile(0.75)
   
   # Viral içerikleri etiketleme
   df["Viral"] = (df["Engagement_Rate"] >= viral_threshold).astype(int)
   
   # Viral içerik sayısını kontrol etme
   print(df["Viral"].value_counts())
   
   # Güncellenmiş veri setini kaydetme
   df.to_csv("updated_ad_campaigns.csv", index=False)
   ```

## 📌 Kullanılan Teknolojiler
- Python (Pandas, NumPy)
- Veri İşleme ve Analiz

## 📌 Katkıda Bulunma
Projeye katkıda bulunmak istiyorsanız, lütfen **pull request** oluşturun veya bir **issue** açın. Her türlü geri bildirim değerlidir! 😊

## 📧 İletişim
Herhangi bir sorunuz veya öneriniz varsa, benimle GitHub üzerinden iletişime geçebilirsiniz.

---
💡 **Not:** Bu proje, sosyal medya kampanyalarını analiz etmek ve viral içerikleri belirlemek için oluşturulmuştur.

