# -*- encoding: utf-8 -*-
'''
setup.py
----
Kryta系统激活


@Time    :   2021/10/03 10:17:05
@Author  :   Mattholy
@Version :   1.0
@Contact :   smile.used@hotmail.com
@License :   MIT License
'''
import os
import uuid
import requests
import json
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from utils.data_format_defines import StandardResponse
from utils.rsa import RsaController

# 准备一些环境变量
URL_PREFIX = os.environ.get('KRYTA_URL_PREFIX','::')
HUB_URL = 'http://127.0.0.1:3080'

router = APIRouter()
citizen = RsaController()

@router.post("/setup/begin", tags=["APIs"], response_model=StandardResponse)
async def setup_begin():
    '''开始进行激活'''
    return {
        'status':True,
        'msg':'ok',
        'data':{}
    }

@router.post("/setup/eula", tags=["APIs"], response_model=StandardResponse)
async def eula():
    '''用户同意EULA'''
    server_id = str(uuid.uuid4())
    data = {
        "data":citizen.encrypt_data(json.dumps(
            {"server_id":server_id}
        ))
    }
    hub_response = requests.post(
        url=HUB_URL + "/kryta/api/orion/accept_eula",
        headers={'Content-Type': 'application/json'},
        data=json.dumps(data)
    )
    print(hub_response.text)
    return {
        'status':True,
        'msg':'ok',
        'data':{
            'server_id':server_id
        }
    }

@router.post("/setup/code", tags=["APIs"], response_class=JSONResponse)
async def activation(code:str):
    '''激活整个Kryta系统'''
    return {"access_token":'this is a token', "token_type": "bearer"}

@router.post("/setup/admin_sign_up", tags=["APIs"], response_class=JSONResponse)
async def admin_register(username:str,password:str,re_password:str):
    '''注册Kryta Server的管理员'''
    return {"access_token":'this is a token', "token_type": "bearer"}