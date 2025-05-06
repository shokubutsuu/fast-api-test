from fastapi import FastAPI
from pydantic import BaseModel
import datetime
import numpy as np
import json_numpy
app = FastAPI()

class LogEntry(BaseModel):
    text: str


@app.post("/log")
async def log(entry: LogEntry):
    print(f"[{datetime.datetime.now()}] {entry.text}")
    return {"response": f"{entry.text}  ✅ received"}


@app.post("/act")
async def act(payload: Dict[str, Any]):
    print(f"[{datetime.datetime.now()}] {payload["instruction"]}")
    return {"action": f"{payload["instruction"]}  ✅ received"}