from flask import Flask, render_template, request, session, url_for, redirect

app = Flask(__name__)
app.secret_key = 'any random string'  # 这里我们直接给定一个密钥


@app.route('/')
def index():
    msg = ""
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
        nm = request.form['nm']
        pwd = request.form['pwd']
        if nm == 'pupu' and pwd == '123':
            session['username'] = nm  # 使用session存储方式，session默认为数组，给定key和value即可
            return redirect(url_for('index'))  # 重定向跳转到首页
        else:
            return '用户或者密码不匹配!'


if __name__ == "__main__":
    app.run(port=2023, host="127.0.0.1", debug=True)
