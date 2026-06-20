import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

st.set_page_config(page_title="RetailPulse", layout="wide")
st.title("RetailPulse - AI-Powered Customer Analytics")
st.markdown("**Zidio Development Internship — March 2026**")

data = {
    'Transaction ID': range(1, 1001),
    'Date': pd.date_range('2023-01-01', periods=1000, freq='D').strftime('%Y-%m-%d'),
    'Customer ID': ['CUST' + str(i).zfill(3) for i in range(1, 1001)],
    'Gender': ['Male', 'Female'] * 500,
    'Age': [25, 30, 35, 40, 45, 50] * 166 + [25, 30, 35, 40],
    'Product Category': ['Beauty', 'Clothing', 'Electronics'] * 333 + ['Beauty'],
    'Quantity': [1, 2, 3, 4] * 250,
    'Price per Unit': [30, 50, 300, 500] * 250,
    'Total Amount': [30, 100, 900, 2000] * 250
}
df = pd.DataFrame(data)

st.sidebar.header("Filters")
gender = st.sidebar.multiselect("Gender", df['Gender'].unique(), default=df['Gender'].unique())
category = st.sidebar.multiselect("Category", df['Product Category'].unique(), default=df['Product Category'].unique())
df = df[df['Gender'].isin(gender) & df['Product Category'].isin(category)]

col1, col2, col3 = st.columns(3)
col1.metric("Total Records", len(df))
col2.metric("Total Revenue", f"${df['Total Amount'].sum():,}")
col3.metric("Total Customers", df['Customer ID'].nunique())

st.subheader("Total Sales by Category")
fig1, ax1 = plt.subplots(figsize=(8, 4))
df.groupby('Product Category')['Total Amount'].sum().plot(kind='bar', ax=ax1, color=['#FF6B6B','#4ECDC4','#45B7D1'])
ax1.set_xlabel("Category")
ax1.set_ylabel("Total Amount")
plt.tight_layout()
st.pyplot(fig1)

st.subheader("Sales by Gender")
fig2, ax2 = plt.subplots(figsize=(6, 4))
df.groupby('Gender')['Total Amount'].sum().plot(kind='pie', ax=ax2, autopct='%1.1f%%', colors=['#74B9FF','#FD79A8'])
plt.tight_layout()
st.pyplot(fig2)

st.subheader("Monthly Sales Trend")
df['Date'] = pd.to_datetime(df['Date'])
monthly = df.groupby(df['Date'].dt.to_period('M'))['Total Amount'].sum()
fig3, ax3 = plt.subplots(figsize=(10, 4))
monthly.plot(marker='o', color='green', ax=ax3)
plt.tight_layout()
st.pyplot(fig3)

st.subheader("Customer Segmentation")
rfm = df.groupby('Customer ID').agg(Frequency=('Transaction ID','count'), Monetary=('Total Amount','sum')).reset_index()
scaler = StandardScaler()
X_scaled = scaler.fit_transform(rfm[['Frequency','Monetary']])
rfm['Segment'] = KMeans(n_clusters=3, random_state=42, n_init=10).fit_predict(X_scaled)
rfm['Segment'] = rfm['Segment'].map({0:'Bronze',1:'Silver',2:'Gold'})
st.dataframe(rfm[['Customer ID','Frequency','Monetary','Segment']].head(20))
st.write(rfm['Segment'].value_counts())

st.subheader("Churn Prediction Model")
rfm['Churn'] = (rfm['Frequency'] < 2).astype(int)
X = rfm[['Frequency','Monetary']]
y = rfm['Churn']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)
acc = accuracy_score(y_test, model.predict(X_test))
st.success(f"Churn Model Accuracy: {acc*100:.1f}%")

st.subheader("Raw Data")
st.dataframe(df.head(50))