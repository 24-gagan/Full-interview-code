from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner


class UnitConverterApp(App):
    def build(self):
        self.layout = BoxLayout(orientation="vertical", padding=20, spacing=20)

        # Input field
        self.input_value = TextInput(
            hint_text="Enter value", font_size=30, multiline=False, input_filter="float"
        )
        self.layout.add_widget(self.input_value)

        # From unit selection
        self.from_unit = Spinner(
            text="Select Unit",
            values=("Celsius", "Fahrenheit", "Meter", "Kilometer", "Gram", "Kilogram"),
            font_size=25,
        )
        self.layout.add_widget(self.from_unit)

        # To unit selection
        self.to_unit = Spinner(
            text="Convert To",
            values=("Celsius", "Fahrenheit", "Meter", "Kilometer", "Gram", "Kilogram"),
            font_size=25,
        )
        self.layout.add_widget(self.to_unit)

        # Convert button
        convert_btn = Button(text="Convert", font_size=30)
        convert_btn.bind(on_press=self.convert)
        self.layout.add_widget(convert_btn)

        # Result label
        self.result_label = Label(text="Result: ", font_size=30)
        self.layout.add_widget(self.result_label)

        return self.layout

    def convert(self, instance):
        try:
            value = float(self.input_value.text)
            from_u = self.from_unit.text
            to_u = self.to_unit.text
            result = None

            # Temperature conversion
            if from_u == "Celsius" and to_u == "Fahrenheit":
                result = (value * 9 / 5) + 32
            elif from_u == "Fahrenheit" and to_u == "Celsius":
                result = (value - 32) * 5 / 9
            elif from_u == "Celsius" and to_u == "Celsius":
                result = value
            elif from_u == "Fahrenheit" and to_u == "Fahrenheit":
                result = value

            # Length conversion
            elif from_u == "Meter" and to_u == "Kilometer":
                result = value / 1000
            elif from_u == "Kilometer" and to_u == "Meter":
                result = value * 1000
            elif from_u == "Meter" and to_u == "Meter":
                result = value
            elif from_u == "Kilometer" and to_u == "Kilometer":
                result = value

            # Weight conversion
            elif from_u == "Gram" and to_u == "Kilogram":
                result = value / 1000
            elif from_u == "Kilogram" and to_u == "Gram":
                result = value * 1000
            elif from_u == "Gram" and to_u == "Gram":
                result = value
            elif from_u == "Kilogram" and to_u == "Kilogram":
                result = value
            else:
                result = "Invalid conversion!"

            self.result_label.text = f"Result: {result}"
        except ValueError:
            self.result_label.text = "Please enter a valid number."


if __name__ == "__main__":
    UnitConverterApp().run()
