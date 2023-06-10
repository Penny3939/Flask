from flask import Flask, request,jsonify #jsonify將json轉成dictionary/list
import poker as p

app= Flask(__name__) #告訴它這隻程式是主程式

@app.route("/") #接口名稱需為字串
#建立接口
def hello_flask():        #hello_flask自行命名
    return "<h1> Hello Flask!12444</h1>"  #回傳值需為字串

@app.route("/poker/<num>")
def poker(num):
    json_data = p.poker(int(num))

    return jsonify(json_data)

if __name__ =="__main__":
    app.run(debug=True,host="0.0.0.0", port=5001)