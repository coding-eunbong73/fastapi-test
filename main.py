from typing import Union
from service import KSPComm
from fastapi import FastAPI, Response

app =  FastAPI()

@app.get("/")
async def read_root(username, password):
    KSPComm.login()
