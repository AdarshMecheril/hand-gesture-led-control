import cv2 as cv
import mediapipe as mp
import time
import serial

# Initialize serial communication with ESP32 (adjust port and baud rate)
ser = serial.Serial('COM5', 9600)  # Change 'COM5' to your actual serial port

time.sleep(2.0)

mp_draw = mp.solutions.drawing_utils
mp_hand = mp.solutions.hands

tipIds = [4, 8, 12, 16, 20]

video = cv.VideoCapture(0)

if not video.isOpened():
    print("Error: Camera not detected or failed to open.")
    exit()

with mp_hand.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while True:
        ret, image = video.read()

        if not ret:
            print("Error: Failed to read frame from camera.")
            break

        image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        results = hands.process(image_rgb)

        lmList = []
        if results.multi_hand_landmarks:
            for hand_landmark in results.multi_hand_landmarks:
                myHands = results.multi_hand_landmarks[0]
                for id, lm in enumerate(myHands.landmark):
                    h, w, c = image.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lmList.append([id, cx, cy])
                mp_draw.draw_landmarks(image, hand_landmark, mp_hand.HAND_CONNECTIONS)

        fingers = []
        if len(lmList) != 0:
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            total = fingers.count(1)

            # Send the number of fingers detected to ESP32
            ser.write(str(total).encode())

            cv.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv.FILLED)
            cv.putText(image, str(total), (45, 375), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)

        cv.imshow("Frame", image)
        k = cv.waitKey(1)
        if k == ord('q'):
            break

video.release()
cv.destroyAllWindows()
ser.close()
