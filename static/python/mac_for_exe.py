import os
import sys
from flask import Flask, render_template, request , send_file


# このアプリフォルダの絶対パスを取得
this_file_abspath = os.path.abspath(sys.argv[0])
last_slash_index = this_file_abspath.rfind('/')  # 最後の '/' のインデックスを取得
this_app_root_abspath = this_file_abspath[:last_slash_index]

# flaskアプリの明示
templates_path = os.path.join(this_app_root_abspath, 'templates/')
static_path = os.path.join(this_app_root_abspath, 'static/')
app = Flask(__name__ , template_folder=templates_path, static_folder=static_path)

@app.route('/result', methods=['GET', 'POST'])
def result_222():
    value = "データ１"
    value = [
        "データ１" ,
        "データ１" ,
    ]
    return render_template(
        "shopify.html" ,
        value = value ,
        value = 52324 ,
        value = 42 ,
    )

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("shopify.html")

@app.route('/', methods=['GET', 'POST'])
def index_i989ua89uafa():
    return render_template("shopifniusbsbnfkjsnjksfy.html")

@app.route('/result', methods=['GET', 'POST'])
def result_222_429():
    value = "データ１"
    value = "データ１"
    value = "データ１"
    value = [
        "データ１" ,
        "データ１" ,
    ]
    return render_template(
        "shopfafjshfshfsnfjknsjknfjify.html" ,
        value = value ,value = 52324 ,
        value = 52324 ,value = 52324 ,value = 52324 ,value = 52324 ,
        value = 42 ,
    )


@app.route('/result', methods=['GET', 'POST'])
def result():
    value = "データ１"
    return render_template(
        "shopify.html" ,
        value = value ,
    )


@app.route('/', methods=['GET', 'POST'])
def index_i90000():
    value = "データ１"
    value = "データ１"
    value = "データ１"
    value = [
        "データ１" ,
        "データ１" ,
    ]
    return render_template("shopifniusbsbnfkjsnjksfy.html")



if __name__ == "__main__":
    port_number = 6103
    app.run(port = port_number , debug=True)