import cv2, time
from utils.pugify import pugify_face
from utils.facefinder import FaceFinder
from utils.fps import calculate_display_fps

ptime = 0
videoCapture = cv2.VideoCapture(0)
videoWidth, videoHeight = int(videoCapture.get(3)), int(videoCapture.get(4))

while True:
    res, frame = videoCapture.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)     # add alpha channel
    ptime = calculate_display_fps(ptime, frame, videoWidth, videoHeight)

    ff = FaceFinder(frame)
    faces = ff.get_faces()
    for (x, y, w, h) in faces:
        pugify_face(x, y, w, h, frame)
    
    window_name = 'Pugify - Q to Quit' 
    cv2.imshow(window_name, frame)
    cv2.setWindowProperty(window_name, cv2.WND_PROP_TOPMOST, 1)
    if cv2.waitKey(1) == ord('q'): break

videoCapture.release()
cv2.destroyAllWindows()
