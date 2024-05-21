import cv2

vid_capture = cv2.VideoCapture("/workdir/results/frame_%d.jpg")
frame_width = int(vid_capture.get(3))
frame_height = int(vid_capture.get(4))
frame_size = (frame_width,frame_height)
fps = 20
output = cv2.VideoWriter('/workdir/output_video_from_file.mp4', cv2.VideoWriter_fourcc(*'XVID'), 20, frame_size)
while(vid_capture.isOpened()):
    ret, frame = vid_capture.read()
    if ret == True:# Write the frame to the output files
            output.write(frame)
    else:
        print("Stream disconnected")
        break
vid_capture.release()
output.release()
