from ultralytics import YOLO

try:
    model = YOLO("models/best_weapon.pt")
except Exception as e:
    print("⚠️ Custom model load failed, using default YOLOv8n:", e)
    model = YOLO("yolov8n.pt")


def detect_weapons(frame):
    results = model(frame)
    return results[0].plot()
