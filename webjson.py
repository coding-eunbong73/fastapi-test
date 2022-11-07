from typing import Union

from fastapi import FastAPI, Response

app =  FastAPI()

@app.get("/")
async def read_root():
   ret_str = """{
   "deploy_type": "cluster",
   "status": "processing",
  "step_status" : "pre_setting\\nabc"
    }"""
   return Response(content=ret_str, media_type="application/json")