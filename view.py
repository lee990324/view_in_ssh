import cv2

# Create a VideoCapture object to read the video
cap = cv2.VideoCapture('/home/bcml1/WBC-Counting/data/20240827_LCH2_LDC_crop.mp4')

# Check if the video opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Loop to read and display each frame of the video
while cap.isOpened():
    # Read a frame from the video
    ret, frame = cap.read()

    # If the frame was read successfully, display it
    if ret:
        cv2.imshow('Video', frame)

        # Wait for 25ms before moving to the next frame.
        # This will create a video effect at 40 FPS (1000ms / 25ms = 40 FPS)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            # Press 'q' to exit the video
            break
    else:
        # Break the loop if no more frames are available
        break

# Release the VideoCapture object and close the display window
cap.release()
cv2.destroyAllWindows()