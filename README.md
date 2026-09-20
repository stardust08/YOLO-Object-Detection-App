# YOLO Object Detection App

![Made with FastAPI](https://img.shields.io/badge/FastAPI-Async%20Web%20Framework-009688?logo=fastapi&logoColor=white)
![YOLO](https://img.shields.io/badge/YOLO-Object%20Detection-green?logo=openai)

A modern web application for real-time object detection in images and videos using powerful **YOLO models**. Built with a **FastAPI** backend and a dynamic **JavaScript** frontend.



---

## Features

-  Real-time object detection (YOLO11)
-  Upload image or video easily (drag & drop)
-  Choose model type: Fast / Balanced / Accurate
-  Smart streaming for video results
-  Dark mode styled UI
-  Reset and upload new file anytime

---

## Getting Started

1. **Clone this repo**
   ```bash
   git clone https://github.com/Raafat-Nagy/YOLO-Object-Detection-App.git
   cd YOLO-Object-Detection-App

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Download YOLO models**
   Put your models (e.g. `yolo11n.pt`) in the `models/` directory.
   Get them from:
   [Ultralytics Official Models](https://docs.ultralytics.com/models)

4. **Run the app**

   ```bash
   uvicorn app.main:app --reload
   ```

5. Open `http://127.0.0.1:8000` in your browser.

---

## Project Structure

```
YOLO-Object-Detection-App/
├── app/                # FastAPI backend
│   ├── image_processor.py
│   ├── main.py
│   ├── model_loader.py
│   └── stream_processor.py
├── static/             # Frontend JS/CSS
│   ├── script.js
│   └── style.css
├── templates/          # HTML template
│   └── index.html
├── models/             # YOLO .pt models
│   ├── yolo11m
│   ├── yolo11n
│   └── yolo11s
├── requirements.txt
└── README.md
```

---

## Tech Stack

* **FastAPI** – lightweight Python backend
* **Ultralytics YOLO** – object detection engine
* **JavaScript + HTML + CSS** – frontend
* **Font Awesome** – icons

---

## License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).

---

## Contact

Feel free to reach out or contribute via pull request or issue!

---
