import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import datetime

# Membaca dataset CSV
@st.cache_data
def load_data(file_path):
    data = pd.read_csv(file_path)
    data['date'] = pd.to_datetime(data['date'])
    return data

# Load data
data_file = 'data_finance.csv'  # Ganti dengan path dataset Anda
data = load_data(data_file)

# Sidebar untuk filter
st.sidebar.header("Filter Data")
start_date = st.sidebar.date_input("Start Date", value=datetime.date(2023, 1, 1))
end_date = st.sidebar.date_input("End Date", value=datetime.date(2023, 12, 31))
category_filter = st.sidebar.multiselect("Category", options=data['category'].unique(), default=data['category'].unique())

# Filter data berdasarkan input user
filtered_data = data[(data['date'] >= pd.to_datetime(start_date)) & (data['date'] <= pd.to_datetime(end_date)) & (data['category'].isin(category_filter))]

# Dashboard utama
st.title("Financial Dashboard")
st.subheader(f"Data from {start_date} to {end_date}")

# Summary metrics
total_income = filtered_data['income'].sum()
total_expenses = filtered_data['expenses'].sum()
net_balance = total_income - total_expenses

st.metric("Total Income", f"${total_income:,.2f}")
st.metric("Total Expenses", f"${total_expenses:,.2f}")
st.metric("Net Balance", f"${net_balance:,.2f}")

# Plotting
st.subheader("Income and Expenses Over Time")
fig, ax = plt.subplots(figsize=(10, 5))
filtered_data.set_index('date')[['income', 'expenses']].resample('M').sum().plot(kind='bar', ax=ax)
ax.set_title('Monthly Income and Expenses')
ax.set_ylabel('Amount ($)')
st.pyplot(fig)

st.subheader("Breakdown by Category")
fig, ax = plt.subplots(figsize=(10, 5))
filtered_data.groupby('category')[['income', 'expenses']].sum().plot(kind='bar', ax=ax)
ax.set_title('Income and Expenses by Category')
ax.set_ylabel('Amount ($)')
st.pyplot(fig)

# Menampilkan data dalam tabel
st.subheader("Detailed Data")
st.dataframe(filtered_data)

# Save to CSV
if st.button('Save Filtered Data to CSV'):
    filtered_data.to_csv('filtered_financial_data.csv', index=False)
    st.success('Data has been saved to filtered_financial_data.csv')
