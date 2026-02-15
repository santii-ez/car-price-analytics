# 🚗 Used Car Price Analytics Dashboard

## 📊 Overview
This project is an interactive data analytics dashboard that explores the used car market for Audi, BMW, and Toyota. It helps users understand how variables like **mileage, engine size, and age** impact the final price of a vehicle.

**🔴 Live Demo:** [Click here to launch the App](https://car-price-analytics.streamlit.app/)

## 🎯 Key Insights
* **Brand Segmentation:** Identified clear price tiering where Audi dominates the high-end luxury segment, while Toyota maintains value in the economy sector.
* **Depreciation Logic:** Confirmed a non-linear relationship between mileage and price (-0.48 correlation).
* **Engine Impact:** Engine size is the strongest positive predictor of price (0.61 correlation).

## 🛠️ Tech Stack
* **Python:** Core language.
* **Pandas:** Data manipulation and cleaning.
* **Seaborn/Matplotlib:** Statistical visualizations.
* **Streamlit:** Interactive frontend web application.

## 📂 Project Structure
* `data/`: Contains raw and processed datasets.
* `notebooks/`: Jupyter notebooks for EDA and step-by-step analysis.
* `app/`: Source code for the Streamlit dashboard.

## 🚀 How to run locally
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `streamlit run app/app.py`

---
*Created by Santiago Garcia - Data Science Student*

