import os, cv2

PUG_IMAGE_PATH = os.path.join(os.getcwd(), "resources", "puggo.png")
PUG_IMAGE = cv2.imread(PUG_IMAGE_PATH, -1)
PUG_IMAGE = cv2.cvtColor(PUG_IMAGE, cv2.COLOR_BGR2BGRA)

def pugify_face(x, y, w, h, frame):
        RESIZE_PUG_IMAGE = cv2.resize(PUG_IMAGE, (w, h))
        alpha_s = RESIZE_PUG_IMAGE[:, :, 3] / 255.0
        alpha_l = 1.0 - alpha_s
        for c in range(0, 3):
            frame[y:y+h, x:x+w, c] = (alpha_s * RESIZE_PUG_IMAGE[:, :, c] + alpha_l * frame[y:y+h, x:x+w, c])
    