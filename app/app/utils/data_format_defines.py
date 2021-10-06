# -*- encoding: utf-8 -*-
'''
data_format_defines.py
----
定义一些数据交互的格式


@Time    :   2021/10/03 19:37:27
@Author  :   Mattholy
@Version :   1.0
@Contact :   smile.used@hotmail.com
@License :   MIT License
'''

from typing import List, Optional
from pydantic import BaseModel


class api_reponse(BaseModel):
    status: str
    detail: Optional[dict] = {}
    mgs: str

api_request_operation_example = {
    "operation":"download",
    "detail":[
        {
            "server_name":"minecraft",
            "edition":"java",
            "verion":"1.16.0"
        },{
            "server_name":"minecraft",
            "edition":"bedrock",
            "verion":"1.10.0"
        }
    ]
}

api_responses_example = {
    "status":"processing",
    "detail":{
        "job_id":"123-456-789",
        "time":"2021-09-28 12:12:23"
    },
    "msg":"ok"
}