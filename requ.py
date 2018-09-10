import requests
import json
import re

# 定位到城市
# r = requests.get('https://api.map.baidu.com/location/ip?ak=Bid8SdiD5e0GcoBGS6ZM7wFcwIItQgpZ&coor=BD09ll')

# 获取天气信息  33ab95c2e813480db5f6cba100d6e53a
# r = requests.get("https://free-api.heweather.com/s6/weather/hourly?location=auto_ip&key=33ab95c2e813480db5f6cba100d6e53a").json()
# print(type(r))

life_resp = requests.get(
        "https://free-api.heweather.com/s6/weather/lifestyle?location=auto_ip&key=33ab95c2e813480db5f6cba100d6e53a").json()
print(life_resp)


