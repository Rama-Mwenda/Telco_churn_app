import streamlit as st

## Change the layout of the application
st.set_page_config(page_title="Home Page", page_icon="🏡", layout="wide")
st.title("CHURN CIPHER")


col1, col2 = st.columns(spec=[17, 15], gap="medium")
with col1:
    container = st.container(height=300, border=False)
    with container:
        st.markdown("""
                <img 
                src="https://webengage.com/blog/wp-content/uploads/sites/4/2019/08/Untitled-1.gif"
                width= 500 height= 300>""", unsafe_allow_html=True )
with col2:
    st.write("""
             ## **INSIGHT**
             
    *This is an interactive application that provides 
    curated information about customers and predicts the 
    churn rate of the customers based on the given data.*"""
    )

col3, col4, col5= st.columns(spec=[12,12,11])
  
with col3:
    container= st.container(height=400)
    with container:
        st.markdown(
"""
<img src="https://img.icons8.com/?size=100&id=iXwUKT27nqsX&format=gif&color=000000" width="40" height="40" />

### *Navigation information*

- **Data** : Represents the data sources available.
- **Dashboard** : Interactive visualizations that show churn rate variables.
- **Predict**: Showcases the possibility of customer to churn.
- **History** : Review of activities that have happened.
"""
, unsafe_allow_html=True) 
with col4:
    container= st.container(height=400)
    with container:
        st.markdown(
        """
        <img src="https://img.icons8.com/?size=100&id=26293&format=png&color=000000" width="40" height="40" />
        
        ### *Machine Embeddedment*
        
        - **Model Selection** : Operate between best performing models.
        - **Seamless integration** : Integrate your predictions into your workflow with a user friendly interface.
        - **Probabilities**: Gain insights on your customer's needs on service delivery.
        """, unsafe_allow_html=True) 
with col5:
    container= st.container(height=400)
    with container:
        st.markdown(
        """
        <img src="https://img.icons8.com/?size=100&id=R6AotCTJVJhE&format=gif&color=000000" width="40" height="40" />
        
    ### *Benefits*
        
    - **Data_driven decisions** : Make informed decisions backed by accurate analysis.
    - **Market_strategies** : Work on restructuring strategies that benefit the consumer.
    - **Efficient machine learning** : Optimize the power of machine learning effortlessly.
        """, unsafe_allow_html=True)
    
container= st.container(height=250, border=False)
with container:
    st.subheader("Enquiries")

    st.markdown(
"""
If you have any enquiries, feel free to reach out to us:
""")
    st.link_button("Enquiries", 'https://github.com/Creative-Parasite/Telco_churn_app')
    st.link_button("LINKED IN", 'www.linkedin.com/in/evalyne-kamuri')
    lIVE_DEMO = st.button("LIVE DEMO")
    if lIVE_DEMO:
        media = open("assets/CHURN CIPHER.mp4", "rb")
        st.video(media,format="mp4")