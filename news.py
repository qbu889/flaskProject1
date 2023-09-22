from flask import Blueprint, render_template

from utils.dbUtils import dbUtils

news = Blueprint('news', __name__)  # news蓝图


@news.route('/news')
def newspage():
    db = dbUtils('web2020.db')
    sql = 'select * from news'
    newslist = db.db_action(sql, 1)
    return render_template("news.html", data=newslist)


@news.route('/news/edit')
def newsEditpage():
    return '/news/edit'
