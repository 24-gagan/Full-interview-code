import tkinter as tk
from tkinter import messagebox
import requests


# ------------------ Weather Function ------------------
def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name")
        return

    api_key = "YOUR_API_KEY_HERE"  # Replace with your OpenWeatherMap API key
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            temp = data["main"]["temp"]
            weather_desc = data["weather"][0]["description"].title()
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            result_text = (
                f"Weather in {city}:\n"
                f"Temperature: {temp}°C\n"
                f"Condition: {weather_desc}\n"
                f"Humidity: {humidity}%\n"
                f"Wind Speed: {wind_speed} m/s"
            )
            result_label.config(text=result_text)
        else:
            messagebox.showerror("Error", f"City not found: {data['message']}")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Cannot connect to weather service.\n{e}")


# ------------------ Tkinter GUI ------------------
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")
root.resizable(False, False)

# Heading
heading = tk.Label(root, text="Weather App", font=("Arial", 18, "bold"))
heading.pack(pady=10)

# City input
city_frame = tk.Frame(root)
city_frame.pack(pady=5)

city_label = tk.Label(city_frame, text="Enter City: ", font=("Arial", 12))
city_label.pack(side=tk.LEFT)

city_entry = tk.Entry(city_frame, font=("Arial", 12))
city_entry.pack(side=tk.LEFT)

# Search button
search_btn = tk.Button(
    root, text="Get Weather", font=("Arial", 12), command=get_weather
)
search_btn.pack(pady=10)

# Result display
result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

# Run GUI
root.mainloop()
