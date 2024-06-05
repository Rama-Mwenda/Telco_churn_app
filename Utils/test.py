import streamlit as st 
import pandas as pd
import numpy as np 
from streamlit_lottie import st_lottie

st.title("Hello World")
st.header("This is my header")
st.subheader("This is my subheader")

st.markdown("### This is my markdown")

status= st.radio("Select gender:", ("male", "female"))
if (status=="male"):
    st.write("You selected male")
else:
    st.success("You selected female")
    
hobby= st.selectbox("Hobbies:", ["Dancing", "Sports", "Reading", "Horseriding"])
st.write("Your hobby is:", hobby)

name= st.text_input("Enter your name", "Type here____")
if (st.button("submit")):
    result= name.title()
    st.success(result)
    
level= st.slider("Select level:", 1,5)
st.text("Selected: {}".format(level))

number= st.number_input("Enter a number")
st.write("Your number", number)


url= "https://lottiefiles.com/search?q=navigation&category=animations"
st_lottie(url, key="user")