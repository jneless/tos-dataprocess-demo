# reference: https://www.volcengine.com/docs/6349/1157336

import json
import os
import tos
from tos.enum import TierType
from tos.models2 import RestoreJobParameters

# 从环境变量获取 AK 和 SK 信息。
ak = os.getenv('TOS_ACCESS_KEY')
sk = os.getenv('TOS_SECRET_KEY')
# 填写 Bucket 所在区域对应的 Endpoint。如果以华北2(北京)为例，则 your endpoint 填写为 tos-cn-beijing.volces.com，your region 填写为 cn-beijing。
endpoint = "tos-cn-beijing.volces.com"
region = "cn-beijing"
bucket_name = "test-cluster-beijing"
image_key = "demofiles/pics/1.png"
style = "image/info"

try:
    # 创建 TosClientV2 对象，对桶和对象的操作都通过 TosClientV2 实现。
    client = tos.TosClientV2(ak, sk, endpoint, region)
    object_stream = client.get_object(bucket=bucket_name, key=image_key, process=style)
    image_info = json.load(object_stream)
    print(image_info)
except tos.exceptions.TosClientError as e:
    # 操作失败，捕获客户端异常，一般情况为非法请求参数或网络异常。
    print('fail with client error, message:{}, cause: {}'.format(e.message, e.cause))
except tos.exceptions.TosServerError as e:
    # 操作失败，捕获服务端异常，可从返回信息中获取详细错误信息。
    print('fail with server error, code: {}'.format(e.code))
    # request id 可定位具体问题，强烈建议日志中保存。
    print('error with request id: {}'.format(e.request_id))
    print('error with message: {}'.format(e.message))
    print('error with http code: {}'.format(e.status_code))
    print('error with ec: {}'.format(e.ec))
    print('error with request url: {}'.format(e.request_url))
except Exception as e:
    print('fail with unknown error: {}'.format(e))