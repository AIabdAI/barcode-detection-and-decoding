
# 📦 Barcode Detection and Decoding

This project demonstrates a complete pipeline for detecting and decoding **EAN-13 barcodes** from images using traditional **digital image processing techniques**. The system is built using **OpenCV** and **NumPy**, and provides reliable barcode extraction and decoding in controlled scenarios.

## 📌 Project Overview

The goal of this project is to locate barcode regions within images and decode the numerical information they contain. It uses morphological operations, contour analysis, and a custom decoding algorithm to read EAN-13 barcodes without relying on external libraries or machine learning models.

## 🎯 Objectives

- Detect the location of the barcode in images.
- Extract and analyze the barcode region for accurate decoding.
- Decode the barcode and validate the extracted data using EAN-13 checksum.

## 🧠 Technologies & Skills Used

- **Python**
- **OpenCV** – for image preprocessing, edge detection, and contour analysis.
- **NumPy** – for numerical operations and pattern analysis.
- **Digital Image Processing** – including thresholding, erosion, morphological gradients.
- **Barcode Standards** – implementing the EAN-13 encoding and checksum validation manually.

## 🔍 How it Works

### 1. Barcode Detection (`detect.py`)

- **Preprocessing**
  - Resize input image while maintaining aspect ratio.
  - Convert to grayscale and apply thresholding.
  - Use **erosion** to simplify the image and highlight barcode regions.
  
- **Edge Detection & Contour Analysis**
  - Apply **morphological gradient** to highlight barcode edges.
  - Use `cv2.findContours()` to extract potential barcode structures.
  
- **Candidate Filtering**
  - Use `cv2.minAreaRect()` to evaluate bounding boxes.
  - Filter based on barcode width to exclude invalid detections.
  - Avoid overlapping detections by maintaining a tracking list.

### 2. Barcode Decoding (`decode.py`)

- **Preprocessing**
  - Apply **Otsu’s thresholding** to the extracted region.
  - Perform horizontal line scans to detect stripe patterns.
  
- **Decoding Algorithm**
  - Divide the barcode into left, center, and right patterns.
  - Convert stripe widths into binary digits based on EAN-13 rules.
  - Detect parity pattern to determine the first digit.
  
- **Validation**
  - Calculate **EAN-13 checksum** using a weighted sum.
  - Compare computed checksum with last digit for validation.

## 🚧 Challenges & Future Improvements

- Lighting conditions and noise can reduce detection accuracy.
- Tilted or distorted barcodes are harder to detect and decode.
- The system can be enhanced by:
  - Incorporating **machine learning** or deep learning models.
  - Adding geometric correction and distortion handling.
  - Improving preprocessing for low-quality images.

## ✅ Conclusion

This project illustrates how traditional computer vision techniques can be used effectively for barcode recognition. By relying solely on OpenCV and NumPy, it demonstrates a low-dependency and efficient solution suitable for learning and prototyping purposes. With enhancements, this system can serve as a base for more robust industrial applications.
