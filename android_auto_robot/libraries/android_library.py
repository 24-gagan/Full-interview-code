import os
import time


class ADBLibrary:

    def connect_device(self):
        os.system("adb devices")

    def launch_android_auto(self):
        os.system(
            "adb shell am start -n com.google.android.projection.gearhead/.GearheadActivity"
        )

    def tap_screen(self, x, y):
        os.system(f"adb shell input tap {x} {y}")

    def get_logs(self):
        os.system("adb logcat -d > android_auto_log.txt")

    def play_pause_media(self):
        os.system("adb shell input keyevent 85")

    def take_screenshot(self):
        os.system("adb shell screencap /sdcard/aa.png")
        os.system("adb pull /sdcard/aa.png")
