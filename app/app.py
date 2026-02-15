import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --- 1. CONFIGURATION & TITLE ---
# Wide layout creates a dashboard feel
st.set_page_config(page_title="Car Price Analytics", layout="wide")

st.title("🚗 Used Car Price Analytics")
st.markdown("""
This dashboard helps you analyze the relationship between **mileage, engine size, and price** for top car brands (Audi, BMW, Toyota).
""")

# --- 2. LOAD DATA ---
@st.cache_data
def load_data():
    return pd.read_csv("data/processed/cleaned_cars.csv")

try:
    df = load_data()
except FileNotFoundError:
    st.error("Error: CSV file not found. Check the file path in 'load_data'.")
    st.stop()

# --- 3. SIDEBAR (FILTERS) ---
st.sidebar.header("Filter Options")

# Filter by Brand
all_brands = df['brand'].unique()
selected_brand = st.sidebar.selectbox("Select a Brand", all_brands)

# Filter by Transmission (Optional extra filter)
# We add 'All' to allow seeing everything
transmissions = ['All'] + list(df['transmission'].unique())
selected_transmission = st.sidebar.selectbox("Transmission Type", transmissions)

# --- 4. DATA FILTERING ---
# We start with the full dataframe and apply filters step by step
filtered_df = df[df['brand'] == selected_brand]

if selected_transmission != 'All':
    filtered_df = filtered_df[filtered_df['transmission'] == selected_transmission]

# --- 5. KEY METRICS (COLUMNS) ---
# st.columns lets us place elements side-by-side
col1, col2, col3 = st.columns(3)

avg_price = filtered_df['price'].mean()
total_cars = filtered_df.shape[0]
avg_mileage = filtered_df['mileage'].mean()

with col1:
    st.metric(label="Average Price", value=f"${avg_price:,.0f}")

with col2:
    st.metric(label="Total Cars Available", value=f"{total_cars}")

with col3:
    st.metric(label="Average Mileage", value=f"{avg_mileage:,.0f} miles")

st.divider() # Adds a visual line separator

# --- 6. VISUALIZATIONS ---

# Create two columns for charts
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.subheader(f"Price Distribution for {selected_brand}")
    fig1, ax1 = plt.subplots(figsize=(8, 5))
    sns.histplot(filtered_df['price'], kde=True, ax=ax1, color="skyblue")
    ax1.set_xlabel("Price ($)") 
    plt.tight_layout() 
    st.pyplot(fig1, use_container_width=True)

with chart_col2:
    st.subheader("Price vs. Mileage")
    # This scatter plot proves your business insight
    fig2, ax2 = plt.subplots(figsize=(8, 5))
    sns.scatterplot(data=filtered_df, x='mileage', y='price', alpha=0.6, ax=ax2, color="salmon")
    ax2.set_xlabel("Mileage")
    ax2.set_ylabel("Price ($)")
    plt.tight_layout()
    st.pyplot(fig2, use_container_width=True)

# --- 7. RAW DATA TABLE ---
st.divider()
if st.checkbox("Show Raw Data for this selection"):
    st.dataframe(filtered_df)