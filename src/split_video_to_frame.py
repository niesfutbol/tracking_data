import cv2

# Open the video file
source = "/workdir/tests/"
video_path = f"{source}fut_sal_nies.mp4"
cap = cv2.VideoCapture(video_path)
count = 0
while cap.isOpened():
    success, frame = cap.read()
    if success:
        path = f"/workdir/tests/data/frame_{count}.jpg"
        cv2.imwrite(path, frame)
        count += 1
    else:
        break