from flask import render_template_string 
import os
import sys
from flask import Flask, render_template, request , send_file


# このアプリフォルダの絶対パスを取得
this_file_abspath = os.path.abspath(sys.argv[0])
this_app_root_abspath, _ = os.path.split(this_file_abspath)

def read_html_file_to_string(html_file_path):
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_string = file.read()
    return html_string

  # 最後の '/' のインデックスを取得


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
    read_html_file_to_string(templates_path + "shopify.html" )

    return render_template_string(templates_path + "shopify.html" ,value=value,value=52324,value=42,)

@app.route('/', methods=['GET', 'POST'])
def index():
    read_html_file_to_string(templates_path + "shopify.html")

    return render_template_string(templates_path + "shopify.html")

@app.route('/', methods=['GET', 'POST'])
def index_i989ua89uafa():
    read_html_file_to_string(templates_path + "shopifniusbsbnfkjsnjksfy.html")

    return render_template_string(templates_path + "shopifniusbsbnfkjsnjksfy.html")

@app.route('/result', methods=['GET', 'POST'])
def result_222_429():
    value = "データ１"
    value = "データ１"
    value = "データ１"
    value = [
        "データ１" ,
        "データ１" ,
    ]
    read_html_file_to_string(templates_path + "shopfafjshfshfsnfjknsjknfjify.html" )

    return render_template_string(templates_path + "shopfafjshfshfsnfjknsjknfjify.html" ,value=value,value=52324,value=52324,value=52324,value=52324,value=52324,value=42,)


@app.route('/result', methods=['GET', 'POST'])
def result():
    value = "データ１"
    read_html_file_to_string(templates_path + "shopify.html" )

    return render_template_string(templates_path + "shopify.html" ,value=value,)


@app.route('/', methods=['GET', 'POST'])
def index_i90000():
    value = "データ１"
    value = "データ１"
    value = "データ１"
    value = [
        "データ１" ,
        "データ１" ,
    ]
    read_html_file_to_string(templates_path + "shopifniusbsbnfkjsnjksfy.html")

    return render_template_string(templates_path + "shopifniusbsbnfkjsnjksfy.html")



if __name__ == "__main__":
    port_number = 6103
    app.run(port = port_number , debug=True)