import cv2
import tensorflow as tf
import numpy as np
 
face_detector = cv2.CascadeClassifier("utils/haar_face.xml")
 
smile_detector = tf.keras.models.load_model("model/best_model.keras")
 
cap = cv2.VideoCapture(0)
 
while True:
    # Capture a frame from the camera
    ret, frame = cap.read()
 
    # Detect faces in the frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
 
    # Loop through the detected faces
    for (x, y, w, h) in faces:
        # Extract the face region
        face_roi = frame[y:y+h, x:x+w]
 
        # Preprocess the face for the smile detection model
        face_roi = cv2.resize(face_roi, (64, 64))
        face_roi = face_roi / 255.0
        face_roi = np.expand_dims(face_roi, axis=0)
 
        # Use the smile detection model to predict if the face is smiling
        smile_prediction = smile_detector.predict(face_roi)[0][0]
 
        # Draw a rectangle around the face and display the smile prediction
        if smile_prediction > 0.5:
            color = (0, 255, 0)  # Green
            label = f"Smiling ({smile_prediction:.2f})"
        else:
            color = (0, 0, 255)  # Red
            label = f"Not Smiling ({smile_prediction:.2f})"
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
        cv2.putText(frame, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
 
    # Display the resulting frame
    cv2.imshow('Smile Detection', frame)
 
    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
