from ultralytics import YOLO


def main():
    # Pretrained YOLOv8 model load karo
    model = YOLO("yolov8n.pt")  # lightweight pretrained model

    # Train model on dataset
    model.train(
        data="configs/yolo_config.yaml",  # correct YAML config file
        epochs=50,  # training epochs
        imgsz=640,  # image size
        batch=16,  # batch size
        project="runs/train",  # output folder
        name="weapon_model",  # experiment name
    )


if __name__ == "__main__":
    main()
