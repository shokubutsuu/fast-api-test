from fastapi import FastAPI
from pydantic import BaseModel
import datetime

app = FastAPI()

class LogEntry(BaseModel):
    text: str

@app.post("/log")
async def log(entry: LogEntry):
    # 打到远程机终端，方便确认
    print(f"[{datetime.datetime.now()}] {entry.text}")
    # 回传给客户端
    return {"response": f"{entry.text}  ✅ received"}
