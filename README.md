# Spatio-Temporal Crime Analysis

This repository contains code and resources for performing a **Spatio-Temporal Crime Analysis**. The project focuses on uncovering geographic and temporal patterns in criminal activity (such as identifying hotspots, peak crime hours, and seasonal trends) to help understand, visualize, and potentially predict where and when crimes are most likely to occur.

---

## 📊 Dataset Information

The analysis is based on the Chicago Crime dataset:

* **Source:** [Kaggle - Crimes 2001 to Present (Chicago)](https://www.kaggle.com/datasets/adelanseur/crimes-2001-to-present-chicago)
* **Dataset Note:** The full Chicago Crime dataset is extremely large. For this project, **only a subsection (subset)** of the dataset was used to ensure efficient processing and faster execution.

---

## ⚙️ Environment and Requirements

This project is built and optimized to run on **Google Colab**.

### Prerequisite Setup:

To access and process the data in Google Colab, you should save your dataset subset on **Google Drive** and mount your drive in the notebook.

### Key Libraries Used:

* `pandas` (Data manipulation)
* `numpy` (Numerical computing)
* `matplotlib` & `seaborn` (Data visualization)
* `folium` / `geopandas` (Spatial mapping and hotspot visualization)

---

## 🚀 How to Run the Project

Follow these steps to run the analysis yourself:

### Step 1: Download the Dataset

1. Go to the [Kaggle Chicago Crimes Dataset](https://www.kaggle.com/datasets/adelanseur/crimes-2001-to-present-chicago).
2. Download the data.
3. Extract or filter a **subsection** of the data (e.g., a specific year range like 2020–present, or a specific neighborhood/crime category) to match the scope of this analysis.

### Step 2: Upload to Google Drive

1. Create a folder in your Google Drive (e.g., `Colab Notebooks/Crime_Analysis/`).
2. Upload your processed dataset subsection (CSV file) into this folder.

### Step 3: Open in Google Colab

1. Upload the Jupyter notebook (`.ipynb` file) from this repository to your Google Colab environment.
2. Ensure you have mounted your Google Drive in Colab by running the following snippet:
```python
from google.colab import drive
drive.mount('/content/drive')

```


3. Update the data path in the notebook to point to the location where you uploaded your dataset on Google Drive:
```python
dataset_path = '/content/drive/MyDrive/Colab Notebooks/Crime_Analysis/your_dataset_subset.csv'

```


4. Run the notebook cells sequentially to execute the data preprocessing, temporal trend analysis, and spatial mapping!

---

## 📌 Project Highlights

* **Temporal Analysis:** Visualizing how crime distribution changes over years, months, days of the week, and hours of the day.
* **Spatial Mapping:** Generating geographic heatmaps of high-density crime regions (hotspots) using latitude and longitude coordinates.
* **Preprocessing Pipeline:** Handling missing geospatial data, cleaning categories, and parsing timestamps for optimized analytical queries.
