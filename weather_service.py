import requests


class WeatherService:
    GEO_URL = "https://geocoding-api.open-meteo.com/v1/search"

    WEATHER_URL = "https://api.open-meteo.com/v1/forecast"

    AIR_QUALITY_URL = "https://air-quality-api.open-meteo.com/v1/air-quality"

    def get_coordinates(self, city):
        params = {
            "name": city,
            "count": 1,
            "language": "en",
            "format": "json"
        }

        response = requests.get(self.GEO_URL, params=params)

        if response.status_code == 200:
            data = response.json()

            if "results" in data:
                result = data["results"][0]

                return {
                    "city": result["name"],
                    "country": result["country"],
                    "latitude": result["latitude"],
                    "longitude": result["longitude"]
                }

        return None

    def get_weather(self, lat, lon):
        params = {
            "latitude": lat,
            "longitude": lon,

            "current": [
                "temperature_2m",
                "relative_humidity_2m",
                "apparent_temperature",
                "weather_code",
                "wind_speed_10m",
                "wind_direction_10m",
                "is_day"
            ],

            "daily": [
                "temperature_2m_max",
                "temperature_2m_min",
                "weather_code",
                "sunrise",
                "sunset"
            ],

            "hourly": [
                "temperature_2m",
                "relative_humidity_2m"
            ],

            "forecast_days": 7,
            "timezone": "auto"
        }

        response = requests.get(self.WEATHER_URL, params=params)

        if response.status_code == 200:
            return response.json()

        return None

    def get_air_quality(self, lat, lon):
        params = {
            "latitude": lat,
            "longitude": lon,

            "hourly": [
                "pm10",
                "pm2_5",
                "carbon_monoxide",
                "nitrogen_dioxide",
                "ozone"
            ]
        }

        response = requests.get(
            self.AIR_QUALITY_URL,
            params=params
        )

        if response.status_code == 200:
            return response.json()

        return None