# -*- coding: UTF-8 -*-
from flask import Flask
import json
from flask_restful import Api
from resources.user import UserReg, UserLogin
from config.config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# SQLAlchemy初使化
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + Config.MYSQL_USER + ':' + Config.MYSQL_PASSWORD + '@' + Config.MYSQL_HOST+ '/' + Config.MYSQL_DBNAME
# 不配置会报错提示。如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它。
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy()
db.init_app(app)

# 创建api
api = Api(app)

api.add_resource(UserReg, '/user/reg')
api.add_resource(UserLogin, '/user/login')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
