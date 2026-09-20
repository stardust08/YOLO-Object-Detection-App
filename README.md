<div align="center">

# 🎯 YOLO Object Detection App

**Real-time object detection for images and video, in your browser.**

Upload a photo or a clip, pick a model, and get annotated results back — powered by
[Ultralytics YOLO11](https://docs.ultralytics.com/models/yolo11/) behind an async
[FastAPI](https://fastapi.tiangolo.com/) backend.

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Async%20Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![YOLO11](https://img.shields.io/badge/YOLO11-Detection-00C853?style=for-the-badge&logo=yolo&logoColor=white)](https://docs.ultralytics.com/models/yolo11/)
[![OpenCV](https://img.shields.io/badge/OpenCV-Streaming-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](#-license)

</div>

---

## ✨ Features

| | Feature | Details |
|:--:|:--|:--|
| 🖼️ | **Image detection** | Drag & drop a `.jpg` / `.jpeg` / `.png`, get an annotated JPEG back |
| 🎬 | **Video streaming** | Upload `.mp4` / `.avi` / `.mov` and watch frames annotated live over MJPEG |
| ⚡ | **Three model tiers** | Trade speed for accuracy — Nano, Small, or Medium |
| 🧠 | **Preloaded weights** | All models load once at startup, so requests never wait on disk |
| 🌙 | **Dark-mode UI** | Clean, responsive single-page frontend — no build step, no framework |
| 🔄 | **Reset anytime** | Swap files and re-run detection without reloading the page |

---

## 🚀 Quickstart

### 1. Clone

```bash
git clone https://github.com/stardust08/YOLO-Object-Detection-App.git
cd YOLO-Object-Detection-App
```

### 2. Create a virtual environment

Python **3.11** is recommended — Ultralytics and Torch ship prebuilt wheels for it.

```bash
python3.11 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Check the model weights

The three YOLO11 checkpoints are already tracked in `models/`. If any are missing,
grab them from the [Ultralytics model zoo](https://docs.ultralytics.com/models/) and
drop them in:

```
models/yolo11n.pt    models/yolo11s.pt    models/yolo11m.pt
```

### 5. Run

```bash
uvicorn app.main:app --reload
```

Open **<http://127.0.0.1:8000>** — interactive API docs live at **`/docs`**.

> [!TIP]
> Port already in use? Pass `--port 8001`. Every frontend URL is relative, so nothing else needs changing.

---

## 🧩 Models

| UI option | `model_type` | Weights | Best for |
|:--|:--:|:--|:--|
| **Fast** | `n` | `yolo11n.pt` | Live video, low-power machines |
| **Balanced** | `s` | `yolo11s.pt` | Everyday use — the UI default |
| **Accurate** | `m` | `yolo11m.pt` | Stills where precision matters |

---

## 🔌 API

| Method | Endpoint | Returns |
|:--|:--|:--|
| `GET` | `/` | The web UI |
| `POST` | `/detect/?model_type=n\|s\|m` | Annotated JPEG (image) or `{"stream_url": …}` (video) |
| `GET` | `/video_stream/{uid}?model_type=…` | MJPEG stream of annotated frames |
| `GET` | `/docs` | Swagger UI |

**Example**

```bash
curl -X POST "http://127.0.0.1:8000/detect/?model_type=s" \
     -F "file=@street.jpg" \
     --output detected.jpg
```

---

## 📂 Project Structure

```
YOLO-Object-Detection-App/
├── app/                      # FastAPI backend
│   ├── main.py               # Routes: /, /detect/, /video_stream/{uid}
│   ├── model_loader.py       # Loads the three YOLO11 checkpoints at startup
│   ├── image_processor.py    # bytes → OpenCV → YOLO → annotated JPEG
│   └── stream_processor.py   # Temp-file registry + MJPEG frame generator
├── static/
│   ├── script.js             # Upload, preview, detection calls
│   └── style.css             # Dark-mode styling
├── templates/
│   └── index.html            # Single-page UI
├── models/                   # YOLO11 weights
│   ├── yolo11n.pt
│   ├── yolo11s.pt
│   └── yolo11m.pt
├── requirements.txt
├── Procfile
└── README.md
```

---

## 🛠️ Tech Stack

<table>
<tr><td><b>Backend</b></td><td>FastAPI · Uvicorn · Starlette</td></tr>
<tr><td><b>Detection</b></td><td>Ultralytics YOLO11 · PyTorch</td></tr>
<tr><td><b>Imaging</b></td><td>OpenCV · NumPy</td></tr>
<tr><td><b>Frontend</b></td><td>Vanilla JS · HTML · CSS · Font Awesome</td></tr>
<tr><td><b>Templating</b></td><td>Jinja2</td></tr>
</table>

---

---
