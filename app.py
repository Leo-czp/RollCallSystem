from flask import Flask
from teacher.views import teacher
from config import initConfig
from flask_apscheduler import APScheduler

app = Flask(__name__)

# 加载配置
app.config.from_object(initConfig)


# 用户蓝图
app.register_blueprint(blueprint=teacher)


# 定时任务
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

if __name__ == '__main__':
    app.run()
