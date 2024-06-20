import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import plotly.express as px
import plotly.figure_factory as ff

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

def eda_dashboard(df):
    st.markdown("#### EXPLORATORY DASHBOARD")
    
    chart1, chart2,chart3 = st.columns(spec=[5,3,2])
    with chart1:
    ## plot a histogram
        fig= px.histogram(df, x=['tenure', 'monthlycharges'], title="Univariate analysis")
        st.plotly_chart(fig)
        
    with chart2:
        ## plot a barchart
        bar = px.bar(df, x="churn", title="Churn rate")
        st.plotly_chart(bar)
        
    with chart3:
        ### plot histogram
            fig1 = px.histogram(df, x='tenure', title='Histogram of Tenure')
            st.plotly_chart(fig1)

    
    
### KPI DASHBOARD

def kpi_dashboard(df):
    st.markdown("### KEY PERFORMANCE INDICATORS")
    st.markdown("#### KEY METRICS")
    

    # Compute key metrics from the DataFrame
    avg_tenure = df['tenure'].mean()
    avg_monthly_charges = df['monthlycharges'].mean()
    churn_rate = df['churn'].value_counts(normalize=True).get('Yes', 0) * 100
    contract_count = df['contract'].value_counts()
    
    st.markdown("KEY METRICS")
    Kpi1, Kpi2 = st.columns(2)
    Kpi1.metric("Average_tenure", value= 32, delta=-24)
    Kpi2.metric("Average_monthly_charges", value= 65.09, delta= +18.0)
    
    ## plot gender bar chart
    chart=px.bar(df, x="gender", y="monthlycharges", color="churn")
    st.plotly_chart(chart)

# Create a pie chart for Contract distribution
    chart2 = px.pie(df, names='contract', title="Distribution of Customers by Contract Type")
    st.plotly_chart(chart2)





if __name__ == "__main__":
    st.title("Dashboard")
    col1, col2= st.columns(2)
    with col1:
        pass
    with col2:
        st.selectbox("Choose your visualizations",options= ["EDA", "KPIs"], key="selected_dashboard_type")
        
    if st.session_state["selected_dashboard_type"] == "EDA":
        eda_dashboard(df)
    else:
        kpi_dashboard(df)
        