# VisionGuard-YOLOv8 🚨  
### 5G Smart Camera Surveillance System  

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-green.svg)](https://docs.ultralytics.com)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-red.svg)
![Status](https://img.shields.io/badge/Project-Active-brightgreen.svg)

Smart Real-Time Human & Object Detection with Email Alerts 📩  

This project uses the YOLOv8 model to detect **humans, animals, and objects** in real-time through a webcam feed.  
If a **human is detected**, the system automatically **captures an image** and **sends an email alert** with the image attached — ideal for **smart surveillance applications**.

---

## 📸 Sample Output

> Add your screenshots into a folder like `images/` and update the file names below.

![Human, Animal & Object Detection](images/detection_human_animal_object.jpg)
![Multiple Humans & Objects](images/detection_multiple_humans_objects.jpg)

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

## 📦 Installation


```bash
git clone https://github.com/<your-username>/VisionGuard-YOLOv8.git
cd VisionGuard-YOLOv8
pip install -r requirements.txt

---

## 🔐 Configure Email Alerts

Edit these lines inside the Python script:

```python
sender_email = "your-email@gmail.com"
app_password = "your-app-password"
receiver_email = "receiver@gmail.com"
````
---

## ▶ Run the Project

```bash
python object_detection.py


## 2️⃣ `requirements.txt` (create this file in your repo)

Create a new file called **`requirements.txt`** in your project folder and paste:

```txt
ultralytics
opencv-python
yagmail

pip install -r requirements.txt
