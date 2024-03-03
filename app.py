"""
windowsでpyinstallerが使えるコードに変換
------------------------
# macルートディレクトリ直下の絶対パス
this_file_abspath = os.path.abspath(sys.argv[0])
last_slash_index = this_file_abspath.rfind('/')  # 最後の '/' のインデックスを取得
this_app_root_abspath = this_file_abspath[:last_slash_index]

# Windowsルートディレクトリ直下の絶対パス
this_file_abspath = os.path.abspath(sys.argv[0])
this_app_root_abspath, _ = os.path.split(this_file_abspath)
------------------------
"""
from flask import Flask, render_template, request , send_file
import os

# flaskアプリの明示
templates_path = 'templates/'
static_path = 'static/'
app = Flask(__name__ , template_folder=templates_path, static_folder=static_path)

# パスの定義
txt_folder_path = static_path + "txt/"
py_folder_path = static_path + "python/"
mac_txt_file_path = txt_folder_path + "mac_for_exe.txt"
win_txt_file_path = txt_folder_path + "win_for_exe.txt"
mac_py_file_path = py_folder_path + "mac_for_exe.py"
win_py_file_path = py_folder_path + "win_for_exe.py"



def py_to_txt(py_file_path , txt_file_path):
    """ Pythonファイルをtxtファイルに変換する関数 """
    with open(py_file_path, 'r', encoding='utf-8') as py_file:
        # Pythonファイルを読み込み、内容をテキストファイルに書き込む
        py_content = py_file.read()
        with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(py_content)

def txt_to_py(py_file_path , txt_file_path):
    """ txtファイルをPythonファイルに変換する関数 """
    with open(txt_file_path, 'r', encoding='utf-8') as txt_file:
        txt_content = txt_file.read()
        # Pythonファイルに書き込み
        with open(py_file_path, 'w', encoding='utf-8') as py_file:
            py_file.write(txt_content)



def mac_txt_to_win_txt(mac_txt_file_path , win_txt_file_path):
    """ macでpyinstallerを使うコードtxtをWindows用に変換するコード """
    with open(mac_txt_file_path, 'r', encoding='utf-8') as mac_txt_data:
        mac_txt_str = mac_txt_data.read()
    
    # print(mac_txt_str)

    # 削除対象の文字列が存在するか確認し、削除
    strings_to_remove_list = [
        "this_file_abspath = os.path.abspath(sys.argv[0])",
        "last_slash_index = this_file_abspath.rfind('/')",
        "this_app_root_abspath = this_file_abspath[:last_slash_index]" ,
    ]
    strings_to_add_list = [
        "this_file_abspath = os.path.abspath(sys.argv[0])" ,
        "this_app_root_abspath, _ = os.path.split(this_file_abspath)" ,
    ]
    strings_to_add = '\n'.join(strings_to_add_list)

    function_html_file_to_str_list = [
        "def read_html_file_to_string(html_file_path):" ,
        "    with open(html_file_path, 'r', encoding='utf-8') as file:" ,
        "        html_string = file.read()" ,
        "    return html_string" ,
    ]
    function_html_file_to_str = '\n'.join(function_html_file_to_str_list)
    
    # mac用の絶対パスのコードを削除
    for loop , string_to_remove in enumerate(strings_to_remove_list):
        start_index = mac_txt_str.find(string_to_remove)
        end_index = start_index + len(string_to_remove)
        if loop == 0:
            mac_txt_str = mac_txt_str[:start_index] + strings_to_add + "\n\n" + function_html_file_to_str + "\n" + mac_txt_str[end_index:]
        else:
            mac_txt_str = mac_txt_str[:start_index] + mac_txt_str[end_index:]

    
    # templatesを変更
    mac_txt_str = "from flask import render_template_string \n" + mac_txt_str
    replace_str = "return render_template_string("
    target_str = "return render_template("
    
    template_str_start_indice_list = [i for i in range(len(mac_txt_str)) if mac_txt_str.startswith("return render_template", i)]
    template_str_end_indice = 0
    loop_flag = True
    while loop_flag :
        template_str_start_indice = mac_txt_str.find(target_str , template_str_end_indice)
        if template_str_start_indice == -1:
            loop_flag = False
            break
        template_str_end_indice = mac_txt_str.find(")", template_str_start_indice)
        template_str = mac_txt_str[ template_str_start_indice : template_str_end_indice + 1]

        templates_dir_str = "templates_path + "
        comma_count = template_str.count(',')   # 「,」の数を数える
        if comma_count > 0:
            # 「render_template(」より後、かつ、一つ目のカンマより前の部分を削除
            start_index = template_str.find("render_template(") + len("render_template(")
            end_index = template_str.find(",", start_index)
            if end_index != -1:
                html_file_name = template_str[start_index : end_index].replace("\n", "").replace(" ", "") + " "
                ### 一つ目のカンマより後を取得
                templates_variable_area = template_str[ end_index : ].replace("\n", "").replace(" ", "").replace(")", "")
                # render_template()内を編集
                after_template_str = template_str[:start_index] + templates_dir_str + html_file_name + templates_variable_area
            # htmlファイルを読み込み文字列に変換するコード
            html_to_str_area = "read_html_file_to_string(templates_path + " + html_file_name + ")" + "\n"
            # mac用のtemplates領域を完全削除
            mac_txt_str = mac_txt_str[ : template_str_start_indice ] + html_to_str_area + "\n" + "    " + replace_str   +   after_template_str[ len(target_str) : ]       + mac_txt_str[template_str_end_indice : ]
            # mac_txt_str = mac_txt_str[ : template_str_start_indice ] + replace_str   +   after_template_str[ len(target_str) : ]       + mac_txt_str[template_str_end_indice : ]
            print(f"replace_str : {replace_str}")
        else:
            start_index = template_str.find("render_template(") + len("render_template(")
            end_index = template_str.find(")", start_index)
            html_file_name = template_str[start_index : end_index]
            after_template_str = templates_dir_str + html_file_name
            html_to_str_area = "read_html_file_to_string(templates_path + " + html_file_name + ")" + "\n"
            # mac_txt_str = mac_txt_str[ : template_str_start_indice ] + html_to_str_area + replace_str +      after_template_str      + mac_txt_str[template_str_end_indice : ]
            # print(f"replace_str : {replace_str}")
            mac_txt_str = mac_txt_str[ : template_str_start_indice ] + html_to_str_area + "\n" + "    " + replace_str +      after_template_str      + mac_txt_str[template_str_end_indice : ]


    # 結果をファイルに書き込み
    with open(win_txt_file_path, 'w', encoding='utf-8') as win_txt_file:
        win_txt_file.write(mac_txt_str)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        mac_py_file = request.files['py_file']
        mac_py_file.save(mac_py_file_path)
        
        # mac用のPythonファイルをtxtに変換
        py_to_txt(mac_py_file_path , mac_txt_file_path)
        # mac用のコードtxtをWindows用に変換
        mac_txt_to_win_txt(mac_txt_file_path , win_txt_file_path)
        # txtをWindows用のPythonファイルに変換
        txt_to_py(win_py_file_path , win_txt_file_path)

        form_flag = True
        return render_template(
            "index.html" ,
            form_flag = form_flag ,
        )
    
    return render_template(
        "index.html" ,
    )

@app.route('/win_py_download')
def win_py_download():
    directory = os.path.join(app.root_path, 'files') 
    return send_file(win_py_file_path , as_attachment=True)

if __name__ == "__main__":
    port_number = 8810
    app.run(port = port_number , debug=True)