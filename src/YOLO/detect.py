from ultralytics import YOLO
import cv2

# Load model
model = YOLO("yolov8n.pt")

# Run detection
results = model("traffic.jpg")

# Get image with boxes
img = results[0].plot()

# Save output
cv2.imwrite("output.jpg", img)

print("✅ Output saved as output.jpg")