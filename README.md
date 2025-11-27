# VisionGuard-YOLOv8 🚨  
### 5G Smart Camera Surveillance System  

Smart Real-Time Human & Object Detection with Email Alerts 📩

This project uses the YOLOv8 model to detect **humans, animals, and objects** in real-time through a webcam feed.  
If a **human is detected**, the system automatically **captures an image** and **sends an email alert** with the image attached — ideal for **smart surveillance applications**.

---

## ✨ Features
- Real-time detection using YOLOv8
- Detects humans, animals & multiple object categories
- Email alert with captured image on human detection
- Anti-spam cooldown to avoid alert spamming
- User-friendly webcam detection interface

---

## 🧠 Tech Stack
- **Python**
- **YOLOv8 (Ultralytics)**
- **OpenCV**
- **Yagmail** (Email automation)
- **Threading**

---
---

## 📦 Installation

```bash
git clone https://github.com/<your-username>/VisionGuard-YOLOv8.git
cd VisionGuard-YOLOv8
pip install ultralytics opencv-python yagmail
---

## 🔐 Configure Email Alerts

Edit these lines inside the Python script:

```python
sender_email = "your-email@gmail.com"
app_password = "your-app-password"
receiver_email = "receiver@gmail.com"

```
---

## ▶ Run the Project

```bash
python object_detection.py

---

## 👨‍💻 Author Information  
- **Name:** Sunny Das  
- **Branch:** Electronics & Communication Engineering  
- **Institute:** NERIST, India

