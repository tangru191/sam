# _*_coding:utf-8_*_
# ����: ����
# ����ʱ��: 2020/7/29 17:44
# �ļ�: MilitaryType.py
# IDE: PyCharm
# ����: tangru@golaxy.cn

from elasticsearch_dsl import Document, Nested, Date, Boolean, analyzer, Completion, Text, Keyword, Integer, Object
from elasticsearch_dsl.connections import connections

connections.create_connection(hosts="10.170.130.230:9202")


class MilitaryType(Document):
    # information
    information = Object()
    # name
    name = Keyword()
    # url
    url = Keyword()
    # date
    date = Date()
    # type
    type = Keyword()

    class Index:
        # ���ݿ����ƺͱ�����
        name = "record"
