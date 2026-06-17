# 🌤️ WeatherVision Dashboard

A modern and interactive Weather Analytics Dashboard built using Streamlit and Open-Meteo APIs.

---

## 🚀 Overview

WeatherVision Dashboard provides real-time weather information, forecasts, and environmental insights through a clean and responsive interface.

The application uses Open-Meteo APIs for accurate weather forecasting and geolocation services without requiring any API key.

---

## ✨ Features

### 🌡 Real-Time Weather

* Current Temperature
* Feels Like Temperature
* Weather Conditions
* Humidity
* Wind Speed
* Wind Direction

### 📅 7-Day Forecast

* Daily High Temperature
* Daily Low Temperature
* Weather Conditions
* Forecast Visualization

### 🌍 Location Search

* Search any city worldwide
* Automatic coordinate detection
* Country information

### ☀ Sun Information

* Sunrise Time
* Sunset Time
* Day/Night Status

### 📊 Interactive Analytics

* Temperature Trends
* Humidity Trends
* Forecast Charts
* Plotly Visualizations

### ⚡ Fast Performance

* Streamlit Caching
* Optimized API Calls
* Responsive Dashboard

### 🔐 No API Key Required

Powered entirely by Open-Meteo APIs.

---

## 🛠 Tech Stack

| Technology     | Purpose            |
| -------------- | ------------------ |
| Python         | Backend Logic      |
| Streamlit      | Web UI             |
| Open-Meteo API | Weather Data       |
| Pandas         | Data Processing    |
| Plotly         | Interactive Charts |
| Requests       | API Integration    |

---

## 📂 Project Structure

weather-vision-dashboard/

├── app.py

├── weather_service.py

├── utils.py

├── requirements.txt

├── README.md

├── screenshots/

└── assets/

---

## ⚙ Installation

### Clone Repository

git clone https://github.com/yourusername/weather-vision-dashboard.git

### Enter Project Folder

cd weather-vision-dashboard

### Install Dependencies

pip install -r requirements.txt

### Run Application

streamlit run app.py

---

## 🌍 APIs Used

### Geocoding API

https://geocoding-api.open-meteo.com/v1/search

Used to convert city names into latitude and longitude.

### Forecast API

https://api.open-meteo.com/v1/forecast

Used for current weather and forecast information.

### Air Quality API

https://air-quality-api.open-meteo.com/v1/air-quality

Used to retrieve AQI and pollution data.

---

## 📈 Future Enhancements

* 🌍 Weather Maps
* 🛰 Satellite View
* 📱 Mobile Optimization
* 🤖 AI Weather Insights
* 🔔 Severe Weather Alerts
* 🌧 Rain Probability Forecast
* 🏙 Favorite Locations

---

## 🤝 Contributions

Contributions are welcome.

Fork the repository and submit a pull request.

---

## ⭐ Support

If you like this project:

⭐ Star the repository

🍴 Fork the project

📢 Share with others

---

## 📄 License

MIT License

---

Made with ❤️ using Python and Streamlit
