import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("CFL FY26 Q2 Forecasts")

# Load data
df = pd.read_csv("final_submission2.csv")

# Search / filter
query = st.text_input("Search product name (substring)")
if query:
    df_show = df[df["Product Name"].str.contains(query, case=False, na=False)]
else:
    df_show = df.copy()

st.subheader("Predictions (preview)")
st.dataframe(df_show)

# Top N plot
n = st.slider("Top N products to show", 5, 30, 10)
topn = df.sort_values("Predicted FY26 Q2", ascending=False).head(n)
fig, ax = plt.subplots(figsize=(8, max(3, n*0.3)))
ax.barh(topn["Product Name"], topn["Predicted FY26 Q2"])
ax.invert_yaxis()
ax.set_xlabel("Predicted FY26 Q2")
st.pyplot(fig)

# Single-product detail
prod = st.selectbox("Select product", df["Product Name"].dropna().unique())
if prod:
    val = df.loc[df["Product Name"] == prod, "Predicted FY26 Q2"].values
    st.metric("Predicted FY26 Q2", int(val[0]) if len(val) else "N/A")

# Download
st.download_button(
    "Download current CSV",
    data=df_show.to_csv(index=False).encode("utf-8"),
    file_name="predictions_filtered.csv",
    mime="text/csv",
)