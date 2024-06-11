from flask import Flask, Response
import cv2
import imutils
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.resnet50 import preprocess_input

app = Flask(__name__)

# Constants
THRESHOLD = 0.1369336
NEW_WIDTH = 64
NEW_HEIGHT = 64

# Load models
DETECTOR = cv2.CascadeClassifier("haar_face.xml")
MODEL = load_model("model/best_model.keras")

# Auxiliary functions
def predict_smile_or_not(x):
    return 'Smile' if x >= THRESHOLD else 'Not Smile'

def generate_frame(stream):
    while True:
        grabbed, frame = stream.read()
        if not grabbed:
            break

        frame = imutils.resize(frame, width=700)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        rects = DETECTOR.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

        for (x, y, w, h) in rects:
            roi_gray = gray[y:y + h, x:x + w]
            
            # Chuyển đổi ROI thành ảnh có 3 kênh màu BGR
            roi_bgr = cv2.cvtColor(roi_gray, cv2.COLOR_GRAY2BGR)
            roi_bgr = cv2.resize(roi_bgr, (NEW_WIDTH, NEW_HEIGHT))
            roi_bgr = roi_bgr / 255.0
            roi_bgr = np.expand_dims(roi_bgr, axis=0)  # Thêm chiều batch

            prediction = MODEL.predict(roi_bgr)[0][0]
            label = predict_smile_or_not(prediction)
            
            color = (0, 255, 0) if label == 'Smile' else (0, 0, 255)
            cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# Main route
@app.route('/')
def video_feed():
    stream = cv2.VideoCapture("http://192.168.43.186:8000")
    return Response(generate_frame(stream), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)
