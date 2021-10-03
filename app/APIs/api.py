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
from fastapi import APIRouter
# 准备一些环境变量
URL_PREFIX = os.environ.get('KRYTA_URL_PREFIX','::')

router = APIRouter()

@router.post("/" + URL_PREFIX + "/api/{some_thing}/{resource}", tags=["APIs"])
async def api(some_thing: str, resource:str, operation:dict = ''):
    '''qwwwwwwwwww'''
    return {"item_id": some_thing, "q": resource}
