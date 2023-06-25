# QR-Code Reader

This is a Python application that uses PyQt5, OpenCV, and PyZbar to scan QR codes from a webcam feed or an uploaded image file. Scanned QR code data is displayed in the application window and can be copied to the clipboard.

## Installation

1. Clone this repository
3. Navigate to the cloned project
4. Install the necessary dependencies
   ```pip install pyqt5 opencv-python pyzbar pyperclip```

## Usage

Run the application with:
  ```python qr-code-reader.py```

In the application:

1. Click "Use Webcam" to start the webcam and begin scanning for QR codes.
   - Close the webcam window by pressing "q".
2. Click "Upload Image" to choose an image file from your system and scan it for QR codes.
3. Click "Copy Data" to copy the scanned QR code data to the clipboard.
