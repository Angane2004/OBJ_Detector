from ultralytics import YOLO 
import cvzone
import cv2

def run_detection():
    # Load the model
    model = YOLO('yolov10n.pt')

    # Live webcam
    cap = cv2.VideoCapture(0)

    while True:
        ret, image = cap.read()
        if not ret:
            print("Failed to grab frame")
            continue

        results = model(image, conf=0.25)

        for info in results:
            parameters = info.boxes
            for box in parameters:
                x1, y1, x2, y2 = box.xyxy[0].numpy().astype('int')
                confidence = box.conf[0].numpy().astype('float') * 100
                class_detected_number = int(box.cls[0])
                class_detected_name = results[0].names[class_detected_number]

                # Draw the rectangle and text inside the loop
                cv2.rectangle(image, (x1, y1), (x2, y2), (0, 0, 255), 3)
                cvzone.putTextRect(image, f'{class_detected_name} {confidence:.2f}%', 
                                [x1 + 8, y1 - 12], thickness=2, scale=1.5)

        cv2.imshow('frame', image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_detection()
