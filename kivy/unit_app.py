# weather_app.py
import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

# Replace with your own OpenWeatherMap API key
API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"


class WeatherApp(App):
    def build(self):
        self.layout = BoxLayout(orientation="vertical", padding=20, spacing=20)

        # City input
        self.city_input = TextInput(hint_text="Enter city name", multiline=False)
        self.layout.add_widget(self.city_input)

        # Get weather button
        get_weather_btn = Button(text="Get Weather", size_hint=(1, None), height=50)
        get_weather_btn.bind(on_press=self.get_weather)
        self.layout.add_widget(get_weather_btn)

        # Result label
        self.result_label = Label(text="Weather info will appear here", font_size=18)
        self.layout.add_widget(self.result_label)

        return self.layout

    def get_weather(self, instance):
        city = self.city_input.text.strip()
        if not city:
            self.result_label.text = "Please enter a city name"
            return

        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url)
            data = response.json()

            if data.get("cod") != 200:
                self.result_label.text = f"City not found!"
                return

            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            description = data["weather"][0]["description"].capitalize()

            self.result_label.text = f"City: {city}\nTemperature: {temp}°C\nHumidity: {humidity}%\nCondition: {description}"

        except Exception as e:
            self.result_label.text = f"Error fetching data: {str(e)}"


if __name__ == "__main__":
    WeatherApp().run()
