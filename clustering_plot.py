import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

df=pd.read_csv('real_estate_consumer_clustering.csv')
features=['Latitude','Longitude','Property_Price','Property_Size_sqft','Consumer_Income','Purchase_Score','Distance_to_City_km']
X=StandardScaler().fit_transform(df[features])
clusters=KMeans(n_clusters=4,random_state=42,n_init=10).fit_predict(X)
p=PCA(n_components=2).fit_transform(X)
plt.scatter(p[:,0],p[:,1],c=clusters,cmap='viridis')
plt.show()
