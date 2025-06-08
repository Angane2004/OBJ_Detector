from ultralytics import YOLO
import cv2
import cvzone
import math

# Load YOLO model
model = YOLO("ppe.pt")

# Define class names
classNames = ['Hardhat', 'Mask', 'NO-Hardhat', 'NO-Mask', 'NO-Safety Vest', 'Person', 'Safety Cone',
              'Safety Vest', 'machinery', 'vehicle']

# Open webcam
cap = cv2.VideoCapture(0)  

while True:
    success, img = cap.read()
    if not success:
        print("Failed to capture video")
        break
    
    results = model(img, stream=True)
    
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cls = int(box.cls[0])
            currentClass = classNames[cls]

            if currentClass in ['NO-Hardhat', 'NO-Safety Vest', 'NO-Mask']:
                    color = (0, 0, 255)  # Red for unsafe
            elif currentClass in ['Hardhat', 'Safety Vest', 'Mask']:
                    color = (0, 255, 0)  # Green for safe
            else:
                    color = (255, 0, 0)  # Blue for other

            cvzone.putTextRect(img, f'{currentClass}', 
                                   (max(0, x1), max(35, y1)), scale=1, thickness=1,
                                   colorB=color, colorT=(255, 255, 255), colorR=color, offset=5)
            cv2.rectangle(img, (x1, y1), (x2, y2), color, 3)

    # Show the output window
    cv2.imshow("YOLO Detection", img)
    
    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
