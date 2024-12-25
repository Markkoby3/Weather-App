import tkinter as tk
import requests
import time

def getWeather(event=None):
    city = textfield.get()
    api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=7b9d491260b05e8dad1a60430da38ca9"
    try:
        json_data = requests.get(api).json()
        if json_data.get("cod") != 200:
            label1.config(text="Error: City not found", fg="red")
            label2.config(text="")
            return

        condition = json_data['weather'][0]['main']
        temp = int(json_data['main']['temp'] - 273.15)
        min_temp = int(json_data['main']['temp_min'] - 273.15)
        max_temp = int(json_data['main']['temp_max'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind_speed = json_data['wind']['speed']
        sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise']))
        sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset']))

        final_info = f"{condition}\n{temp}°C"
        final_data = (
            f"Max Temp: {max_temp}°C\n"
            f"Min Temp: {min_temp}°C\n"
            f"Pressure: {pressure} hPa\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind_speed} m/s\n"
            f"Sunrise: {sunrise}\n"
            f"Sunset: {sunset}"
        )
        label1.config(text=final_info, fg="black")
        label2.config(text=final_data, fg="black")
    except Exception as e:
        label1.config(text="Error: Unable to fetch data", fg="red")
        label2.config(text="")

canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textfield = tk.Entry(canvas, font=t)
textfield.pack(pady=20)
textfield.focus()
textfield.bind('<Return>', getWeather)  # Bind Enter key to getWeather

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()

canvas.mainloop()
