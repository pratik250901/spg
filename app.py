import streamlit as st
import pandas as pd
import pickle
def get_features():
    st.title('Solar Panel Regression Deployment')
    st.sidebar.title("Enter Parameters Values")

    dist_to_solar_moon = st.number_input("Insert a number",key=1)
    temp = st.number_input("Insert a number",key=2)
    wind_dir = st.number_input("Insert a number",key=3)
    wind_speed = st.number_input("Insert a number",key=4) 
    sky_cover = st.number_input("Insert a number")
    visibility = st.number_input("Insert a number",key=5)
    humidity = st.number_input("Insert a number",key=6)
    avg_wind_speed = st.number_input("Insert a number",key=7)
    avg_pressure = st.number_input("Insert a number",key=8)
    
    data = {
        'distance-to-solar-noon':dist_to_solar_moon,  
        'humidity':humidity, 
}
        

    features = pd.DataFrame(data,index=[0])
    return features


xvals=get_features()
if st.sidebar.button('Submit'):
    st.write(xvals)
    loaded_model=pickle.load(open('deploy.pkl','rb'))
    result=loaded_model.predict(xvals)
    st.write(result)
