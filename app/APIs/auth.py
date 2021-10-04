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

# 准备一些环境变量
URL_PREFIX = os.environ.get('KRYTA_URL_PREFIX','::')

router = APIRouter()

@router.post("/auth", tags=["APIs"])
async def user_auth(username:str,password:str):
    '''qwwwwwwwwww'''
    return {"access_token": 'this is a token', "token_type": "bearer"}

@router.post("/signup", tags=["APIs"])
async def signup(username:str,password:str):
    '''qwwwwwwwwww'''
    return {"access_token":'this is a token', "token_type": "bearer"}