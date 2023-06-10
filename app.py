from flask import Flask

app= Flask(__name__) #告訴它這隻程式是主程式

@app.route("/") #接口名稱需為字串

#建立接口
def hello_flask():        #hello_flask自行命名
    return "<h1> Hello Flask!12444</h1>"  #回傳值需為字串

#啟動網頁伺服器
#host="0.0.0.0",限制可以連入網頁伺服器的IP
#設置Debug,若有任何變動不需要重新啟動網頁伺服器,直接在網頁上refresh就可更新
if __name__ =="__main__":
    app.run(debug=True,host="0.0.0.0", port=5000)
