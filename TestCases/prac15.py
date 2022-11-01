import sys
import requests
import json
url = "http://test.com"
payload_plan = open('RSA_TW_CP_rlovr_without_Addon.json', 'r')
json_payload_plan = json.loads(payload_plan.read())
response_plan = requests.post(url,json=json_payload_plan,)
json_response_plan = response_plan.json()
print(response_plan.status_code)
print(json_response_plan)
try:
    assert 1 == 1
except Exception as e:
    json_data = json_payload_plan
    sys.stdout = open("RSA_TW_CP_plan_rlovr_without_Addon.log", "w")
    print(
        "empty response - No quotes have been generated, please verify the below inputs")
    print(json.dumps(json_data, indent=2))
    raise e