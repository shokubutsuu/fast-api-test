import requests
import json_numpy
json_numpy.patch()
import numpy as np


def send_log(msg: str):
    url = "http://localhost:8000/log" 
    resp = requests.post(url, json={"text": msg})
    print("Server says:", resp.json())

def sent_act():
    url = "http://localhost:8000/act" 
    resp = requests.post(
        url,
        json={"image": np.zeros((256, 256, 3), dtype=np.uint8), # TODO: replace this with your photo!
              "instruction": "do something"})
    print("Server says:", resp.json())

if __name__ == "__main__":
    send_log("Hello SSH!")
