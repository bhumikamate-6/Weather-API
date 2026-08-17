import requests
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("WEATHER_APP_KEY")

st.set_page_config(
    page_title="Weather App",
    page_icon="🌤️"
)

st.title("🌤️ Weather App")

st.write("Enter city name")

city = st.text_input("Enter city name")

if st.button("Fetch Weather Data"):

    if city.strip() == "":
        st.warning("Please enter a city name.")

    else:
        API_URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

        response = requests.get(API_URL)

        if response.status_code == 200:

            st.success("Data fetched successfully!")

            data = response.json()

            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            weather = data["weather"][0]["main"]

            # Convert Kelvin to Celsius
            temperature = temperature - 273.15

            col1, col2 = st.columns(2)
            col3, col4 = st.columns(2)

            col1.metric("🌡️ Temperature", f"{temperature:.2f} °C")
            col2.metric("💧 Humidity", f"{humidity}%")
            col3.metric("💨 Wind Speed", f"{wind_speed} m/s")
            col4.metric("☁️ Weather", weather)

        else:
            st.error("❌ Invalid city name or weather data unavailable.")