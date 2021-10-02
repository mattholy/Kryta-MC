# -*- encoding: utf-8 -*-
'''
main.py
----
Kryta_MC is a docker image for Minecraft with a web-based management system.


@Time    :   2021/10/02 23:31:40
@Author  :   Mattholy
@Version :   1.0
@Contact :   smile.used@hotmail.com
@License :   MIT License
'''
import os
import uvicorn
from fastapi import FastAPI
from fastapi import status as http_code
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

# 准备一些环境变量
URL_PREFIX = os.environ.get('KRYTA_URL_PREFIX','_')

# 初始化App
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 开始路由
@app.get("/", response_class=HTMLResponse, status_code=http_code.HTTP_303_SEE_OTHER)
async def gate():
    return RedirectResponse(app.url_path_for('auth'))

@app.get("/" + URL_PREFIX + "/auth", response_class=HTMLResponse)
async def auth():
    return 'qewr'

@app.get("/" + URL_PREFIX + "/dashboard", response_class=HTMLResponse)
async def dashboard():
    return '123'

@app.post("/" + URL_PREFIX + "/register")
async def user_register():
    '''qwwwwwwwwww'''
    return {}

@app.post("/" + URL_PREFIX + "/api/{user}/{resource}")
async def user_api(user: str, resource:str, operation:dict = ''):
    '''qwwwwwwwwww'''
    return {"item_id": user, "q": resource}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)