from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    msg = "my name is caojianhua, China up!"
    return render_template("index.html", data=msg)


@app.route('/news')  # 增加一个news页面
def newspage():
    newsContent = "全国上下一心支持武汉，武汉加油！"
    return render_template("news.html", data=newsContent)


@app.route('/product/<a>')  # 增加一个product页面
def productpage(a):
    return render_template("products.html", data=a)


@app.route('/login')
def loginpage():
    return render_template("login.html")


@app.route('/loginProcess', methods=['POST', 'GET'])
def loginProcesspage():
    if request.method == 'POST':
        nm = request.form['nm']  # 获取姓名文本框的输入值
        pwd = request.form['pwd']  # 获取密码框的输入值
        if nm == 'pupu' and pwd == '123':
            return render_template("index.html", data=nm)  # 使用跳转html页面路由
        else:
            return '用户或者密码不匹配！'


if __name__ == "__main__":
    app.run(port=2020, host="127.0.0.1", debug=True)
