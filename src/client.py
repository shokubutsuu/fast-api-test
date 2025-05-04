import requests

def send_log(msg: str):
    url = "http://localhost:8000/log"   # 看似本地，实际已转发到远程
    resp = requests.post(url, json={"text": msg})
    print("Server says:", resp.json())

if __name__ == "__main__":
    send_log("Hello SSH!")
