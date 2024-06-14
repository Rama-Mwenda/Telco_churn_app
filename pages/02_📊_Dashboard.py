import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import plotly.express as px
import plotly.figure_factory as ff
from Utils.authenticator import app

st.set_page_config(page_title="Dashboard Page", 
                   page_icon="📊", 
                   layout="wide"
                   )


col1, col2= st.columns(2)
with col1:
    app()
    
with col2:
    pass
    
def load_data():
    df= pd.read_csv("Datafiles/new_data.csv")
    return df

df = load_data()

col1, col2 = st.columns(2)
with col1:
    pass
with col2:
    st.selectbox("Choose your visualizations", ["EDA", "KPIs"])

##KPIs
st.markdown("KEY METRICS")
Kpi1, Kpi2 = st.columns(2)
Kpi1.metric("Average_tenure", value= 32, delta=-24)
Kpi2.metric("Average_monthly_charges", value= 65.09, delta= +18.0)


chart1, chart2 = st.columns(spec=[5,3])
with chart1:
    ## plot a histogram
    fig= px.histogram(df, x=['tenure', 'monthlycharges'])
    st.plotly_chart(fig)

    ## plot a barchart
    bar = px.bar(df, x="churn")
    st.plotly_chart(bar)

    ## plot gender bar chart
    chart=px.bar(df, x="gender", y="monthlycharges", color="churn")
    st.plotly_chart(chart)
    # ## plot a pie chart
    # sizes= df["churn"]
    # labels= df["gender"]
    
    # fig1, ax1 = plt.subplots()
    # ax1.pie(sizes,labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    # ax1.axis('equal')
    # pie = px.pie(df, values="churn", names="gender")
    # st.pyplot(pie) 
