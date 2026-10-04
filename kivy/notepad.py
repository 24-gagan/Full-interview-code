# simple_notepad.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
import os


class NotepadApp(App):
    def build(self):
        self.layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        # Text input area
        self.text_area = TextInput(multiline=True, font_size=16)
        self.layout.add_widget(self.text_area)

        # Buttons layout
        btn_layout = BoxLayout(size_hint=(1, None), height=50, spacing=10)

        save_btn = Button(text="Save")
        save_btn.bind(on_press=self.save_file)
        btn_layout.add_widget(save_btn)

        open_btn = Button(text="Open")
        open_btn.bind(on_press=self.open_file)
        btn_layout.add_widget(open_btn)

        self.layout.add_widget(btn_layout)
        return self.layout

    def save_file(self, instance):
        content = self.text_area.text
        if not content.strip():
            return  # do nothing if empty

        # Open save dialog
        self.file_chooser_popup("Save File", "save")

    def open_file(self, instance):
        # Open open dialog
        self.file_chooser_popup("Open File", "open")

    def file_chooser_popup(self, title, mode):
        filechooser = FileChooserIconView()
        popup_layout = BoxLayout(orientation="vertical")
        popup_layout.add_widget(filechooser)

        btn_layout = BoxLayout(size_hint=(1, None), height=50, spacing=10)
        select_btn = Button(text="Select")
        cancel_btn = Button(text="Cancel")
        btn_layout.add_widget(select_btn)
        btn_layout.add_widget(cancel_btn)
        popup_layout.add_widget(btn_layout)

        popup = Popup(title=title, content=popup_layout, size_hint=(0.9, 0.9))

        def select_file(instance):
            selected = filechooser.selection
            if selected:
                file_path = selected[0]
                if mode == "open":
                    with open(file_path, "r", encoding="utf-8") as f:
                        self.text_area.text = f.read()
                elif mode == "save":
                    # Save to selected path
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(self.text_area.text)
                popup.dismiss()

        def cancel(instance):
            popup.dismiss()

        select_btn.bind(on_press=select_file)
        cancel_btn.bind(on_press=cancel)
        popup.open()


if __name__ == "__main__":
    NotepadApp().run()
