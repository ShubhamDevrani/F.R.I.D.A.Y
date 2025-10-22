import os
import cv2
import numpy as np
from PIL import Image

path = 'FaceRecognition\\Data\\Samples'

recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier("FaceRecognition\\Data\\haarcascade_frontalface_default.xml")

def Images_And_Labels(path):

    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
    faceSamples=[]
    ids = []

    for imagePath in imagePaths:                                # to iterate particular image path

        gray_img = Image.open(imagePath).convert('L')           # convert it to grayscale
        img_arr = np.array(gray_img,'uint8')

        id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = detector.detectMultiScale(img_arr)

        for (x,y,w,h) in faces:
            faceSamples.append(img_arr[y:y+h,x:x+w])
            ids.append(id)

    return faceSamples,ids

print ("Training faces. It will take a few seconds. Wait ...")

faces,ids = Images_And_Labels(path)
recognizer.train(faces, np.array(ids))
recognizer.write('FaceRecognition/DATA/Trainer/Trainer.yml')

print("Model trained, Now we can recognize your face.")
