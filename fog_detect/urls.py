from django.urls import path
from . import views

app_name = 'fog_detect'
urlpatterns = [
    path('', views.index, name='index'),
    path('get_loc_ajax/', views.get_loc_ajax, name="get_loc_ajax"),
    path('get_loc_wea/', views.get_loc_wea, name="get_loc_wea"),
    path('get_tmp_hum/', views.get_tmp_hum, name="get_tmp_hum"),
    path('rush/', views.index, name="rush"),
    # path('redis_cache/', views.redis_cache, name='redis_cache')  # celery异步测试失败，先搁置。
]