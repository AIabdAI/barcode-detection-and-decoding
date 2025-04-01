Barcode Detection and Decoding
1. Introduction
This project aims to detect and decode barcodes in images using digital image processing
techniques. The system analyzes images to extract the barcode region and then deciphers
the encoded data. The implementation is based on OpenCV and NumPy for performing
various image processing tasks.
2. Objectives
 Detect the location of the barcode in images using image processing techniques.
 Extract and analyze the barcode region to improve decoding accuracy.
 Decode the barcode and verify the extracted data.
3. Methodology
3.1 Barcode Detection (detect.py)
 Preprocessing:
 The input image is resized to appropriate dimensions while maintaining aspect ratio.
 The image is converted to grayscale, followed by thresholding to separate the barcode
from the background.
 Erosion (Morphological Operation) is applied to merge small details and transform
the image into uniform color blocks, making the barcode appear as a solid black
rectangle for easier detection.
 Edge Detection and Contour Analysis:
 Morphological Gradient is applied instead of traditional edge detection techniques, as it
helps focus on sharp transitions that define barcode edges.
 Contours are extracted using findContours_morph(), which isolates barcode-related
structures based on the morphological characteristics of the image.
 Barcode Candidate Selection:
 Rectangular bounding boxes around detected contours are analyzed using
cv2.minAreaRect().
 Candidates are filtered based on minimum barcode width, ensuring that only valid EAN-
13 barcodes (width &gt; 95 pixels) are considered.
 A list is maintained to prevent overlapping detections, ensuring that only the correct
barcode is extracted.
3.2 Barcode Decoding (decode.py)
 Preprocessing:

 The extracted barcode region is binarized using Otsu’s thresholding, which helps
eliminate lighting inconsistencies.
 Horizontal scan lines are extracted across the barcode to analyze black and white stripe
patterns.
 Decoding Algorithm:
 The barcode is divided into different sections, including guard bars, left patterns, center
guard, and right patterns.
 The widths of the stripes are analyzed and converted into numerical values based on the
EAN-13 encoding standard.
 Parity patterns are used to determine the first digit of the barcode.
 Barcode Validation:
 The checksum (mod-10) is calculated using weighted values specific to the EAN-13
format.
 The last digit of the barcode is compared to the computed checksum, and if they match,
the barcode is considered valid.
4. Challenges and Recommendations
 Poor lighting conditions or image noise can impact the accuracy of barcode detection
and decoding.
 Tilted or distorted barcodes may be difficult to read without additional correction
methods.
 The system could be further improved by integrating machine learning or advanced
image analysis techniques for better performance.
5. Conclusion
This system provides an efficient method for detecting and decoding barcodes in images
using traditional image processing techniques. The use of erosion plays a crucial role in
converting the barcode region into a solid black rectangle, which improves detection
accuracy. The system performs well with clear images but may require further refinements
when dealing with low-quality images or challenging lighting conditions. Integrating
AI-based models or enhancing preprocessing techniques could further improve the
system’s robustness.
