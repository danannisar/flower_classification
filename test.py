import requests

# For Local Deployment
#url = 'http://localhost:3000/2015-03-31/functions/function/invocations'

# For Cloud Deployment using AWS Lambda
url = 'https://h2lpfof2pc.execute-api.us-east-1.amazonaws.com/test/predict'

data = {'url': 'https://www.thespruce.com/thmb/V9sZh_5_x4UwS1BRGmo3TjH7n-c=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/daisy-types-for-gardens-1316051-04-e0f4e84f081d452885752e84bc7886ed.jpg'}

result = requests.post(url, json = data).json()

print(result)
