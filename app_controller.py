from flask import Flask, request,jsonify,render_template #jsonify將json轉成dictionary/list
import model
from test_controller import test_controller

app= Flask(__name__,static_url_path="/resource",static_folder="./my_resource")#網頁後面加上: /resource/test.txt

app.register_blueprint(test_controller, url_prefix="/controller_A") #網頁後麵加上:/controller_A/test_ctrl


@app.route("/") #接口名稱需為字串
#建立接口
def hello_flask():        #hello_flask自行命名
    return "<h1> Hello Flask!12444</h1>"  #回傳值需為字串

if __name__ =="__main__":
    app.run(debug=True,host="0.0.0.0", port=5001)