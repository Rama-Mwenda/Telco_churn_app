import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

st.set_page_config(page_title="Dashboard Page", page_icon="📊", layout="wide")

st.title("Dashboard visualizations")
df = pd.read_csv("Datafiles/new_data.csv")
