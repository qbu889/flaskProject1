import logging

from flask import Flask, render_template, request, session, redirect, url_for

from testSql import cursor
from utils.dbUtils import dbUtils as dbutil

app = Flask(__name__)
app.secret_key = 'any random string'  # 这里我们直接给定一个密钥


@app.route('/hello')
def hello_world():
    return '我是 python Hello World2!'


@app.route('/hello/<name>')
def hello(name):
    return '这是% s!' % name


@app.route('/')
def index():
    # return render_template("index.html")   #调用render_template函数，传入html文件参数
    msg = "my name is caojianhua, China up!"
    return render_template("index.html", data=msg)  # 加入变量传递


# @app.route('/news')  # 增加一个news页面
# def newspage():
#     newsContent = "全国上下一心支持武汉，武汉加油！"
#     return render_template("news.html", data=newsContent)


@app.route('/product')  # 增加一个product页面
def productpage():
    return render_template("products.html")


@app.route('/login')
def loginpage():
    return render_template("login.html")


@app.route('/loginProcess', methods=['POST', 'GET'])
def loginProcesspage():
    if request.method == 'POST':
        nm = request.form['nm']
        pwd = request.form['pwd']
        if nm == 'lzw' and pwd == '123':
            session['username'] = nm  # 使用session存储方式，session默认为数组，给定key和value即可
            return redirect(url_for('index'))  # 重定向跳转到首页
        else:
            return 'the username or userpwd does not match!'


@app.route('/news')
def newspage():
    with app.app_context():
        newsreal = []
        db = dbutil('web2020.db')  # 链接web2020数据库
        sql = 'select content from news'  # 组装查询sql语句
        newslists = db.db_action(sql, 1)
        # rows = cursor.fetchall()
        forcount = len(newslists)
        for i in range(forcount):
            text = newslists[i][0]
            newsreal.append(text)
            # print(newsreal)

        # 查询处理并返回列表
        # print(newsreal)
        db.close()  # 关闭数据库
        return render_template("news.html", data=newsreal)  # 将数据传递到news.html页面中


if __name__ == '__main__':
    app.run(host="127.0.0.1", debug=True)
