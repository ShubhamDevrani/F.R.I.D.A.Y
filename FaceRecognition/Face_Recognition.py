import cv2
import pyautogui

def Face_Recognition():
    try:
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read('FaceRecognition/Data/Trainer/Trainer.yml')
    except cv2.error:
        print("Error: Could not load trained model. Check 'Trainer.yml' path.")
        return

    cascadePath = "FaceRecognition/Data/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)

    font = cv2.FONT_HERSHEY_SIMPLEX
    names = ["Unknown", "Harsh", "Master SPSG"]  

    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    if not cam.isOpened():
        print("Error: Could not open camera.")
        return

    cam.set(3, 640)
    cam.set(4, 480)

    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)

    while True:
        ret, img = cam.read()
        if not ret:
            #print("Failed to capture image.")
            break

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(int(minW), int(minH)))

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            id, confidence = recognizer.predict(gray[y:y+h, x:x+w])
            accuracy = 100 - round(confidence)  

            if accuracy < 40:
                id_name = "Unknown"
            else:
                id_name = names[id] if id < len(names) else "Unknown"

            accuracy_text = f"{accuracy}%"
            cv2.putText(img, str(id_name), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
            cv2.putText(img, accuracy_text, (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

            if id_name == "Master SPSG":
                print("Master SPSG detected. Exiting......")
                cam.release()
                cv2.destroyAllWindows()
                pyautogui.press('esc')  # Exit the program immediately

        cv2.imshow('Face Recognition', img)

        k = cv2.waitKey(10) & 0xFF
        if k == 27:  # ESC key to break
            break

    print("Verification Complete.")
    cam.release()
    cv2.destroyAllWindows()

# Face_Recognition()
