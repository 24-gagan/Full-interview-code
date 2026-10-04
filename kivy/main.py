from kivy.app import App  # Base class for kivy apps
from kivy.uix.boxlayout import BoxLayout  # Layout for widgits
from kivy.clock import Clock  # used for scheduling events
from kivy.uix.label import Label  # display text
from kivy.uix.button import Button  # create button


class StopwatchApp(App):  # main class of the app
    def build(self):  # build the UI
        self.seconds = 0  # keep track of seconds
        self.running = False  # True if time is running

        # Main layout
        self.layout = BoxLayout(
            orientation="vertical", padding=20, spacing=20
        )  # main layout

        # Timer display
        self.label = Label(text="00:00:00", font_size=50)  # main label to display time
        self.layout.add_widget(self.label)  # initially show 00:00:00

        # Buttons layout
        buttons_layout = BoxLayout(
            size_hint=(1, 0.3), spacing=20
        )  # Horizontal layout for buttons

        # Start button
        self.start_btn = Button(text="Start")
        self.start_btn.bind(on_press=self.start)
        buttons_layout.add_widget(self.start_btn)

        # Pause button
        self.pause_btn = Button(text="Pause")
        self.pause_btn.bind(on_press=self.pause)
        buttons_layout.add_widget(self.pause_btn)

        # Reset button
        self.reset_btn = Button(text="Reset")
        self.reset_btn.bind(on_press=self.reset)
        buttons_layout.add_widget(self.reset_btn)

        self.layout.add_widget(buttons_layout)
        return self.layout

    def update_time(self, dt):
        if self.running:
            self.seconds += 1
            hrs = self.seconds // 3600
            mins = (self.seconds % 3600) // 60
            secs = self.seconds % 60
            self.label.text = f"{hrs:02d}:{mins:02d}:{secs:02d}"

    def start(self, instance):
        if not self.running:
            self.running = True
            # Schedule update every 1 second
            Clock.schedule_interval(self.update_time, 1)

    def pause(self, instance):
        self.running = False

    def reset(self, instance):
        self.running = False
        self.seconds = 0
        self.label.text = "00:00:00"


if __name__ == "__main__":
    StopwatchApp().run()
