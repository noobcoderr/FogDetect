# from __future__ import absolute_import
# import time
# import requests
# from celery import task
# from django.views.decorators.cache import cache_page
# from django.core.cache import cache
#
#
# @task
# def get_wea_now():
#     weather_resp = requests.get(
#         "https://free-api.heweather.com/s6/weather/now?key=33ab95c2e813480db5f6cba100d6e53a&location=" + "西安").json()
#     cond_code = weather_resp["HeWeather6"][0]["now"]["cond_code"]
#     return cond_code

