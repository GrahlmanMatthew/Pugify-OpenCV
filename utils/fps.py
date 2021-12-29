import cv2, time

def calculate_display_fps(ptime, frame, videoWidth, videoHeight):
    ctime = time.time()
    fps = (1 / (ctime - ptime))
    show_fps(frame, fps, videoWidth, videoHeight)
    return ctime
    
def show_fps(frame, fps, videoWidth, videoHeight):
    cv2.putText(frame, f'FPS:{int(fps)}', (videoWidth-125, videoHeight - (videoHeight-35)), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    