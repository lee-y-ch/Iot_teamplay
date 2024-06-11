import torch
import numpy as np
from ultralytics import YOLO
import cv2
from picamera2 import Picamera2, Preview
from gpiozero import LED
import webbrowser

green_led = LED(17)
red_led = LED(10)

model = YOLO("./best.pt")

picam2 = Picamera2()
preview_config = picam2.create_preview_configuration()
picam2.configure(preview_config)
picam2.start()

# cap = cv2.VideoCapture(0)

pre_mush = ""

while True:
	# ret, frame = cap.read()
	frame = picam2.capture_array()
	
	# Check number of channels
	num_channels = frame.shape[2]
	if num_channels != 3:
		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	
	# if not freak:
	# 	break
	results = model(frame)
	
	### Use result!!!
	if(results and results[0]):
		print("What?")
		scores = np.array(results[0].boxes.conf.cpu())
		classes =  np.array(results[0].boxes.cls.cpu(), dtype="int")
		if(classes.any()):
			cls = classes[0]
			score = scores[0]
		else:
			green_led.off()
			red_led.off()
			continue
		
		mushroom = results[0].names[cls]
		print("This is ", mushroom)
		print("Score is ", score)
		if(pre_mush == mushroom):
			continue
		pre_mush = mushroom
		if(mushroom == "Hypholoma fasciculare"):
			green_led.off()
			red_led.on()
			webbrowser.get("chromium-browser").open("file:///home/pi/Desktop/web-page/page1.html")
			continue
		elif(mushroom == "Galerina marginata"):
			green_led.off()
			red_led.on()
			webbrowser.get("chromium-browser").open("file:///home/pi/Desktop/web-page/page3.html")
			continue
		elif(mushroom == "Amanita virosa"):
			green_led.off()
			red_led.on()
			webbrowser.get("chromium-browser").open("file:///home/pi/Desktop/web-page/page4.html")
			continue
		elif(mushroom == "Apioperdon pyriforme"):
			green_led.on()
			red_led.off()
			webbrowser.get("chromium-browser").open("file:///home/pi/Desktop/web-page/page10.html")
			continue
		elif(mushroom == "Agaricus arvensis"):
			green_led.on()
			red_led.off()
			webbrowser.get("chromium-browser").open("file:///home/pi/Desktop/web-page/page6.html")
			continue
		elif(mushroom == "Hypholoma lateritium"):
			green_led.on()
			red_led.off()
			webbrowser.get("chromium-browser").open("file:///home/pi/Desktop/web-page/page5.html")
			continue
		elif(mushroom == "Sparassis crispa"):
			green_led.on()
			red_led.off()
			webbrowser.get("chromium-browser").open("file:///home/pi/Desktop/web-page/page8.html")
			continue
		elif(mushroom == "Volvariella volvacea"):
			green_led.on()
			red_led.off()
			webbrowser.get("chromium-browser").open("file:///home/pi/Desktop/web-page/page9.html")
			continue
		elif(mushroom == "Oyster mushroom"):
			green_led.on()
			red_led.off()
			webbrowser.get("chromium-browser").open("file:///home/pi/Desktop/web-page/page7.html")
			continue
		elif(mushroom == "Ramaria formosa"):
			green_led.off()
			red_led.on()
			webbrowser.get("chromium-browser").open("file:///home/pi/Desktop/web-page/page2.html")
			continue
	else:
		green_led.off()
		red_led.off()
	
	cv2.imshow("Img", frame)
	key = cv2.waitKey(1)
	if key == 27:
		break
	
picam2.stop()
cv2.destroyAllWindows()
# cap.release()
