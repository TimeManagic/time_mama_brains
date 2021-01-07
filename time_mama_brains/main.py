from datetime import datetime

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime
from time_mama_brains.config import configure, ConfigEnv

app = Flask(__name__)
config = configure(ConfigEnv.DEV)

app.config.update(config)

# 创建数据库sqlalchemy工具对象
db = SQLAlchemy(app)


# 定义User对象:
class User(db.Model):
    # 表的名字:
    __tablename__ = 'sys_access_user'

    # 表的结构:
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    name = Column(String(20))
    ip = Column(String(20))
    created_at = Column(DateTime())

    def __init__(self, name, ip, created_at):
        self.name = name
        self.ip = ip
        self.created_at = created_at


db.create_all()


@app.route("/")
def index():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip = request.environ['REMOTE_ADDR']
    else:
        ip = request.environ['HTTP_X_FORWARDED_FOR']

    new_user = User('visitor', ip, datetime.now())
    # 添加到session:
    db.session.add(new_user)
    # 提交即保存到数据库:
    db.session.commit()
    # 关闭session:
    db.session.close()
    return "Hello, %s" \
           "Welcome to Flask appliaction created by Serverless Framework.2" % ip


@app.route("/users")
def users():
    users = [{'name': 'test1'}, {'name': 'test2'}]
    return jsonify(data=users)


@app.route("/users/<id>")
def user(id):
    return jsonify(data={'name': 'test1'})
