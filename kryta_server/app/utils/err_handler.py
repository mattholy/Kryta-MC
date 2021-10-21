# -*- encoding: utf-8 -*-
'''
err_handler.py
----
define some error handler


@Time    :   2021/10/03 18:11:45
@Author  :   Mattholy
@Version :   1.0
@Contact :   smile.used@hotmail.com
@License :   MIT License
'''
from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi import status as http_code
from fastapi.encoders import jsonable_encoder

app = FastAPI()

@app.exception_handler(RequestValidationError)
async def http_422_handler(request:Request,exc:RequestValidationError) -> JSONResponse:
    '''
    重写FastAPI默认的422错误
    '''
    return JSONResponse(
        status_code = http_code.HTTP_422_UNPROCESSABLE_ENTITY,
        content = {"msg":jsonable_encoder(exc.errors())}
    )