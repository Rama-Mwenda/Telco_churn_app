import streamlit as st

st.set_page_config(page_title="Home Page", page_icon="🏡", layout="wide")

st.title("CHURN CIPHER")
st.header("Customer churn rate prediction and prevention")
st.text("Churn butter not customers")

uploaded_file = st.file_uploader("assets\Customer-churn-prediction-with-evoML.png")
if uploaded_file is not None:
    st.image(uploaded_file)

