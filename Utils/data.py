import streamlit as st 
import pyodbc
import pandas as pd

## create a connection to a database
@st.cache_resource(show_spinner="connecting to database...")
def init_connection():
    connection_string = (
        "DRIVER={SQL Server};"
        "SERVER=" + st.secrets['SERVER'] + ";"
        "DATABASE=" + st.secrets['DATABASE'] + ";"
        "UID=" + st.secrets['USERNAME'] + ";"
        "PWD=" + st.secrets['PASSWORD']
    )
    return pyodbc.connect(connection_string)
 
conn = init_connection()

@st.cache_data(show_spinner="Running query...")
def running_query(query):
    with conn.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        df = pd.DataFrame.from_records(rows, columns=columns)
    return df


def get_all_columns():
    sql_query = "SELECT * FROM dbo.LP2_Telco_churn_first_3000"
    df = running_query(sql_query)
    return df

data1= get_all_columns()
