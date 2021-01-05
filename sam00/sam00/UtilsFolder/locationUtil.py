# _*_coding:utf-8_*_
# 作者: 唐茹
# 创建时间: 2020/7/28 9:32
# 文件: locationUtil.py
# IDE: PyCharm
# 邮箱: tangru@golaxy.cn
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="Mozilla/4.0 (Windows; MSIE 6.0; Windows NT 5.2)")
location = geolocator.geocode("China")  # 还得是有名地方。名气小的地方这个API会罢工
print(location.address)
print((location.latitude, location.longitude))
print(location.raw)
