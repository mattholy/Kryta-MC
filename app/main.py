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

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}