from flask import Blueprint, render_template

product = Blueprint('product', __name__)


@product.route('/product/<a>')
def productpage(a):
    return render_template("product.html", data=a)
