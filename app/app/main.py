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
from fastapi.responses import HTMLResponse, RedirectResponse, PlainTextResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

# 自定义的一些玩意儿
if __name__ == "__main__":
    os.chdir('./app')
from APIs import api, setup

# 准备一些环境
URL_PREFIX = "/" + os.environ.get('KRYTA_URL_PREFIX','')

# 定义App
app = FastAPI(root_path = URL_PREFIX)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api.router)
app.include_router(setup.router)

description = """
## Features
- Auto generate openapi json
- Swagger UI & ReDoc UI
"""
app.openapi()["info"] = {
    "title": "Kryta-MC",
    "version": "Version 0.0 - Yangtez",
    "description": description,
    "contact": {
        "name": "Mattholy",
        "url": "https://github.com/mattholy",
        "email": "realmattholy@outlook.com",
    },
    "license": {
        "name": "MIT License",
        "url": "https://github.com/mattholy/Kryta-MC/blob/storyline/LICENSE",
    },
    "x-logo": {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
}

# 启动
@app.on_event("startup")
def startup_event():
    print("啊我开始了")

# 开始路由
app.mount("/setup/static", StaticFiles(directory=os.path.join(".","app","html","setup")), name="setup")
app.mount("/dashboard/static", StaticFiles(directory=os.path.join(".","app","html","dashboard")), name="dashboard")

@app.get("/", response_class=FileResponse, status_code=http_code.HTTP_200_OK, tags=['Pages'])
async def main():
    return FileResponse('./app/html/setup/index.html')

# 终止
@app.on_event("shutdown")
def shutdown_event():
    print("啊我被关闭了222")



if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True, debug=True, workers=4)