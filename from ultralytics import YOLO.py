from ultralytics import YOLO
import cv2
import time
import yagmail
import threading

# ------------------------------
# 📨 Email Setup
# ------------------------------
sender_email = "sunny.784161@gmail.com"
app_password = "gszx ssfy fjyg txbo" # 🔐 Use your Gmail App Password
receiver_email = "sunny.784161@gmail.com"

yag = yagmail.SMTP(user=sender_email, password=app_password)

def send_email_with_image(image_path):
    subject = "🚨 Human Detected!"
    body = "A human has been detected by the 5G smart camera system."
    try:
        yag.send(to=receiver_email, subject=subject, contents=body, attachments=image_path)
        print("📧 Email sent successfully!")
    except Exception as e:
        print("❌ Failed to send email:", e)

# ------------------------------
# 🔍 YOLO + Webcam Setup
# ------------------------------
print("🔄 Starting camera...")

model = YOLO("yolov8n.pt")  # Load YOLOv8 Nano model

# Define animal classes
animal_classes = {'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'bird'}

# Open webcam or RTSP
cap = cv2.VideoCapture("0")  # Change to RTSP link if needed

if not cap.isOpened():
    print("❌ Cannot access camera stream")
    exit()

print("✅ Camera stream accessed. Beginning detection...")

last_alert_time = 0  # Cooldown tracker, the timer stops your mail from spamming 

while True:
    ret, frame = cap.read()
    if not ret:
        print("⚠ Failed to capture frame")
        continue

    results = model(frame)[0]  # YOLOv8 inference

    # Initialize counters
    human_count = 0
    animal_count = 0
    object_count = 0

    for box, cls_id, conf in zip(results.boxes.xyxy, results.boxes.cls, results.boxes.conf):
        class_name = model.names[int(cls_id)]

        if class_name == 'person':
            tag = "HUMAN"
            color = (0, 0, 255)
            human_count += 1

            current_time = time.time()
            if current_time - last_alert_time > 10:  # Cooldown check
                image_path = f"detected_human_{int(current_time)}.jpg"
                cv2.imwrite(image_path, frame)

                # 📧 Send email in background
                threading.Thread(target=send_email_with_image, args=(image_path,)).start()

                last_alert_time = current_time

        elif class_name in animal_classes:
            tag = "ANIMAL"
            color = (0, 255, 0)
            animal_count += 1

        else:
            tag = "OBJECT"
            color = (255, 255, 0)
            object_count += 1

        # Draw bounding box
        x1, y1, x2, y2 = map(int, box)
        label = f"{tag} ({class_name})"
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        cv2.putText(frame, label, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

        print(f"[{time.strftime('%H:%M:%S')}] {label} - Confidence: {conf:.2f}")

    # Overlay counts on frame
    cv2.putText(frame, f"Humans: {human_count}  Animals: {animal_count}  Objects: {object_count}",
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.imshow("Webcam Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()

