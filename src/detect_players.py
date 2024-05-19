from ultralytics import YOLO
import shutil

# Use custom trained model and predict results
model = YOLO("yolov8n.pt")

# Define the location of the database
source = "/workdir/tests/data/"
output = "/workdir/results/"

# Configure the prediction
resultsDetect = model.predict(source, conf=0.5, stream=True, show=False, save=True)

# Creates bounding boxes
for result in resultsDetect:
    boxes = result.boxes
    masks = result.masks
    keypoints = result.keypoints
    probs = result.probs
    output_path = result.save_dir + "/" + result.path.split("/")[-1]
    if "person" in result.verbose():
        shutil.copy(output_path, output)
