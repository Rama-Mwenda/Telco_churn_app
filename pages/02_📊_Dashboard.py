import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.figure_factory as ff

st.set_page_config(
    page_title="Dashboard Page", 
    page_icon="📊", 
    layout="wide"
    )
  
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
    
    chart1, chart2 = st.columns(spec=[4,4])
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
        ## Distribution of monthly charges by contract
        violin = px.violin(df, x='monthlycharges', y='contract', title="Distribution of monthly charges by contract",
                           color_discrete_sequence=['lightsalmon', 'lightskyblue']
                           )
        st.plotly_chart(violin)
        
        ## Distribution of contract by tenure
        violin = px.violin(df, x='monthlycharges', y='paymentmethod', title='Distribution of monthly charges by paymentmethod',
                           color_discrete_sequence=["lightsalmon", "lightskyblue"])
        st.plotly_chart(violin)
        
        ## Distribution of internet services by monthly charges
        box = px.box(df, x='monthlycharges', y='internetservice', title='Distribution of monthlycharges by internet services',
                           color_discrete_sequence=['lightsalmon', 'lightskyblue'])
        st.plotly_chart(box)
    
    ## Correlation matrix of numeric columns
    numeric_columns = df.select_dtypes(include=['int64','Float64']).columns
    if len(numeric_columns) > 1:
        correlation_matrix = df[numeric_columns].corr()
        fig= px.imshow(correlation_matrix, text_auto=True, color_continuous_scale='peach', 
                       title="Correlation matrix", width=500, height=500 )
        st.plotly_chart(fig)
        
def kpi_dashboard():
    st.markdown("### KEY PERFORMANCE INDICATORS")
    st.markdown("#### KEY METRICS")
    
    # Compute key metrics from the DataFrame
    avg_tenure = df['tenure'].mean()
    avg_monthly_charges = df['monthlycharges'].mean()
    churn_rate = df['churn'].value_counts(normalize=True).get('Yes', 0) * 100
    
    Kpi1, Kpi2,Kpi3 = st.columns(spec=[5,5,2])
    Kpi1.metric("Average_tenure", value= (round(avg_tenure,2)), delta=-24)
    Kpi2.metric("Average_monthly_charges", value= (round(avg_monthly_charges,2)), delta= +18.0)
    Kpi3.metric("Average_churn_rate", value= (round(churn_rate,2,)), delta= +20)
    
    with Kpi1:
        churn_gender_counts = df.groupby(['gender', 'churn']).size().reset_index(name='count') #Groupby
        fig = px.bar(churn_gender_counts, x='gender', y='count', color='churn', barmode='group',
                color_discrete_map={'No': 'mediumseagreen', 'Yes': 'mediumvioletred'}) # Barplot and its settings.

        fig.update_layout(
            xaxis_title='Gender',
            yaxis_title='Count',
            title='Distribution of Churn by Gender') # Barplot layout

        st.plotly_chart(fig) # Display the chart
    
        ## Partner relationship
        partner_churn_counts = df.groupby(['partner', 'churn']).size().reset_index(name='totalcount') #Groupby
        pie = px.pie(partner_churn_counts, names='churn', values='totalcount',
                    color="churn", title="Impact of a partner relationship",
                color_discrete_map={'No': 'mediumseagreen', 'Yes': 'mediumvioletred'})
        
        st.plotly_chart(pie)
        
        # Group by seniorcitizen and churn
        churn_Senior_citizen = df.groupby(['seniorcitizen', 'churn']).size().reset_index(name='totalcount')

        # Create a bar plot
        fig = px.bar(churn_Senior_citizen, 
             x=['seniorcitizen', 'churn'],  # x-axis: seniorcitizen and churn
             y='totalcount',  # y-axis: total count
             color='churn',  # color by churn
             barmode='group',  # group bars by seniorcitizen
             title='Churn by Senior Citizen',  # title
             labels={'seniorcitizen': 'Senior Citizen', 'churn': 'Churn', 'totalcount': 'Total Count'})  # axis labels

        # Show the plot
        st.plotly_chart(fig)  
    
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
    
    col1, col2= st.columns(2)
    with col1:
        pass
    
    with col2:
        st.selectbox("Choose your visualizations",options= ["EDA", "KPIs"], key="selected_dashboard_type")
        
    if st.session_state["selected_dashboard_type"] == "EDA":
        eda_dashboard()
    else:
        kpi_dashboard()
        