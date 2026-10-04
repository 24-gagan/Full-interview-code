import cv2

# Haar Cascade classifier load karo (OpenCV ke saath aata hai)
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)


def detect_faces_from_webcam():
    # Webcam open karo (0 = default camera)
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Faces detect karo
        faces = face_cascade.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
        )

        # Har face ke around rectangle draw karo
        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Output show karo
        cv2.imshow("Webcam Face Detection", frame)

        # 'q' dabao exit ke liye
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


def detect_faces_from_image(image_path):
    # Image load karo
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Faces detect karo
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Rectangle draw karo
    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow("Image Face Detection", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    print("Choose mode:")
    print("1. Webcam detection")
    print("2. Image detection")

    choice = input("Enter 1 or 2: ")

    if choice == "1":
        detect_faces_from_webcam()
    elif choice == "2":
        path = input("Enter image path: ")
        detect_faces_from_image(path)
    else:
        print("Invalid choice!")
