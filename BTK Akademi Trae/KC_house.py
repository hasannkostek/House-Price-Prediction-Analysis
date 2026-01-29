#King County House Price Prediction
# 1-Kütüphaneler Yüklenir 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_squared_error
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor

df = pd.read_csv("c:\\Users\\Hasan\\Desktop\\BTK Akademi Trae\\kc_house_data.csv")
pd.set_option('display.max_columns', None)   # tüm sütunları gösterir
print(df.head())

# Veri Seti Hakkında Bilgi
print(df.info())
print(df['price'].max()) # en pahalı evin fiyatı
print(df['price'].min()) # en ucuz evin fiyatı
print(df['price'].mean()) # ortalama fiyat
print(df[df['price']==df['price'].max()]) # en pahalı ev hakkında bilgi
print(df[df['price']==df['price'].min()]) # en ucuz ev hakkında bilgi

# en genç ev 
print(df['yr_built'].max())
print(df[df['yr_built']==df['yr_built'].max()])

# en yaşlı ev
print(df['yr_built'].min())
print(df[df['yr_built']==df['yr_built'].min()])

print(df['bedrooms'].max())  # en fazla yatak odalı ev

# Veri Setindeki Aykırı Değerleri Ayıklamak Outlier
# Outlier Hesaplanacak Sütunları Belirleme
df_outlier_columns = df[['price','bedrooms','bathrooms','sqft_living','sqft_lot']]
outliers = df_outlier_columns.quantile(q=.99)
print(outliers)

df_clean = df[(df['price']<outliers['price'])] 
print("Ev fiyatı yeni max: ",df_clean['price'].max())   # ayıklanan değerler arasında en pahalı ev

df_clean = df_clean[(df_clean['bedrooms']<outliers['bedrooms'])] 
df_clean = df_clean[(df_clean['sqft_living']<outliers['sqft_living'])] 
df_clean = df_clean[(df_clean['sqft_lot']<outliers['sqft_lot'])] 
df_clean.describe()
df_corr = df_clean.corr(numeric_only=True).sort_values('price',ascending=False)['price'].head(10)
print(df_corr)  # ev fiyatı ile diğer özellikler arası colerasyonun büyükten küçüğe sıralanışı

df_clean['age']=2015-df_clean['yr_built']

df_clean['restore'] = np.where(df_clean['yr_renovated']==0,0,1)  # restore edilmiş mi diye kontrol edilir (0 ise restore edilmemiş, 1 ise restore edilmişdir. Ve onu nasıl kontrol eder? (Yıl yazıyorsa veri setinde restore edilmiştir !!!))
df_clean['sqft_total'] = df_clean['sqft_living'] + df_clean['sqft_lot']
df_clean['sqft_basement'] = np.where(df_clean['sqft_basement']==0,0,1)  # bodrum var mı yok muyu kontrol eder


print(df_clean.shape)
x=df_clean.drop(['price','date','id','yr_built','yr_renovated','lat','long','sqft_living','sqft_lot'],axis=1)
y=df_clean['price']
print(x.shape)
print(y.shape)
print(x.info())
print(y.info())
x = pd.get_dummies(x,columns=['zipcode'],drop_first=True) # eksik veri yok sadece zipcode OHE ile kategori sayısal değere çevrildi.
print(x.info())

# ölçeklendirme işlemi yapıldı
scaler=StandardScaler()
x = scaler.fit_transform(x)   # fit_transform = hem uyguluyor hem dönüştürüyor hem de öğreniyor.
print(x)

# veri setini eğitim-test olarak ayırma
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)  # burada sonuçlar elimizde olduğu için ayrı bir val değeri yok !!!

# model oluşturmaca:
print("Model1: ")
model = LinearRegression()
model.fit(x_train,y_train)   # model eğitimi = train 

# tahmin yaparak modeli tets ederiz:
y_pred = model.predict(x_test)
print("R2 Score: ",r2_score(y_test,y_pred))
print("Ortalama Hata: ",mean_squared_error(y_test,y_pred)**.5)

# Başka bir model denemek istersek: (model2)
print("Model2: ")
model = RandomForestRegressor()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)
print("R2 Score: ",r2_score(y_test,y_pred))
print("Ortalama Hata: ",mean_squared_error(y_test,y_pred)**.5)

# Başka bir model denemek istersek: (model3)
print("Model3: ")
model = XGBRegressor()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)
print("R2 Score: ",r2_score(y_test,y_pred))
print("Ortalama Hata: ",mean_squared_error(y_test,y_pred)**.5)
