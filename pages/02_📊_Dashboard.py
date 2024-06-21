import streamlit as st
import pandas as pd
import numpy as np
import altair
import seaborn as sns 
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
    
    ## plot a histogram
    fig= px.histogram(df, x=['tenure', 'monthlycharges'], 
                          color_discrete_map={'tenure':'lightsalmon', 'monthlycharges':'lightblue'}, 
                          title="Univariate analysis")
    st.plotly_chart(fig)
    
    chart1, chart2 = st.columns(spec=[3,3])
    with chart1:
        
        ## plot a churn chart
        pie = px.pie(df, names='churn', title="Churn rate", color_discrete_sequence=['lightsalmon', 'lightskyblue'])
        st.plotly_chart(pie)
        
        ## plot a internet service chart
        bar = px.pie(df, names= "internetservice", title="Internet service providers")
        st.plotly_chart(bar)
        
        ## plot a contract chart
        pie = px.pie(df, names='contract', title="Contract rate")
        st.plotly_chart(pie)
    
        
    with chart2:
        ## Plot by contract and monthly charges
        violin = px.violin(df, x="monthlycharges", y="contract", color_discrete_sequence=['lightsalmon', 'lightskyblue', "blue"], 
                           title="Distribution of monthly charges by contract")
        st.plotly_chart(violin)
        
        ## Plot by tenure and gender
        violin = px.violin(df, x="tenure", y="gender", color_discrete_sequence=["lightsalmon", "lightskyblue"],
                           title="Lifespan of customer by gender")
        st.plotly_chart(violin)
        
        ## Plot payment method by monthly charges
        violin = px.violin(df, x="monthlycharges", y="paymentmethod", color_discrete_sequence=["lightsalmon", "lightskyblue"], 
                           title="Distribution of monthlycharges by payment")
        st.plotly_chart(violin)
        
         
    # with chart3:
    #     pair = px.scatter(df, x='partner', y= 'monthlycharges', color='churn')
    #     st.plotly_chart(pair)
        

def kpi_dashboard():
    st.markdown("### KEY PERFORMANCE INDICATORS")
    
    st.markdown("KEY METRICS")
    Kpi1, Kpi2 = st.columns(2)
    Kpi1.metric("Average_tenure", value= 32, delta=-24)
    Kpi2.metric("Average_monthly_charges", value= 65.09, delta= +18.0)
    
    ## plot gender bar chart
    with Kpi1:
        churn_gender_counts = df.groupby(['gender', 'churn']).size().reset_index(name='count') #Groupby
        fig = px.bar(churn_gender_counts, x='gender', y='count', color='churn', barmode='group',
                color_discrete_map={'No': 'mediumseagreen', 'Yes': 'mediumvioletred'}) # Barplot and its settings.

        fig.update_layout(
            xaxis_title='Gender',
            yaxis_title='Count',
            title='Distribution of Churn in Gender') # Barplot layout

        st.plotly_chart(fig) # Display the chart
    
        ## Partner relationship
        partner_churn_counts = df.groupby(['partner', 'churn']).size().reset_index(name='totalcount') #Groupby
        pie = px.pie(partner_churn_counts, names='churn', values='totalcount',
                    color="churn", title="Impact of a partner relationship",
                color_discrete_map={'No': 'mediumseagreen', 'Yes': 'mediumvioletred'})
        
        st.plotly_chart(pie)
        
        
    
    ## Relationship between monthly charges and churn rate
    with Kpi2:
        charges= px.bar(df, x='monthlycharges', y='churn', color="churn", 
                        title='Impact of monthly charges on churn rate',
                        color_discrete_sequence=["mediumseagreen", "mediumvioletred"])
        st.plotly_chart(charges) # Display the chart
    
    ## Relationship between tenure and churn
        ax= px.bar(df, x='monthlycharges', y='internetservice',
                    color="churn", title="Impact of internet service on churn rate",
                    color_discrete_sequence=["mediumseagreen", "mediumvioletred"])
        
        st.plotly_chart(ax)
    
    ## Payment methods
        payment= px.bar(df, x="monthlycharges", y='paymentmethod',
                        color='churn', title='Influence of payment methods on churn rate',
                        color_discrete_sequence=["mediumseagreen", "mediumvioletred"])
        
        st.plotly_chart(payment) # Display the chart

if __name__ == "__main__":
    st.title("Dashboard")
    col1, col2 = st.columns(2)
    with col1:
        pass
    
    with col2:
        st.selectbox("Choose your visualizations",options= ["EDA", "KPIs"], key="slected_dashboard_type")
        
    if st.session_state["slected_dashboard_type"] == "EDA":
        eda_dashboard()
    else:
        kpi_dashboard()
        