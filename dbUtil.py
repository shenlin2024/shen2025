import pymysql
from pymysql.cursors import DictCursor
# 数据库连接工具
db = pymysql.connect(
    host="localhost", #主机名
    port=3306, # 端口号
    database="job", # 连接的数据库名，每个项目建一个
    user="root", # 账号
    passwd="123456", # 密码
    charset="utf8" # 字符集
)