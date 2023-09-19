from flask import Flask
from flask_sqlalchemy import SQLAlchemy

class flasktest():
    app = Flask(__name__)

    # MYSQL所在的主机名
    HOSTNAME = "127.0.0.1"

    # MYSQL监听的端口号，默认是：3306
    PORT = 3306

    # 连接MYSQL的用户名
    USERNAME = "root"

    # 连接数据库密码
    PASSWORD = "root@123456"

    # MYSQL上创建数据库的名称
    DATABASE = "test"
    app.config[
        "SQLALCHEMY_DATABASE_URI"] = f"mysql+_pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8"
    db = SQLAlchemy(app)
    # 测试连接是否成功
    with db.engine.connect() as conn:
        rs = conn.execute("select 1")
        print(rs)

if __name__ == '__main__':
    flasktest()