from datetime import timedelta
import os

class initConfig(object):
    # INIT
    SECRET_KEY = os.urandom(24)
    DEBUG = True
    # SEND_FILE_MAX_AGE_DEFAULT = timedelta(seconds=1)   # 强制取消缓存
    KEY = "x9uo3L1xDDcF58Pt"

    # 周次
    DICT_WEEK = {"2021-01-04" : 1,
            "2021-01-11" : 2}
    # 节次
    DICT_TIME ={"08:20" : 1,
                '09:10' : 2,
                "10:00" : 3,
                "10:50" : 4,
                "11:40" : 5,
                "14:00" : 6,
                "14:50" : 7,
                "15:40" : 8,
                "16:30" : 9,
                "17:20" : 10,
                "19:00" : 11,
                "19:50" : 12,
                "20:40" : 13,
                "21:30" : 14}


    # 定时任务配置
    SCHEDULER_API_ENABLED = True
    JOBS = [
        {
            'id': 'No1',
            'func': 'timedTask.emailTask:task1',
            'args': '',
            'trigger': {
                'type': 'cron',  # 类型
                # 'day_of_week': "0-6", # 可定义具体哪几天要执行
                'hour': '3', # 小时数
                'minute': '1',
                'second': '3'
            }
        }
    ]



class dbConfig(object): # db
    HOST = "localhost"
    DB = "RollCallSystem"
    USERNAME = "root"
    USERPASSWORD = os.environ.get('MYSQL_PASSWORD') # 从环境变量读取数据库密码
