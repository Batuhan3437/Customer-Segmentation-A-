#Gelişmiş müşteri segmentasyonu projesi 
import numpy as np
import pandas as pd

from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt
from kmodes.kprototypes import KPrototypes
from kmodes.kmodes import KModes

df=pd.read_csv("reading_data/segmentation_data.csv")

#print(df.isnull().sum())
#hiç null data yok

#income ve age data normalization işlemi
df_temp=df[['ID','Age','Income']]
#df_temp

#scale işlemi
scaler=MinMaxScaler()
#age scaling işlemi
scaler.fit(df[['Age']])
df['Age']=scaler.transform(df[['Age']])
#income scale işlemi
scaler.fit(df[['Income']])
df['Income']=scaler.transform(df[['Income']])

#Id silme işlemi 
df=df.drop(['ID'],axis=1)
#değerler normalize edildi küçüldü

mark_array=df.values
#kmodes float istediği için floata çeviriyoruz.
mark_array[:,2]=mark_array[:,2].astype(float)
mark_array[:,4]=mark_array[:,4].astype(float)

#kproto modelini kuruyoruz
#n_clusters kaç tane clustera ayıracağını gösteriyor
#verbose logn işlemleri için
kproto=KPrototypes(n_clusters=10,verbose=2,max_iter=20)
clusters=kproto.fit_predict(mark_array,categorical=[0,1,3,5,6])

#print(kproto.cluster_centroids_)
#len(kproto.cluster_centroids_)

cluster_dict=[]
for c in clusters:
    cluster_dict.append(c)
    
df['cluster']=cluster_dict

#orjinal sutunları koyuyoruz.
df[['ID','Age','Income']]=df_temp

#cluster=0 olanların baştan on tanesini ekrana bastır
df[df['cluster']==0].head(10)

#cluster atama işlemi
df1=df[df.cluster==0]
df2=df[df.cluster==1]
df3=df[df.cluster==2]
df4=df[df.cluster==3]
df5=df[df.cluster==4]
df6=df[df.cluster==5]
df7=df[df.cluster==6]
df8=df[df.cluster==7]
df9=df[df.cluster==8]
df10=df[df.cluster==9]

#tablo figsize boyut belirliyor 15*15 x tarafı ismi age=yas,y tarafı ismi income maas
plt.figure(figsize=(15,15))
plt.xlabel('Age')
plt.ylabel('Income')

#tablolama işlemi rengi ve alphası
plt.scatter(df1.Age,df1['Income'],color='green',alpha=0.4)
plt.scatter(df2.Age,df2['Income'],color='red',alpha=0.4)
plt.scatter(df3.Age,df3['Income'],color='gray',alpha=0.4)
plt.scatter(df4.Age,df4['Income'],color='orange',alpha=0.4)
plt.scatter(df5.Age,df5['Income'],color='yellow',alpha=0.4)
plt.scatter(df6.Age,df6['Income'],color='cyan',alpha=0.4)
plt.scatter(df7.Age,df7['Income'],color='magenta',alpha=0.4)
plt.scatter(df8.Age,df8['Income'],color='gray',alpha=0.4)
plt.scatter(df9.Age,df9['Income'],color='purple',alpha=0.4 )
plt.scatter(df10.Age,df10['Income'],color='blue',alpha=0.4)

#tablonun ekrana bastırılması
plt.legend()
plt.show()


