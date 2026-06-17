import streamlit as st
import pandas as pd
import plotly.express as px

from weather_service import WeatherService
from utils import get_weather_description


st.set_page_config(
    page_title="WeatherVision Dashboard",
    page_icon="🌤",
    layout="wide"
)

service = WeatherService()

st.title("🌤 WeatherVision Dashboard")
st.markdown("Real-Time Weather Analytics Dashboard")

city = st.text_input(
    "🔍 Enter City Name",
    placeholder="e.g. London, Delhi, New York"
)

if city:

    location = service.get_coordinates(city)

    if location:

        weather = service.get_weather(
            location["latitude"],
            location["longitude"]
        )

        air = service.get_air_quality(
            location["latitude"],
            location["longitude"]
        )

        current = weather["current"]

        st.success(
            f"📍 {location['city']}, {location['country']}"
        )

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "🌡 Temperature",
                f"{current['temperature_2m']} °C"
            )

        with col2:
            st.metric(
                "💧 Humidity",
                f"{current['relative_humidity_2m']}%"
            )

        with col3:
            st.metric(
                "🌬 Wind Speed",
                f"{current['wind_speed_10m']} km/h"
            )

        with col4:
            st.metric(
                "🤔 Feels Like",
                f"{current['apparent_temperature']} °C"
            )

        st.subheader("Current Condition")

        st.info(
            get_weather_description(
                current["weather_code"]
            )
        )

        st.divider()

        st.subheader("📅 7-Day Forecast")

        forecast_df = pd.DataFrame({

            "Date": weather["daily"]["time"],

            "Max Temp":
                weather["daily"]["temperature_2m_max"],

            "Min Temp":
                weather["daily"]["temperature_2m_min"]

        })

        st.dataframe(
            forecast_df,
            use_container_width=True
        )

        fig = px.line(
            forecast_df,
            x="Date",
            y=["Max Temp", "Min Temp"],
            title="Temperature Trend"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.divider()

        st.subheader("🌍 Air Quality")

        latest_pm25 = air["hourly"]["pm2_5"][0]
        latest_pm10 = air["hourly"]["pm10"][0]

        aqi1, aqi2 = st.columns(2)

        with aqi1:
            st.metric(
                "PM2.5",
                latest_pm25
            )

        with aqi2:
            st.metric(
                "PM10",
                latest_pm10
            )

        st.divider()

        st.subheader("☀ Sunrise & Sunset")

        sun1, sun2 = st.columns(2)

        with sun1:
            st.write(
                weather["daily"]["sunrise"][0]
            )

        with sun2:
            st.write(
                weather["daily"]["sunset"][0]
            )

    else:
        st.error("City not found")