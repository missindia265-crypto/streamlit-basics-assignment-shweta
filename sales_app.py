import streamlit as st
import pandas as pd

st.title("Sales Summary Dashboard")
st.subheader("Interactive sales summary by product category")

data = {
    "Product": ["Laptop", "Phone", "Headphones", "Keyboard", "Monitor", "Mouse"],
    "Category": ["Electronics", "Electronics", "Accessories",
                 "Accessories", "Electronics", "Accessories"],
    "Sales": [50000, 35000, 5000, 3000, 20000, 2000]
}

df = pd.DataFrame(data)


categories = df["Category"].unique()


st.sidebar.header("Filter Options")

selected_category = st.sidebar.selectbox(
    "Select Category",
    categories
)


filtered_df = df[df["Category"] == selected_category]

st.dataframe(filtered_df)

st.line_chart(filtered_df.set_index("Product")["Sales"])