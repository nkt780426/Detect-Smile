import os
import cv2

# Constants
THRESHOLD = 0.2921139
NEW_WIDTH = 64
NEW_HEIGHT = 64

# Constants
IMAGE_FOLDER = "model/testset"
OUTPUT_FOLDER = "model/testset-gray"
DETECTOR = cv2.CascadeClassifier("haar_face.xml")

# Initialize count
count = 1

# Function to preprocess image
def preprocess_image(image):
    global count  # Ensure count is modified globally
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    rects = DETECTOR.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
    
    for (x, y, w, h) in rects:
        roi_gray = gray[y:y + h, x:x + w]
        output_path = os.path.join(OUTPUT_FOLDER, f"{count}.jpg")
        cv2.imwrite(output_path, roi_gray)
        count += 1
    
# Create output folder if it does not exist
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

# Process each image in the input folder
for filename in os.listdir(IMAGE_FOLDER):
    # Read image
    image_path = os.path.join(IMAGE_FOLDER, filename)
    image = cv2.imread(image_path)
    
    # Preprocess image
    preprocess_image(image)
    
print("Preprocessing complete.")
