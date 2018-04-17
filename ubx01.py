# 784632ee-e66f-4f6f-ab1b-e9c9c0d47cf8:US
# https://api-01.ubx.ibmmarketingcloud.com/v1/endpoint
# https://api-01.ubx.ibmmarketingcloud.com/v1/application

import requests

# Register ADP Endpoint to consume data from ACP-Saas
auth_param = '784632ee-e66f-4f6f-ab1b-e9c9c0d47cf8:US'
ubx_url = 'https://api-01.ubx.ibmmarketingcloud.com/v1/endpoint'
head = {"Authorization": "Bearer "+auth_param,
        "Content-type": "application/json"}
payload = '{"providerName": "IBM", "name": "ADP PoC", "description": "ADP Consuming ACP Saas Data","endpointTypes": {"event": {"destination": {"enabled": true, "destinationType": "pull"}}}, "url": ""}'
response = requests.put(ubx_url, headers=head, data=payload)
print(response)
print(response.text)
