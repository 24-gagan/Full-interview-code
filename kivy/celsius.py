# temperature_converter.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner


class TemperatureConverterApp(App):
    def build(self):
        self.layout = BoxLayout(orientation="vertical", padding=20, spacing=20)

        # Input field
        self.input_text = TextInput(
            hint_text="Enter temperature", multiline=False, input_filter="float"
        )
        self.layout.add_widget(self.input_text)

        # From unit spinner
        self.from_unit = Spinner(
            text="Celsius",
            values=("Celsius", "Fahrenheit", "Kelvin"),
            size_hint=(1, None),
            height=44,
        )
        self.layout.add_widget(self.from_unit)

        # To unit spinner
        self.to_unit = Spinner(
            text="Fahrenheit",
            values=("Celsius", "Fahrenheit", "Kelvin"),
            size_hint=(1, None),
            height=44,
        )
        self.layout.add_widget(self.to_unit)

        # Convert button
        convert_button = Button(text="Convert", size_hint=(1, None), height=50)
        convert_button.bind(on_press=self.convert_temperature)
        self.layout.add_widget(convert_button)

        # Result label
        self.result_label = Label(text="Result: ", font_size=20)
        self.layout.add_widget(self.result_label)

        return self.layout

    def convert_temperature(self, instance):
        try:
            temp = float(self.input_text.text)
            from_unit = self.from_unit.text
            to_unit = self.to_unit.text

            # Convert input temperature to Celsius first
            if from_unit == "Celsius":
                celsius = temp
            elif from_unit == "Fahrenheit":
                celsius = (temp - 32) * 5 / 9
            elif from_unit == "Kelvin":
                celsius = temp - 273.15
            else:
                celsius = temp

            # Convert Celsius to target unit
            if to_unit == "Celsius":
                result = celsius
            elif to_unit == "Fahrenheit":
                result = celsius * 9 / 5 + 32
            elif to_unit == "Kelvin":
                result = celsius + 273.15
            else:
                result = celsius

            self.result_label.text = f"Result: {result:.2f} {to_unit}"
        except ValueError:
            self.result_label.text = "Please enter a valid number"


if __name__ == "__main__":
    TemperatureConverterApp().run()
