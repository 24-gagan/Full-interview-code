# bmi_calculator.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class BMICalculatorApp(App):
    def build(self):
        self.layout = BoxLayout(orientation="vertical", padding=20, spacing=20)

        # Weight input
        self.weight_input = TextInput(
            hint_text="Enter weight in kg", multiline=False, input_filter="float"
        )
        self.layout.add_widget(self.weight_input)

        # Height input
        self.height_input = TextInput(
            hint_text="Enter height in cm", multiline=False, input_filter="float"
        )
        self.layout.add_widget(self.height_input)

        # Calculate button
        calc_button = Button(text="Calculate BMI", size_hint=(1, None), height=50)
        calc_button.bind(on_press=self.calculate_bmi)
        self.layout.add_widget(calc_button)

        # Result label
        self.result_label = Label(text="Your BMI: ", font_size=20)
        self.layout.add_widget(self.result_label)

        return self.layout

    def calculate_bmi(self, instance):
        try:
            weight = float(self.weight_input.text)
            height_cm = float(self.height_input.text)
            height_m = height_cm / 100  # convert cm to meters

            bmi = weight / (height_m**2)
            category = self.get_bmi_category(bmi)

            self.result_label.text = f"Your BMI: {bmi:.2f} ({category})"
        except ValueError:
            self.result_label.text = "Please enter valid numbers for weight and height"

    def get_bmi_category(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 25 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obesity"


if __name__ == "__main__":
    BMICalculatorApp().run()
