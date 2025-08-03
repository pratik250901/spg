import streamlit as st
import pandas as pd
import pickle

# Streamlit App Interface
def get_features():
    st.title('Solar Power Prediction (Random Forest)')
    st.sidebar.title("Enter Weather & Solar Parameters")

    dist_to_solar_noon = st.sidebar.number_input("Distance to Solar Noon", key=1)
    temp = st.sidebar.number_input("Temperature", key=2)
    wind_dir = st.sidebar.number_input("Wind Direction", key=3)
    wind_speed = st.sidebar.number_input("Wind Speed", key=4)
    sky_cover = st.sidebar.number_input("Sky Cover", key=5)
    visibility = st.sidebar.number_input("Visibility", key=6)
    humidity = st.sidebar.number_input("Humidity", key=7)
    avg_wind_speed = st.sidebar.number_input("Average Wind Speed", key=8)
    avg_pressure = st.sidebar.number_input("Average Pressure", key=9)

    input_data = {
        'distance-to-solar-noon': dist_to_solar_noon,
        'temperature': temp,
        'wind-direction': wind_dir,
        'wind-speed': wind_speed,
        'sky-cover': sky_cover,
        'visibility': visibility,
        'humidity': humidity,
        'average-wind-speed': avg_wind_speed,
        'average-pressure': avg_pressure
    }

    features = pd.DataFrame([input_data])
    return features

# Load inputs
input_df = get_features()

# Predict and show results
if st.sidebar.button('Predict Solar Power'):
    try:
        model = pickle.load(open('deploy.pkl', 'rb'))
        prediction = model.predict(input_df)
        st.subheader("Predicted Solar Power Output")
        st.write(f"⚡ {prediction[0]:.2f} kW")
    except Exception as e:
        st.error(f"Error in prediction: {e}")
