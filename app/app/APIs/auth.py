# -*- encoding: utf-8 -*-
'''
auth.py
----
提供用户登录注册与鉴权


@Time    :   2021/10/03 10:17:05
@Author  :   Mattholy
@Version :   1.0
@Contact :   smile.used@hotmail.com
@License :   MIT License
'''
import os
from fastapi import APIRouter
from fastapi.responses import JSONResponse

# 准备一些环境变量
URL_PREFIX = os.environ.get('KRYTA_URL_PREFIX','::')

router = APIRouter()

@router.post("/auth/login", tags=["APIs"], response_class=JSONResponse)
async def user_auth(username:str,password:str):
    '''qwwwwwwwwww'''
    return {"access_token": 'this is a token', "token_type": "bearer"}

@router.post("/auth/signup", tags=["APIs"], response_class=JSONResponse)
async def signup(username:str,password:str):
    '''qwwwwwwwwww'''
    return {"access_token":'this is a token', "token_type": "bearer"}

@router.post("/setup/eula", tags=["APIs"], response_class=JSONResponse)
async def eula():
    '''用户同意EULA'''
    pass

@router.post("/setup/code", tags=["APIs"], response_class=JSONResponse)
async def activation(code:str):
    '''激活整个Kryta系统'''
    return {"access_token":'this is a token', "token_type": "bearer"}

@router.post("/setup/admin_sign_up", tags=["APIs"], response_class=JSONResponse)
async def admin_register(username:str,password:str,re_password:str):
    '''注册Kryta Server的管理员'''
    return {"access_token":'this is a token', "token_type": "bearer"}