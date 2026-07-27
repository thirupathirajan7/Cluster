# Large-Scale Geographic Consumer Clustering & High-Dimensional Visualizations

## Project Overview

This project analyzes synthetic real-estate transaction data to identify
regional consumer housing market segments. Geographic coordinates and
property attributes are clustered using K-Means after feature scaling.
PCA reduces the high-dimensional data to two dimensions for
visualization, and Folium can be used to display the clustered
properties on an interactive map.

## Objectives

-   Analyze multivariate real-estate data.
-   Group similar consumer/property markets using clustering.
-   Visualize clusters using PCA.
-   Support location-based business and expansion planning.

## Dataset

**File:** `real_estate_consumer_clustering.csv`

### Features

-   Property_ID
-   Latitude
-   Longitude
-   Property_Price
-   Property_Size_sqft
-   Bedrooms
-   Bathrooms
-   Property_Type
-   Transaction_Type
-   Consumer_Income
-   Consumer_Age
-   Purchase_Score
-   Distance_to_City_km
-   Region

## Technologies

-   Python 3.x
-   Pandas
-   NumPy
-   Scikit-learn
-   Matplotlib
-   Folium

## Methodology

1.  Load the dataset.
2.  Select numerical features.
3.  Standardize features using StandardScaler.
4.  Apply K-Means clustering.
5.  Reduce dimensions using PCA.
6.  Visualize clusters.
7.  Export clustered results and map.

## Installation

``` bash
pip install pandas numpy scikit-learn matplotlib folium
```

## Run

``` bash
python consumer_clustering.py
```

## Output Files

-   clustered_output.csv
-   cluster_plot.png
-   consumer_clusters_map.html

## Folder Structure

    Project/
    │── real_estate_consumer_clustering.csv
    │── consumer_clustering.py
    │── clustering_plot.py
    │── cluster_plot.png
    │── consumer_clusters_map.html
    │── clustered_output.csv
    └── README.md

## Future Enhancements

-   DBSCAN and Hierarchical Clustering
-   t-SNE visualization
-   Interactive dashboard using Streamlit
-   Real-world property datasets
-   Automatic optimal cluster selection

## Author
Rajan B
BCA Mini Project Large-Scale Geographic Consumer Clustering &
High-Dimensional Visualizations
