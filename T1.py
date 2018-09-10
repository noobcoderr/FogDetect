
import re
import time
import requests
# reg = ".*?tmp': '(\d+?)'"
# res = re.findall(reg, A)
# res = [int(item) for item in res]
# print(res)

# regx_hum = ".*?hum': '(\d+?)'"
# res = re.findall(regx_hum, A)
# res = [int(item) for item in res]
# print(res)

# reg_loc = ".*?location': '(.*?)'.*?admin_area': '(.*?)'.*?cnty': '(.*?)'"
# reg_loc1 = ".*?loc': '(.*?)'"
# reg_cnty = ".*?cnty': '(.*?)'"
# # reg_loc = ".*?location': '(.*?)'"
# # loc = re.findall(".*?loc': '(.*?)'", A)[0]
# # am_a = re.findall(reg_am_a, A)
# # cnty = re.findall(reg_cnty, A)
# # print(loc)
# t1s = time.time()
# A = {"HeWeather6":[{"basic":{"cid":"CN101110101","location":"西安","parent_city":"西安","admin_area":"陕西","cnty":"中国","lat":"34.26316071","lon":"108.94802094","tz":"+8.00"},"update":{"loc":"2018-09-08 08:45","utc":"2018-09-08 00:45"},"status":"ok","now":{"cloud":"0","cond_code":"100","cond_txt":"晴","fl":"19","hum":"62","pcpn":"0.0","pres":"1019","tmp":"20","vis":"28","wind_deg":"339","wind_dir":"西北风","wind_sc":"2","wind_spd":"11"}}]}
# A = str(A)
# context1 = {
#     "tmp": re.findall(".*?tmp': '(.*?)'", A)[0],
#     "loc": re.findall(".*?loc': '(.*?)'", A)[0],
#     "fl": re.findall(".*?fl': '(.*?)'", A)[0],
#     "hum": re.findall(".*?hum': '(.*?)'", A)[0],
#     "wind_dir": re.findall(".*?wind_dir': '(.*?)'", A)[0],
#     "wind_sc": re.findall(".*?wind_sc': '(.*?)'", A)[0],
#     "cond_txt": re.findall(".*?cond_txt': '(.*?)'", A)[0],
#     "cond_code": re.findall(".*?cond_code': '(.*?)'", A)[0],
#
# }
# t1e = time.time()
#
# t2s = time.time()
# B = {"HeWeather6":[{"basic":{"cid":"CN101110101","location":"西安","parent_city":"西安","admin_area":"陕西","cnty":"中国","lat":"34.26316071","lon":"108.94802094","tz":"+8.00"},"update":{"loc":"2018-09-08 08:45","utc":"2018-09-08 00:45"},"status":"ok","now":{"cloud":"0","cond_code":"100","cond_txt":"晴","fl":"19","hum":"62","pcpn":"0.0","pres":"1019","tmp":"20","vis":"28","wind_deg":"339","wind_dir":"西北风","wind_sc":"2","wind_spd":"11"}}]}
#
# context2 = {
#     "loc": B["HeWeather6"][0]["update"]["loc"],  # 更新时间
#     "fl": B["HeWeather6"][0]["now"]["fl"],  # 体感温度
#     "tmp": B["HeWeather6"][0]["now"]["tmp"],  # 温度
#     "hum": B["HeWeather6"][0]["now"]["hum"],  # 湿度
#     "cond_code": B["HeWeather6"][0]["now"]["cond_code"],
#     "cond_txt": B["HeWeather6"][0]["now"]["cond_txt"],  # 天气描述
#     "wind_dir": B["HeWeather6"][0]["now"]["wind_dir"],  # 风向
#     "wind_sc": B["HeWeather6"][0]["now"]["wind_sc"],  # 风力
# }
# t2e = time.time()
#
# print("正则所用时间", t1e-t1s)
# print("索引所用时间", t2e-t2s)

# A = {"HeWeather6":[{"basic":{"cid":"CN101110101","location":"西安","parent_city":"西安","admin_area":"陕西","cnty":"中国","lat":"34.26316071","lon":"108.94802094","tz":"+8.00"},"update":{"loc":"2018-09-08 09:45","utc":"2018-09-08 01:45"},"status":"ok","hourly":[{"cloud":"2","cond_code":"100","cond_txt":"晴","dew":"4","hum":"43","pop":"0","pres":"1016","time":"2018-09-08 13:00","tmp":"25","wind_deg":"35","wind_dir":"东北风","wind_sc":"1-2","wind_spd":"8"},{"cloud":"3","cond_code":"100","cond_txt":"晴","dew":"2","hum":"41","pop":"0","pres":"1013","time":"2018-09-08 16:00","tmp":"26","wind_deg":"15","wind_dir":"东北风","wind_sc":"3-4","wind_spd":"24"},{"cloud":"5","cond_code":"100","cond_txt":"晴","dew":"6","hum":"43","pop":"0","pres":"1014","time":"2018-09-08 19:00","tmp":"22","wind_deg":"62","wind_dir":"东北风","wind_sc":"3-4","wind_spd":"14"},{"cloud":"15","cond_code":"100","cond_txt":"晴","dew":"7","hum":"50","pop":"0","pres":"1015","time":"2018-09-08 22:00","tmp":"19","wind_deg":"88","wind_dir":"东风","wind_sc":"1-2","wind_spd":"4"},{"cloud":"34","cond_code":"101","cond_txt":"多云","dew":"7","hum":"54","pop":"0","pres":"1018","time":"2018-09-09 01:00","tmp":"16","wind_deg":"15","wind_dir":"东北风","wind_sc":"1-2","wind_spd":"7"},{"cloud":"74","cond_code":"101","cond_txt":"多云","dew":"6","hum":"53","pop":"0","pres":"1018","time":"2018-09-09 04:00","tmp":"15","wind_deg":"46","wind_dir":"东北风","wind_sc":"1-2","wind_spd":"9"},{"cloud":"73","cond_code":"101","cond_txt":"多云","dew":"8","hum":"50","pop":"0","pres":"1020","time":"2018-09-09 07:00","tmp":"16","wind_deg":"88","wind_dir":"东风","wind_sc":"1-2","wind_spd":"8"},{"cloud":"80","cond_code":"101","cond_txt":"多云","dew":"8","hum":"46","pop":"0","pres":"1019","time":"2018-09-09 10:00","tmp":"21","wind_deg":"112","wind_dir":"东南风","wind_sc":"1-2","wind_spd":"1"}]}]}
# B = A["HeWeather6"][0]["hourly"][0]["tmp"]
#
# print(B)

# url = "https://search.heweather.com/find?number=7&mode=match&key=33ab95c2e813480db5f6cba100d6e53a&location=" + "怀化"
# location_resp = requests.get(url).json()
# loc1= re.findall(".*?location': '(.*?)'", str(location_resp))
# co = re.findall(".*?status': '(.*?)'", str(location_resp))
# # loca = {
# #     "location": location_resp["HeWeather6"][0]["basic"][0]["location"],
# #     "admin_area": location_resp["HeWeather6"][0]["basic"][0]["location"],
# #     "cnty": location_resp["HeWeather6"][0]["basic"][0]["location"],
# #     "status_code": location_resp["HeWeather6"][0]["status"],
# # }
# print(loc1)
# print(co)


# def foo(x,**kwargs):
#     print(x)
#     if not kwargs:
#         print("没有多余的参数")
#     else:
#         print(type(kwargs["url"]))
#
# foo(1, url="http://xxx.com")

# r = str(requests.get(
#     "https://free-api.heweather.com/s6/weather/hourly?key=33ab95c2e813480db5f6cba100d6e53a&location=西安").json())

r = "{'HeWeather6': [{'basic': {'cid': 'CN101110101', 'location': '西安', 'parent_city': '西安', 'admin_area': '陕西', 'cnty': '中国', 'lat': '34.26316071', 'lon': '108.94802094', 'tz': '+8.00'}, 'update': {'loc': '2018-09-09 15:45', 'utc': '2018-09-09 07:45'}, 'status': 'ok', 'hourly': [{'cloud': '99', 'cond_code': '104', 'cond_txt': '阴', 'dew': '6', 'hum': '52', 'pop': '7', 'pres': '1017', 'time': '2018-09-09 19:00', 'tmp': '25', 'wind_deg': '113', 'wind_dir': '东南风', 'wind_sc': '3-4', 'wind_spd': '15'}, {'cloud': '99', 'cond_code': '104', 'cond_txt': '阴', 'dew': '6', 'hum': '62', 'pop': '7', 'pres': '1018', 'time': '2018-09-09 22:00', 'tmp': '23', 'wind_deg': '151', 'wind_dir': '东南风', 'wind_sc': '3-4', 'wind_spd': '22'}, {'cloud': '99', 'cond_code': '104', 'cond_txt': '阴', 'dew': '6', 'hum': '70', 'pop': '0', 'pres': '1018', 'time': '2018-09-10 01:00', 'tmp': '21', 'wind_deg': '225', 'wind_dir': '西南风', 'wind_sc': '3-4', 'wind_spd': '21'}, {'cloud': '98', 'cond_code': '104', 'cond_txt': '阴', 'dew': '5', 'hum': '71', 'pop': '0', 'pres': '1018', 'time': '2018-09-10 04:00', 'tmp': '19', 'wind_deg': '84', 'wind_dir': '东风', 'wind_sc': '3-4', 'wind_spd': '12'}, {'cloud': '79', 'cond_code': '104', 'cond_txt': '阴', 'dew': '7', 'hum': '58', 'pop': '0', 'pres': '1018', 'time': '2018-09-10 07:00', 'tmp': '19', 'wind_deg': '86', 'wind_dir': '东风', 'wind_sc': '3-4', 'wind_spd': '22'}, {'cloud': '57', 'cond_code': '101', 'cond_txt': '多云', 'dew': '7', 'hum': '58', 'pop': '0', 'pres': '1017', 'time': '2018-09-10 10:00', 'tmp': '21', 'wind_deg': '175', 'wind_dir': '南风', 'wind_sc': '1-2', 'wind_spd': '7'}, {'cloud': '55', 'cond_code': '101', 'cond_txt': '多云', 'dew': '7', 'hum': '67', 'pop': '0', 'pres': '1014', 'time': '2018-09-10 13:00', 'tmp': '24', 'wind_deg': '175', 'wind_dir': '南风', 'wind_sc': '1-2', 'wind_spd': '10'}, {'cloud': '53', 'cond_code': '101', 'cond_txt': '多云', 'dew': '8', 'hum': '68', 'pop': '0', 'pres': '1012', 'time': '2018-09-10 16:00', 'tmp': '29', 'wind_deg': '190', 'wind_dir': '南风', 'wind_sc': '1-2', 'wind_spd': '7'}]}, {'basic': {'cid': 'CN101050311', 'location': '西安', 'parent_city': '牡丹江', 'admin_area': '黑龙江', 'cnty': '中国', 'lat': '44.5810318', 'lon': '129.6131134', 'tz': '+8.00'}, 'update': {'loc': '2018-09-09 15:45', 'utc': '2018-09-09 07:45'}, 'status': 'ok', 'hourly': [{'cloud': '0', 'cond_code': '100', 'cond_txt': '晴', 'dew': '6', 'hum': '70', 'pop': '0', 'pres': '1028', 'time': '2018-09-09 19:00', 'tmp': '11', 'wind_deg': '297', 'wind_dir': '西北风', 'wind_sc': '1-2', 'wind_spd': '9'}, {'cloud': '0', 'cond_code': '100', 'cond_txt': '晴', 'dew': '6', 'hum': '77', 'pop': '0', 'pres': '1029', 'time': '2018-09-09 22:00', 'tmp': '7', 'wind_deg': '82', 'wind_dir': '东风', 'wind_sc': '1-2', 'wind_spd': '7'}, {'cloud': '0', 'cond_code': '100', 'cond_txt': '晴', 'dew': '2', 'hum': '86', 'pop': '0', 'pres': '1028', 'time': '2018-09-10 01:00', 'tmp': '5', 'wind_deg': '41', 'wind_dir': '东北风', 'wind_sc': '1-2', 'wind_spd': '7'}, {'cloud': '34', 'cond_code': '100', 'cond_txt': '晴', 'dew': '2', 'hum': '91', 'pop': '0', 'pres': '1029', 'time': '2018-09-10 04:00', 'tmp': '4', 'wind_deg': '94', 'wind_dir': '东风', 'wind_sc': '1-2', 'wind_spd': '7'}, {'cloud': '18', 'cond_code': '100', 'cond_txt': '晴', 'dew': '6', 'hum': '80', 'pop': '0', 'pres': '1026', 'time': '2018-09-10 07:00', 'tmp': '8', 'wind_deg': '139', 'wind_dir': '东南风', 'wind_sc': '1-2', 'wind_spd': '8'}, {'cloud': '8', 'cond_code': '101', 'cond_txt': '多云', 'dew': '6', 'hum': '50', 'pop': '0', 'pres': '1024', 'time': '2018-09-10 10:00', 'tmp': '16', 'wind_deg': '183', 'wind_dir': '南风', 'wind_sc': '1-2', 'wind_spd': '3'}, {'cloud': '11', 'cond_code': '101', 'cond_txt': '多云', 'dew': '4', 'hum': '45', 'pop': '0', 'pres': '1021', 'time': '2018-09-10 13:00', 'tmp': '21', 'wind_deg': '207', 'wind_dir': '西南风', 'wind_sc': '1-2', 'wind_spd': '3'}, {'cloud': '9', 'cond_code': '101', 'cond_txt': '多云', 'dew': '7', 'hum': '56', 'pop': '0', 'pres': '1020', 'time': '2018-09-10 16:00', 'tmp': '20', 'wind_deg': '236', 'wind_dir': '西南风', 'wind_sc': '1-2', 'wind_spd': '7'}]}, {'basic': {'cid': 'CN101060705', 'location': '西安', 'parent_city': '辽源', 'admin_area': '吉林', 'cnty': '中国', 'lat': '42.92041397', 'lon': '125.15142059', 'tz': '+8.00'}, 'update': {'loc': '2018-09-09 15:45', 'utc': '2018-09-09 07:45'}, 'status': 'ok', 'hourly': [{'cloud': '0', 'cond_code': '100', 'cond_txt': '晴', 'dew': '7', 'hum': '64', 'pop': '0', 'pres': '1025', 'time': '2018-09-09 19:00', 'tmp': '12', 'wind_deg': '82', 'wind_dir': '东风', 'wind_sc': '1-2', 'wind_spd': '6'}, {'cloud': '0', 'cond_code': '100', 'cond_txt': '晴', 'dew': '6', 'hum': '77', 'pop': '0', 'pres': '1025', 'time': '2018-09-09 22:00', 'tmp': '8', 'wind_deg': '99', 'wind_dir': '东风', 'wind_sc': '1-2', 'wind_spd': '9'}, {'cloud': '0', 'cond_code': '100', 'cond_txt': '晴', 'dew': '5', 'hum': '85', 'pop': '0', 'pres': '1026', 'time': '2018-09-10 01:00', 'tmp': '7', 'wind_deg': '151', 'wind_dir': '东南风', 'wind_sc': '1-2', 'wind_spd': '11'}, {'cloud': '0', 'cond_code': '100', 'cond_txt': '晴', 'dew': '5', 'hum': '89', 'pop': '0', 'pres': '1026', 'time': '2018-09-10 04:00', 'tmp': '6', 'wind_deg': '117', 'wind_dir': '东南风', 'wind_sc': '1-2', 'wind_spd': '8'}, {'cloud': '0', 'cond_code': '100', 'cond_txt': '晴', 'dew': '8', 'hum': '75', 'pop': '0', 'pres': '1024', 'time': '2018-09-10 07:00', 'tmp': '11', 'wind_deg': '137', 'wind_dir': '东南风', 'wind_sc': '1-2', 'wind_spd': '5'}, {'cloud': '0', 'cond_code': '100', 'cond_txt': '晴', 'dew': '7', 'hum': '49', 'pop': '0', 'pres': '1023', 'time': '2018-09-10 10:00', 'tmp': '19', 'wind_deg': '177', 'wind_dir': '南风', 'wind_sc': '1-2', 'wind_spd': '2'}, {'cloud': '39', 'cond_code': '100', 'cond_txt': '晴', 'dew': '5', 'hum': '49', 'pop': '0', 'pres': '1020', 'time': '2018-09-10 13:00', 'tmp': '23', 'wind_deg': '204', 'wind_dir': '西南风', 'wind_sc': '1-2', 'wind_spd': '1'}, {'cloud': '19', 'cond_code': '100', 'cond_txt': '晴', 'dew': '10', 'hum': '58', 'pop': '0', 'pres': '1019', 'time': '2018-09-10 16:00', 'tmp': '22', 'wind_deg': '248', 'wind_dir': '西南风', 'wind_sc': '1-2', 'wind_spd': '1'}]}]}"
# regx_tmp = ".*?tmp': '(\d+?)'"
# regx_hum = ".*?hum': '(\d+?)'"
regx_time = ".*?time': '.*?\s(.*?)'"
#
# tmp_24 = re.findall(regx_tmp, r)
# hum_24 = re.findall(regx_hum, r)
time_24 = re.findall(regx_time, r)
#
# tmp_24 = [int(item) for item in tmp_24][:8]
# hum_24 = [int(item) for item in hum_24][:8]
time_24 = time_24[:8]

# context = {
#     "tmp_24": tmp_24,
#     "hum_24": hum_24,
#     "time_24": time_24
# }

# print(context)

print(time_24)