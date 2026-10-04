import cv2
from src.detection import detect_weapons


def main():
    # Webcam open karo
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Webcam not accessible")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Weapon detection run karo
        annotated_frame = detect_weapons(frame)

        # Output show karo
        cv2.imshow("Weapon Detection", annotated_frame)

        # 'q' dabao to exit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
