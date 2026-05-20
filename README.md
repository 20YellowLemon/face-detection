# 📷 Real-Time Face Detection using OpenCV

> A lightweight Python script that uses your device's camera and OpenCV's Haar Cascade Classifier to detect and highlight human faces in real time.

---

## 📚 Table of Contents

1. [Project Overview](#1-project-overview)
2. [Features](#2-features)
3. [Prerequisites & Dependencies](#3-prerequisities--dependencies)
4. [Project Structure](#4-project-structure)
5. [License](#5-license)

---

## 1. Project Overview

This script performs **real-time face detection** by reading a live video stream from a connected camera, analyzing each frame using a pre-trained Machine Learning classifier, and drawing a bounding rectangle around every detected face — all in a single continuous loop.

---

## 2. Features

- ✅ Real-time camera face detection at native camera frame rate.
- ✅ Zero model training required — uses OpenCV's bundled pre-trained classifier.
- ✅ Green bounding rectangle drawn around every detected face.
- ✅ Clean camera and window resource release on exit.
- ✅ Minimal codebase — easy to read, modify, and extend.

---

## 3. Prerequisities & Dependencies

### Python Version

Python **3.7 or higher** is required.

### Installation

```bash
pip install opencv-python
```

For environments where GUI windows are not needed (headless servers), install the headless variant instead:

```bash
pip install opencv-python-headless
```

---

## 4. Project Structure

```
face-detection/
│
├── face-detection.py       ← Main script (entry point)
└── README.md               ← This documentation file
```

No additional files, datasets, or model downloads are required. The Haar Cascade XML file is loaded directly from OpenCV's installation directly at runtime.

---

## 5. License

This project is released for educational use. OpenCV is distributed under the **Apache 2.0 License**. The bundled Haar Cascade XML files are part of the OpenCV project and subject to the same license.