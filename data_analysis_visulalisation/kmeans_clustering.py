"""
This Python script performs K-Means clustering on patient data to identify optimal locations 
for population clusters based on patient coordinates (Pat_X, Pat_Y) and drive distance (Drive_Distance_Miles).

The script achieves the following:
1. Normalizes the input features (Pat_X, Pat_Y, Drive_Distance_Miles) for clustering.
2. Applies K-Means clustering to group patients into three clusters.
3. Visualizes the clusters and the centroids representing optimal locations for each cluster.
4. Prints the centroids of the clusters, which indicate the optimal patient locations.

"""

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Example dataset based on the file provided
# This data would typically come from the full dataset
data = {
    'Pat_X': np.random.randint(10, 100, 100),
    'Pat_Y': np.random.randint(10, 100, 100),
    'Drive_Distance_Miles': np.random.randint(5, 50, 100)
}

df = pd.DataFrame(data)
features = df[['Pat_X', 'Pat_Y', 'Drive_Distance_Miles']]
scaler = StandardScaler()
normalized_features = scaler.fit_transform(features)
k = 3
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(normalized_features)
df['Cluster'] = kmeans.labels_
centroids = scaler.inverse_transform(kmeans.cluster_centers_)

plt.figure(figsize=(10, 6))
colors = ['blue', 'green', 'orange']
for cluster in range(k):
    cluster_data = df[df['Cluster'] == cluster]
    plt.scatter(cluster_data['Pat_X'], cluster_data['Pat_Y'], label=f'Population Cluster {cluster + 1}', color=colors[cluster])
    plt.scatter(centroids[cluster, 0], centroids[cluster, 1], s=400, color=colors[cluster], edgecolor='black', label=f'Optimal Site {cluster + 1}')

plt.title('K-Means Clustering of Patients')
plt.xlabel('Pat_X (Patient X Coordinate)')
plt.ylabel('Pat_Y (Patient Y Coordinate)')
plt.legend(loc='upper left', bbox_to_anchor=(0, 1.05), borderaxespad=0.)
plt.grid()
plt.savefig("./data_vis_assets/kmeans_clusters.png", dpi=300)
plt.show()

print("Cluster Centroids (Patient Locations):")
for i, centroid in enumerate(centroids):
    print(f"Population Cluster {i + 1}: Pat_X = {centroid[0]:.2f}, Pat_Y = {centroid[1]:.2f}, Drive_Distance_Miles = {centroid[2]:.2f}")
