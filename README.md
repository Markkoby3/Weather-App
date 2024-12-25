### README: Weather App

---

#### **Overview**
This is a Python-based Weather App built using `tkinter` for the graphical user interface (GUI) and the OpenWeatherMap API for real-time weather data retrieval. The app allows users to input a city name and displays current weather conditions, temperature, and additional metrics such as wind speed, humidity, and sunrise/sunset times.

---

#### **Features**
- **Real-time Weather Updates**: Get the latest weather information by entering a city name.
- **Detailed Metrics**: Includes current temperature, min/max temperatures, pressure, humidity, wind speed, and more.
- **User-Friendly GUI**: A simple interface with clear displays for weather data.
- **Error Handling**: Displays error messages for invalid city names or connectivity issues.

---

#### **Requirements**
- Python 3.8 or higher
- Libraries:
  - `tkinter` (standard with Python)
  - `requests` (install using `pip install requests`)

---

#### **How to Use**
1. Clone or download the repository containing the `weather_app.py` file.
2. Ensure all dependencies are installed (e.g., `requests`).
3. Run the app using:
   ```bash
   python weather_app.py
   ```
4. Enter a city name in the input field and press **Enter** to fetch the weather data.
5. The app will display:
   - Current weather condition (e.g., "Cloudy," "Clear")
   - Temperature (in °C)
   - Maximum and minimum temperatures
   - Pressure (in hPa)
   - Humidity (percentage)
   - Wind speed (in m/s)
   - Sunrise and sunset times

---

#### **Error Handling**
- If the city name is invalid or not found, the app displays an error message in red.
- If there’s an issue with the API or network, it displays "Unable to fetch data."

---

#### **Customization**
- Replace the API key in the code with your own key from OpenWeatherMap:
  ```python
  api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY"
  ```
- Modify the GUI elements by adjusting fonts, sizes, or colors in the `tkinter` code.

---

#### **License**
This project is free to use and modify. No specific license applies.
