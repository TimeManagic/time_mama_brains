import os
from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 读取配置
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgresql://tencentdb_3501ozmp:o3b%7C!82ax%7BKcG4U@10.0.0.14:5432/tencentdb_3501ozmp'
# app.config[
#     'SQLALCHEMY_DATABASE_URI'] = 'postgresql://tencentdb_3501ozmp:o3b%7C!82ax%7BKcG4U@postgres-3501ozmp.sql.tencentcdb.com:50140/tencentdb_3501ozmp'
# 设置sqlalchemy自动更跟踪数据库
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 查询时会显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = True
# 禁止自动提交数据处理
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = False
# 创建数据库sqlalchemy工具对象
db = SQLAlchemy(app)


# 定义User对象:
class User(db.Model):
    # 表的名字:
    __tablename__ = 'sys_access_user'

    # 表的结构:
    id = Column(Integer, primary_key=True, autoincrement=True,nullable=True)
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
