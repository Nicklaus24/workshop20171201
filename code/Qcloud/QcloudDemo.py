from QcloudApi.qcloudapi import QcloudApi
import json

# 定义使用的服务类型
module = 'wenzhi'

# 定义服务接口
action = 'TextSentiment'

# 配置参数
config = {
    # 定义提供服务的地区
    'Region': 'sh',
    # 这里填写从控制台获取的secretId和secretKey
    'secretId': 'Your secretId',
    'secretKey': 'Your secretKey',
    # 请求方式
    'method': 'get'
}

with open('good.txt', 'r', encoding='utf-8') as f:
    goodTxt = f.read()

with open('bad.txt', 'r', encoding='utf-8') as f:
    badTxt = f.read()

# https://cloud.tencent.com/document/product/271/2072
params = {
    'content': goodTxt,
    'type': 1
}

service = QcloudApi(module, config)

# print('Request Url: ')
# print(service.generateUrl(action, params))
# 调用情感分析服务
result = service.call(action, params)
print(json.loads(result))
