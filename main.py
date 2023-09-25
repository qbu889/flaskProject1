from flask import Flask, render_template, request, session, url_for, redirect


from utils.dbutil import dbUtils

app = Flask(__name__)
app.secret_key = 'any random string'  # 这里我们直接给定一个密钥


@app.route('/')
def index():
    msg = ""
    return render_template("index.html", data=msg)


@app.route('/news')
def newspage():
    newsreal = []
    # 导入dbutil模块，就是上面这个文件
    db = dbUtils('web2023.db')  # 链接web2020数据库
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


@app.route('/product/<a>')  # 增加一个product页面
def productpage(a):
    return render_template("products.html", data=a)


@app.route('/login')
def loginpage():
    return render_template("login.html")


@app.route('/loginProcess', methods=['POST', 'GET'])
def loginProcesspage():
    if request.method == 'POST':
        nm = request.form['nm']
        pwd = request.form['pwd']
        if nm == 'pupu' and pwd == '123':
            session['username'] = nm  # 使用session存储方式，session默认为数组，给定key和value即可
            return redirect(url_for('index'))  # 重定向跳转到首页
        else:
            return '用户或者密码不匹配!'


if __name__ == "__main__":
    app.run(port=2023, host="127.0.0.1", debug=True)
