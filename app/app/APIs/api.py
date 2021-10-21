# -*- encoding: utf-8 -*-
'''
api.py
----
提供api


@Time    :   2021/10/03 10:17:05
@Author  :   Mattholy
@Version :   1.0
@Contact :   smile.used@hotmail.com
@License :   MIT License
'''
import os
from sys import prefix
from fastapi import FastAPI, APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse


# 准备一些环境变量
URL_PREFIX = os.environ.get('KRYTA_URL_PREFIX','::')

app = FastAPI()
router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth")

@router.post("/api/{resource_category}/{resource_name}", tags=["APIs"])
async def api(
    resource_category: str,
    resource_name:str,
    operation:dict = '',
    token: str = Depends(oauth2_scheme)
    ):
    '''Kryta主要逻辑'''
    return {}
