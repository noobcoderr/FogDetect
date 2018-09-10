from django.db import models

# Create your models here.


class NowLoc(models.Model):
    location = models.CharField(max_length=20)
    admin_area = models.CharField(max_length=20)
    cnty = models.CharField(max_length=20)


class Weather(models.Model):
    """实况天气详情、空气质量详情、24小时温、湿度变化(不保存)、未来三天天气预报(不保存)。"""
    tmp = models.IntegerField()
    hum = models.IntegerField()
    wind_dir = models.CharField(max_length=10)
    wind_sc = models.IntegerField()
    cond_code = models.IntegerField()
    cond_txt = models.CharField(max_length=10)

    aqi = models.IntegerField()
    qlty = models.CharField(max_length=10)
    pm_10 = models.IntegerField()
    pm_25 = models.IntegerField()
    no_2 = models.IntegerField()
    so_2 = models.IntegerField()
    co = models.IntegerField()

    dsg = models.CharField(max_length=50)
    flu = models.CharField(max_length=50)
    sports = models.CharField(max_length=50)
    air = models.CharField(max_length=50)

    now_city = models.OneToOneField(NowLoc, on_delete=models.DO_NOTHING)

    # tmp_24 = models.IntegerField()
    # hum_24 = models.IntegerField()

# class Wea_3(models.Model):
#     date1 = models.DateTimeField()
#     tmp_max1 = models.IntegerField()
#     tmp_min1 = models.IntegerField()
#     pop1 = models.IntegerField()
#     cont_txt_d1 = models.CharField(max_length=20)
#     cond_txt_n1 = models.CharField(max_length=20)
#     wind_dir1 = models.CharField(max_length=20)
#     wind_sc1 = models.IntegerField()
#
#     date2 = models.DateTimeField()
#     tmp_max2 = models.IntegerField()
#     tmp_min2 = models.IntegerField()
#     pop2 = models.IntegerField()
#     cont_txt_d2 = models.CharField(max_length=20)
#     cond_txt_n2 = models.CharField(max_length=20)
#     wind_dir2 = models.CharField(max_length=20)
#     wind_sc2 = models.IntegerField()
#
#     date3 = models.DateTimeField()
#     tmp_max3 = models.IntegerField()
#     tmp_min3 = models.IntegerField()
#     pop3 = models.IntegerField()
#     cont_txt_d3 = models.CharField(max_length=20)
#     cond_txt_n3 = models.CharField(max_length=20)
#     wind_dir3 = models.CharField(max_length=20)
#     wind_sc3 = models.IntegerField()
