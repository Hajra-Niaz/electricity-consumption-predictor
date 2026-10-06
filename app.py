import streamlit as st
import numpy as np
import joblib as jb
model=jb.load('elec.pkl')
st.set_page_config(page_title="Electricity Consumption Predictor",page_icon="🔍",layout="centered")
st.sidebar.title("Navigator:")
page=st.sidebar.radio("Menu:",['Home','Predictor','Team','About'])
if page=="Home":
    st.title("This is the Web App to predict a Next_Month_Consumption_kWh")
    st.header("Problem Statement:")
    st.info("Develop a machine learning model to predict next month’s electricity consumption (in kWh) based on temperature, number of residents, and past consumption.")
    st.header("Goal")
    st.info("Estimate future energy usage to help with demand forecasting and energy management.")
elif page=='Predictor':
    st.title("Electricity Consumption Checker")
    #Inputs
    Month=st.number_input("Enter Month",min_value=1,max_value=12,value=6)
    Avg_Temperature_C=st.number_input("Enter Avg_Temperature_C",min_value=5,max_value=45,value=30)
    Residents=st.number_input("Enter No: of Residents",min_value=1,value=4)
    Past_Month_Consumption_kWh=st.number_input("Enter Past_Month_Consumption_kWh",min_value=50,value=300)
    if st.button('Predict'):
        input_data=np.array([[Month,Avg_Temperature_C,Residents,Past_Month_Consumption_kWh]])
        result=model.predict(input_data)[0]
        st.success(f" **Predicted Next_Month_Consumption is:** {round(result, 2)}_kWh ")
elif page=="Team":
        st.title("👩‍💻Team Members")
        st.write("Meet the developers behind this project:")
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Zainab Abbasi")
            st.write("Data Scientist | Model Developer | Interface Designer")
        with col2:
            st.subheader("Hajra Khan")
            st.write("ML Engineer | Data Analyst | Research & Evaluation|")   
elif page=="About":
    st.title("ℹ️ About This Project")
    st.write("""
    This application is a **Machine Learning practice project** developed to demonstrate 
    the power of AI in **Energy Management and Demand Forecasting**.

    **The Problem:** Predicting next month's electricity consumption helps households and 
    utility companies plan energy usage, reduce waste, and optimize costs.

    **How It Works:**
    The app uses a **Linear Regression** model trained on 1,000 historical records. 
    It analyzes four key inputs to make its prediction:
    - 📅 Month of the year (1-12)
    - 🌡️ Average Temperature (°C)
    - 🏠 Number of Residents
    - ⚡ Past Month's Consumption (kWh)

    **Technologies Used:**
    - Python 🐍
    - Pandas & NumPy 📊
    - Scikit-learn 🤖
    - Streamlit 🌐
    - Joblib 📦

    **Future Enhancements:**
    - 📈 Advanced models (Random Forest, XGBoost) for higher accuracy
    - 🗓️ Seasonal and weather-based trend analysis
    - 📊 A dashboard for comparing historical vs. predicted usage
    """)

    st.info("Developed by: ")
    st.info("Zainab Abbasi & Hajra Khan")