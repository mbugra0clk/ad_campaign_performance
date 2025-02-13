import pandas as pd

# Dosyayı okuyalım
df = pd.read_csv('C:\ML/ad_campaign_performance/ad_campaign_performance.csv')

# İlk birkaç satırı ve genel bilgileri inceleyelim
df.head(), df.info(), df.describe()

import numpy as np
import matplotlib.pyplot as plt

# Engagement Rate hesaplama (Clicks + Conversions) / Budget
df["Engagement_Rate"] = (df["Clicks"] + df["Conversions"]) / df["Budget"]

# Engagement Rate dağılımını görselleştirme
plt.figure(figsize=(8, 5))
plt.hist(df["Engagement_Rate"], bins=30, edgecolor='k', alpha=0.7)
plt.xlabel("Engagement Rate")
plt.ylabel("Frequency")
plt.title("Engagement Rate Distribution")
plt.grid(True)
plt.show()

# Engagement Rate'in istatistiksel özetini görüntüleyelim
df["Engagement_Rate"].describe()


# Viral içerik etiketini oluşturma (Engagement Rate >= 75. yüzdelik dilim: 2.25)
df["Viral"] = (df["Engagement_Rate"] >= 2.25).astype(int)

# Viral ve normal içerik sayısını görüntüleyelim
df["Viral"].value_counts()


import pandas as pd


# Engagement Rate hesaplama
df["Engagement_Rate"] = (df["Clicks"] + df["Conversions"]) / df["Budget"]

# Viral içerik eşiğini belirleme (75. yüzdelik dilim)
viral_threshold = df["Engagement_Rate"].quantile(0.75)

# Viral içerikleri etiketleme
df["Viral"] = (df["Engagement_Rate"] >= viral_threshold).astype(int)

# Viral içerik sayısını kontrol etme
print(df["Viral"].value_counts())

#**anlaşılıyor ki burada 0.75 i yani %75 i viral videodur.**