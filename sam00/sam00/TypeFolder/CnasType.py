# _*_coding:utf-8_*_
# ����: ����
# ����ʱ��: 2020/7/27 17:12
# �ļ�: CnasType.py
# IDE: PyCharm
# ����: tangru@golaxy.cn

from elasticsearch_dsl import Document, Nested, Date, Boolean, analyzer, Completion, Text, Keyword, Integer, Object
from elasticsearch_dsl.connections import connections

connections.create_connection(hosts="10.170.130.230:9202")


class CnasType(Document):
    information = Object()
    # name
    name = Text(analyzer="ik_max_word")
    # url
    url = Keyword()
    # title
    title = Text(analyzer="ik_max_word")
    # pub_time
    pub_time = Keyword()
    # author
    author = Keyword()
    # type
    type = Keyword()
    # content
    content = Text(analyzer="ik_max_word")
    # date = Date()

    class Index:
        # ���ݿ����ƺͱ�����
        name = "record"
        # type = "ThinkTanks"


if __name__ == '__main__':
    CnasType.init()
