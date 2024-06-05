import RPi.GPIO as GPIO
import time
import numpy as np
import torch
from ultralytics import YOLO
import cv2

# Setup GPIO pins
RED_LED_PIN = 17
GREEN_LED_PIN = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_LED_PIN, GPIO.OUT)
GPIO.setup(GREEN_LED_PIN, GPIO.OUT)
# LEDs control
def set_led(color):
    if color == "red":
        GPIO.output(RED_LED_PIN, GPIO.HIGH)
        GPIO.output(GREEN_LED_PIN, GPIO.LOW)
    elif color == "green":
        GPIO.output(RED_LED_PIN, GPIO.LOW)
        GPIO.output(GREEN_LED_PIN, GPIO.HIGH)
# Load the YOLO model
model = YOLO("yolov8n.pt")
# Open the camera
cap = cv2.VideoCapture(0)
# Main loop
try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        # get results
        results = model(frame)
        # Check the results (this assumes the model returns a specific label for inedible mushrooms)
        if results:
            # Replace with the actual condition to identify inedible mushrooms
            for result in results:
                if result['class'] == 'inedible':
                    print("Inedible")
                    set_led("red")
                else:
                    print("Edible")
                    set_led("green")
        # Display frame 
        cv2.imshow("Img", frame)
        key = cv2.waitKey(1)
        if key == 27:  # ESC key to break
            break
        # Wait for a while before the next capture
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
finally:
    cap.release()
    cv2.destroyAllWindows()
    GPIO.cleanup()
