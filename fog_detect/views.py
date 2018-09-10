from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import requests
import re
from django.views.decorators.cache import cache_page
from django.core.cache import cache


def index(request):
    """
    定位采用ip定位，api用的和风天气
     天气api采用和风天气
    """

    wea_now = weather_now(request)
    air_qos_now = air_qos(request)
    wea_fore_3 = wea_fore(request)
    life_style = get_life_point(request)

    context = {}
    context.update(wea_now)
    context.update(air_qos_now)
    context.update(wea_fore_3)
    context.update(life_style)

    return render(request, 'fog_detect/index.html', context)


def get_loc_wea(request):
    """处理表单内容"""
    city = request.GET["city"]

    wea_now = weather_now(request, city=city)
    air_qos_now = air_qos(request, city=city)
    wea_fore_3 = wea_fore(request, city=city)
    life_style = get_life_point(request, city=city)

    context_loc_wea = {}
    context_loc_wea.update(wea_now)
    context_loc_wea.update(air_qos_now)
    context_loc_wea.update(wea_fore_3)
    context_loc_wea.update(life_style)
    cache.set("context_loc_wea", context_loc_wea, 1200)
    return render(request, 'fog_detect/index.html', context_loc_wea)


def get_loc_ajax(request):
    """获取当前地理位置，定位到市区"""
    url = "https://search.heweather.com/find?mode=match&key=33ab95c2e813480db5f6cba100d6e53a&location=" + request.GET['location']
    location_resp = requests.get(url).json()
    loc1 = re.findall(".*?location': '(.*?)'", str(location_resp))
    loca = {
        "location": loc1,

        "status_code": re.findall(".*?status': '(.*?)'", str(location_resp))
    }
    cache.set("location", loca, 1200)
    return JsonResponse(loca)


def weather_now(request, **kwargs):
    """获取实时天气"""
    if not kwargs:
        weather_resp = requests.get(
            "https://free-api.heweather.com/s6/weather/now?location=auto_ip&key=33ab95c2e813480db5f6cba100d6e53a").json()
    else:
        weather_resp = requests.get("https://free-api.heweather.com/s6/weather/now?key=33ab95c2e813480db5f6cba100d6e53a&location="+kwargs["city"]).json()

    cond_code = weather_resp["HeWeather6"][0]["now"]["cond_code"]
    context_now = {
        "loc": weather_resp["HeWeather6"][0]["update"]["loc"],   # 更新时间
        "fl": weather_resp["HeWeather6"][0]["now"]["fl"],       # 体感温度
        "tmp": weather_resp["HeWeather6"][0]["now"]["tmp"],     # 温度
        "hum": weather_resp["HeWeather6"][0]["now"]["hum"],     # 湿度
        "vis": weather_resp["HeWeather6"][0]["now"]["vis"],     # 能见度
        "cloud": weather_resp["HeWeather6"][0]["now"]["cloud"],     # 云量
        "cond_code": '/static/images/cond-icon-heweather/' + cond_code + '.png',        # 天气代码
        "cond_txt": weather_resp["HeWeather6"][0]["now"]["cond_txt"],       # 天气描述
        "wind_dir": weather_resp["HeWeather6"][0]["now"]["wind_dir"],       # 风向
        "wind_sc": weather_resp["HeWeather6"][0]["now"]["wind_sc"],     # 风力
        "location": weather_resp["HeWeather6"][0]["basic"]["location"],
        "admin_area": weather_resp["HeWeather6"][0]["basic"]["admin_area"],
        "cnty": weather_resp["HeWeather6"][0]["basic"]["cnty"],
    }
    cache.set("context_now", context_now, 1200)
    return context_now


def air_qos(request, **kwargs):
    """获取实时空气质量"""
    if not kwargs:
        aqos_now_resp = requests.get(
            "https://free-api.heweather.com/s6/air/now?location=auto_ip&key=33ab95c2e813480db5f6cba100d6e53a").json()
    else:
        aqos_now_resp = requests.get("https://free-api.heweather.com/s6/air/now?key=33ab95c2e813480db5f6cba100d6e53a&location="+kwargs["city"]).json()

    if aqos_now_resp["HeWeather6"][0]["status"] != "ok":
        context_air_qos = {
            "pub_time": "无",
            "aqi": "无",
            "main": "无",  # 主要污染物
            "qlty": "良",
            "pm10": "无",
            "pm25": "无",
            "no2": "无",
            "so2": "无",
            "co": "无",
        }
        cache.set("context_air_qos", context_air_qos, 1200)
        return context_air_qos
    else:
        context_air_qos = {
            "pub_time": aqos_now_resp["HeWeather6"][0]["air_now_city"]["pub_time"],
            "aqi": aqos_now_resp["HeWeather6"][0]["air_now_city"]["aqi"],
            "main": aqos_now_resp["HeWeather6"][0]["air_now_city"]["main"],   # 主要污染物
            "qlty": aqos_now_resp["HeWeather6"][0]["air_now_city"]["qlty"],
            "pm10": aqos_now_resp["HeWeather6"][0]["air_now_city"]["pm10"],
            "pm25": aqos_now_resp["HeWeather6"][0]["air_now_city"]["pm25"],
            "no2": aqos_now_resp["HeWeather6"][0]["air_now_city"]["pm25"],
            "so2": aqos_now_resp["HeWeather6"][0]["air_now_city"]["pm25"],
            "co": aqos_now_resp["HeWeather6"][0]["air_now_city"]["pm25"],

        }
        cache.set("context_air_qos", context_air_qos, 1200)
        return context_air_qos


def wea_fore(request, **kwargs):
    """获取未来三天的天气预报"""
    if not kwargs:
        fore_3 = requests.\
            get("https://free-api.heweather.com/s6/weather/forecast?location=auto_ip&key=33ab95c2e813480db5f6cba100d6e53a")\
            .json()
    else:
        fore_3 = requests.get("https://free-api.heweather.com/s6/weather/forecast?key=33ab95c2e813480db5f6cba100d6e53a&location="+kwargs["city"]).json()

    context_wea_fore = {
        "update": fore_3["HeWeather6"][0]["update"]["loc"],
    }
    context_1 = {
        "date1": fore_3["HeWeather6"][0]["daily_forecast"][0]["date"],
        "tmp_max1": fore_3["HeWeather6"][0]["daily_forecast"][0]["tmp_max"],
        "tmp_min1": fore_3["HeWeather6"][0]["daily_forecast"][0]["tmp_min"],
        "hum1": fore_3["HeWeather6"][0]["daily_forecast"][0]["hum"],
        "pop1": fore_3["HeWeather6"][0]["daily_forecast"][0]["pop"],
        "uv_index1": fore_3["HeWeather6"][0]["daily_forecast"][0]["uv_index"],
        "vis1": fore_3["HeWeather6"][0]["daily_forecast"][0]["vis"],
        "cont_txt_d1": fore_3["HeWeather6"][0]["daily_forecast"][0]["cond_txt_d"],
        "cond_txt_n1": fore_3["HeWeather6"][0]["daily_forecast"][0]["cond_txt_n"],
        "wind_sc1": fore_3["HeWeather6"][0]["daily_forecast"][0]["wind_sc"],
        "wind_dir1": fore_3["HeWeather6"][0]["daily_forecast"][0]["wind_dir"],

    }

    context_2 = {
        "date2": fore_3["HeWeather6"][0]["daily_forecast"][1]["date"],
        "tmp_max2": fore_3["HeWeather6"][0]["daily_forecast"][1]["tmp_max"],
        "tmp_min2": fore_3["HeWeather6"][0]["daily_forecast"][1]["tmp_min"],
        "hum2": fore_3["HeWeather6"][0]["daily_forecast"][1]["hum"],
        "pop2": fore_3["HeWeather6"][0]["daily_forecast"][1]["pop"],
        "uv_index2": fore_3["HeWeather6"][0]["daily_forecast"][1]["uv_index"],
        "vis2": fore_3["HeWeather6"][0]["daily_forecast"][1]["vis"],
        "cont_txt_d2": fore_3["HeWeather6"][0]["daily_forecast"][1]["cond_txt_d"],
        "cond_txt_n2": fore_3["HeWeather6"][0]["daily_forecast"][1]["cond_txt_n"],
        "wind_sc2": fore_3["HeWeather6"][0]["daily_forecast"][1]["wind_sc"],
        "wind_dir2": fore_3["HeWeather6"][0]["daily_forecast"][0]["wind_dir"],
    }
    context_3 = {
        "date3": fore_3["HeWeather6"][0]["daily_forecast"][2]["date"],
        "tmp_max3": fore_3["HeWeather6"][0]["daily_forecast"][2]["tmp_max"],
        "tmp_min3": fore_3["HeWeather6"][0]["daily_forecast"][2]["tmp_min"],
        "hum3": fore_3["HeWeather6"][0]["daily_forecast"][2]["hum"],
        "pop3": fore_3["HeWeather6"][0]["daily_forecast"][2]["pop"],
        "uv_index3": fore_3["HeWeather6"][0]["daily_forecast"][2]["uv_index"],
        "vis3": fore_3["HeWeather6"][0]["daily_forecast"][2]["vis"],
        "cont_txt_d3": fore_3["HeWeather6"][0]["daily_forecast"][2]["cond_txt_d"],
        "cond_txt_n3": fore_3["HeWeather6"][0]["daily_forecast"][2]["cond_txt_n"],
        "wind_sc3": fore_3["HeWeather6"][0]["daily_forecast"][2]["wind_sc"],
        "wind_dir3": fore_3["HeWeather6"][0]["daily_forecast"][0]["wind_dir"],
    }

    context_wea_fore.update(context_1)
    context_wea_fore.update(context_2)
    context_wea_fore.update(context_3)
    cache.set("context_wea_fore", context_wea_fore, 1200)
    return context_wea_fore


@cache_page(1200)
def get_tmp_hum(request):
    """获取温度，湿度的24小时数据"""
    city = request.GET["location"]
    if not city:
        r = str(requests.get(
            "https://free-api.heweather.com/s6/weather/hourly?location=auto_ip&key=33ab95c2e813480db5f6cba100d6e53a")\
            .json())
    else:
        r = str(requests.get("https://free-api.heweather.com/s6/weather/hourly?key=33ab95c2e813480db5f6cba100d6e53a&location="+city).json())

    regx_tmp = ".*?tmp': '(\d+?)'"
    regx_hum = ".*?hum': '(\d+?)'"
    regx_time = ".*?time': '.*?\s(.*?)'"

    tmp_24 = re.findall(regx_tmp, r)
    hum_24 = re.findall(regx_hum, r)
    time_24 = re.findall(regx_time, r)

    tmp_24 = [int(item) for item in tmp_24][:8]
    hum_24 = [int(item) for item in hum_24][:8]
    time_24 = time_24[:8]

    context = {
        "tmp_24": tmp_24,
        "hum_24": hum_24,
        "time_24": time_24
    }
    return JsonResponse(context)


def get_life_point(request, **kwargs):
    if not kwargs:
        life_resp = str(requests.get(
            "https://free-api.heweather.com/s6/weather/lifestyle?location=auto_ip&key=33ab95c2e813480db5f6cba100d6e53a").json())
    else:
        life_resp = str(requests.get("https://free-api.heweather.com/s6/weather/lifestyle?key=33ab95c2e813480db5f6cba100d6e53a&location="+kwargs["city"]).json())

    reg_drsg = ".*?txt': '(.*?)'"
    res = re.findall(reg_drsg, life_resp)
    context_life_p = {
        "dsg": res[1],
        "flu": res[2],
        "sports": res[3],
        "air": res[7]
    }
    cache.set("context_life_p", context_life_p, 1200)
    return context_life_p


# @cache_page(120)
# def redis_cache(request):
#     result = get_wea_now.delay()
#     print(result.id)
#     return HttpResponse("你好")