import cv2
from deepface import DeepFace
import time

duration = 5

# Start time
start_time = time.time()

# Initialize the video capture object
video_capture = cv2.VideoCapture(
    0
)  # Set the argument to the appropriate camera index if you have multiple cameras

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Display the captured frame
    cv2.imshow("Video", frame)

    result = DeepFace.analyze(
        img_path=frame,
        actions=["age", "gender", "race", "emotion"],
        enforce_detection=False,
    )

    # Perform facial expression analysis

    # Break the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord("q") or (time.time() - start_time) > duration:
        break

    # Access the facial expression result

    # Print the emotion scores


# Release the video capture object and close the windows
video_capture.release()
cv2.destroyAllWindows()
dd = result[0]
age = list(dd.values())[0]
gender = list(dd.values())[3]
race = list(dd.values())[5]
emotion = list(dd.values())[7]
print(f"your age is :{age}")
print(f"your gender is :{gender}")
print(f"your race is :{race}")
print(f"your are :{emotion}")
