from __future__ import annotations
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import time

class ResponseOK(BaseModel):
    ok: bool = True
    result: list


class ResponseError(BaseModel):
    ok: bool = False
    error_code: int
    description: str


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_model=ResponseOK | ResponseError)
def get_tds_ec():
    put_header = {"Content-Type": "application/json"}
    ec = requests.get("https://fra1.blynk.cloud/external/api/get?token=SoOALwl0VxKPXMzEXCGLVs0RrGYv2GbX&v5", put_header)
    tds = requests.get("https://fra1.blynk.cloud/external/api/get?token=SoOALwl0VxKPXMzEXCGLVs0RrGYv2GbX&v6", put_header)
    ec = ec.json()
    tds = tds.json()
    print(ec['v5'])
    print(tds['v6'])
    time.sleep(5)
    result = [ec['v5'],tds['v6']]
    return {"ok": True, "result": result}