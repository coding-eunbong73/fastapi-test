from typing import Union

from fastapi import FastAPI, Response

app =  FastAPI()

@app.get("/")
async def read_root():
   ret_str = """{
   "deploy_type": "cluster",
   "status": "processing",
  "step_status" : [
     { "pre_setting": {
             "start_time": "2020/09/20, 13:44:30"
             "duration": 30
           }
     }
     ]
    }"""
   return Response(content=ret_str, media_type="application/json")