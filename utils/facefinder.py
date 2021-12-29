import cv2

class FaceFinder:
    def __init__(self, image):
        self.image = image
        self.gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        
    def get_image(self):    
        return self.image
        
    def get_faces(self):
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        faces = face_cascade.detectMultiScale(self.gray_image, 1.2, 20)
        return faces