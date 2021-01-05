# _*_coding:utf-8_*_
# ����: ����
# ����ʱ��: 2020/7/28 9:32
# �ļ�: locationUtil.py
# IDE: PyCharm
# ����: tangru@golaxy.cn
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="Mozilla/4.0 (Windows; MSIE 6.0; Windows NT 5.2)")
location = geolocator.geocode("China")  # �����������ط�������С�ĵط����API��չ�
print(location.address)
print((location.latitude, location.longitude))
print(location.raw)
