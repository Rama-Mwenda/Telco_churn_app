import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import plotly.express as px
import plotly.figure_factory as ff
from Utils.authenticator import app

st.set_page_config(
    page_title="Dashboard Page", 
    page_icon="📊", 
    layout="wide"
    )


# col1, col2= st.columns(2)
# with col1:
#     app()
    
# with col2:
#     pass
    
def load_data():
    df= pd.read_csv("Datafiles/new_data.csv")
    return df

df = load_data()

def eda_dashboard():
    st.markdown("#### EXPLORATORY DASHBOARD")
    
    chart1, chart2 = st.columns(spec=[5,3])
    with chart1:
    ## plot a histogram
        fig= px.histogram(df, x=['tenure', 'monthlycharges'], title="Univariate analysis")
        st.plotly_chart(fig)
        
    with chart2:
        ## plot a barchart
        bar = px.bar(df, x="churn")
        st.plotly_chart(bar)
    
    


def kpi_dashboard():
    st.markdown("### KEY PERFORMANCE INDICATORS")
    
    st.markdown("KEY METRICS")
    Kpi1, Kpi2 = st.columns(2)
    Kpi1.metric("Average_tenure", value= 32, delta=-24)
    Kpi2.metric("Average_monthly_charges", value= 65.09, delta= +18.0)
    
    ## plot gender bar chart
    chart=px.bar(df, x="gender", y="monthlycharges", color="churn")
    st.plotly_chart(chart)






if __name__ == "__main__":
    st.title("Dashboard")
    col1, col2= st.columns(2)
    with col1:
        pass
    with col2:
        st.selectbox("Choose your visualizations",options= ["EDA", "KPIs"], key="slected_dashboard_type")
        
    if st.session_state["slected_dashboard_type"] == "EDA":
        eda_dashboard()
    else:
        kpi_dashboard()
        