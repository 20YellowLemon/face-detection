# Step 1: Installing OpenCV Library
# pip install opencv-python

# Step 2: Importing OpenCV and Haar Cascade Classifier
import cv2
def main():
 face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Step 3: Open Camera and Check for Camera Access
 cap = cv2.VideoCapture(0)
 if not cap.isOpened():
  print("Error. Please check your camera.")
  exit()

# Step 4: Capture Frames, Convert to Grayscale and Detect Faces
 while True:
  ret, frame = cap.read()
  if not ret:
    print("Failed to capture/read frame.")
    break
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Step 5: Draw Rectangles Around Detected Faces and Display the Frame:
  for (x, y, w, h) in faces:
   cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
  cv2.imshow('Face Detection', frame)

# Step 6: Exit the Program
  if cv2.waitKey(1) & 0xFF == ord('q'):
   break

# Step 7: Release the Camera and Cloase All Windows
 cap.release()
 cv2.destroyAllWindows()

if __name__ == "__main__":
 main()
