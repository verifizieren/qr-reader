import sys
import cv2
from PyQt5 import QtWidgets, QtCore, QtGui
from pyzbar.pyzbar import decode
import pyperclip

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QR Code Scanner")
        main_layout = QtWidgets.QVBoxLayout()
        self.image_label, self.text_field = QtWidgets.QLabel(), QtWidgets.QTextEdit()
        main_layout.addWidget(self.image_label)

        # Buttons for interacting with the application
        self.webcam_button = QtWidgets.QPushButton("Use Webcam")
        self.webcam_button.clicked.connect(self.use_webcam)
        main_layout.addWidget(self.webcam_button)

        self.upload_button = QtWidgets.QPushButton("Upload Image")
        self.upload_button.clicked.connect(self.upload_image)
        main_layout.addWidget(self.upload_button)

        main_layout.addWidget(self.text_field)

        # Button to copy QR data
        self.copy_button = QtWidgets.QPushButton("Copy Data")
        self.copy_button.clicked.connect(self.copy_data)
        main_layout.addWidget(self.copy_button)

        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def use_webcam(self):
        cap = cv2.VideoCapture(0)
        while True:
            _, frame = cap.read()
            cv2.imshow('Webcam - Press "q" to exit', frame)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            data = self.scan_qr_code(gray)
            if data: self.text_field.setText(data)
            if cv2.waitKey(1) & 0xFF == ord('q'): break
        cap.release()
        cv2.destroyAllWindows()

    def upload_image(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', filter="Images (*.png *.xpm *.jpg)")
        if fname[0]:
            img = cv2.imread(fname[0])
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            data = self.scan_qr_code(gray)
            if data: self.text_field.setText(data)

    # Function to scan QR code
    def scan_qr_code(self, img):
        qr_codes = decode(img)
        for qr in qr_codes: return qr.data.decode('utf-8')
        return None

    # Function to copy data
    def copy_data(self):
        pyperclip.copy(self.text_field.toPlainText())

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()