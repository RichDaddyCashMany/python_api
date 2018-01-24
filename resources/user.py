from flask_restful import Resource, reqparse, fields, marshal
from flask_sqlalchemy import SQLAlchemy
from model.model import User as UserModel
import hashlib
import time

db = SQLAlchemy()


class UserReg(Resource):
    def get(self):
        return self.handle()

    def post(self):
        return self.handle()

    def handle(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username')
        parser.add_argument('password')
        args = parser.parse_args()

        isExist = db.session.query(UserModel).filter_by(username=args.username).first()
        if isExist:
            return {"error": "-1", "msg": "user is exist"}

        if len(args.password) < 6 or len(args.password) > 16:
            return {"error": "-1", "msg": "password's length must between [6-16]"}

        md5 = hashlib.md5()
        md5.update(args.password)

        user = UserModel(username=args.username, password=md5.hexdigest(), create_at=int(time.time()))
        db.session.add(user)
        db.session.commit()

        return {"error": "0", "msg": "success"}


class UserLogin(Resource):
    def get(self):
        return self.handle()

    def login(self):
        return self.handle()

    def handle(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username')
        parser.add_argument('password')
        args = parser.parse_args()

        user = db.session.query(UserModel).filter_by(username=args.username).first()
        if user == None:
            return {"error":"-1", "msg":"account not exists"}

        pwd = hashlib.md5()
        pwd.update(args.password)

        if user.password == pwd.hexdigest():
            token = hashlib.md5()
            token.update(str(time.time()))

            user.token = token.hexdigest()
            db.session.commit()

            data = db.session.query(UserModel).filter_by(username=args.username).first()
            dict = {
                'token': fields.String,
                'create_at': fields.Integer
            }

            return {"error": "0", "msg": "success", "data":marshal(data, dict)}
        else:
            return {"error": "-1", "msg": "not a correct password"}


