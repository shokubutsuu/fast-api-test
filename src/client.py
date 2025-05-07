import requests
import json_numpy
json_numpy.patch()
import numpy as np
import time
#pip install opencv-python
import cv2
import matplotlib.pyplot as plt

hz=20
interval = 1/hz

def send_log(msg: str):
    url = "http://localhost:8000/log" 
    resp = requests.post(url, json={"text": msg})
    print("Server says:", resp.json())

def send_act(image: np.array, instruction: str):
    url = "http://localhost:8000/act" 
    resp = requests.post(
        url,
        json={"image": np.zeros((256, 256, 3), dtype=np.uint8), # TODO: replace this with your photo!
              "instruction": "do something",
              "unnorm_key":"roboturk"})
    print("Server says:", resp.json())

def crop_center_square(image):
    h, w = image.shape[:2]
    min_dim = min(h,w)
    start_x = w//2 - min_dim//2
    start_y = h//2 - min_dim//2
    return image[start_y: start_y+min_dim, start_x: start_x + min_dim]

def capture_and_process_image():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise RuntimeError("Cannot open camera")
    
    ret, frame = cap.read()
    cap.release()
    if not ret:
        raise RuntimeError("failed to capture image")
    
    frame = crop_center_square(frame)
    frame_resized = cv2.resize(frame,(256,256))
    return frame_resized

if __name__ == "__main__":
    instruction = "do something"
    img = capture_and_process_image()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.imwrite("img.jpg", img)
    cv2.imwrite("img_rgb.jpg", img_rgb)
    send_act(img_rgb, instruction)
    time.sleep(interval)
    print("sleep end")
    # while(True):
        
        

