from flask import Flask, request

app= Flask(__name__) #告訴它這隻程式是主程式

@app.route("/") #接口名稱需為字串
#建立接口
def hello_flask():        #hello_flask自行命名
    return "<h1> Hello Flask!12444</h1>"  #回傳值需為字串

@app.route("/greet/<name>")  #要自行在網頁後輸入/greet/Penny
def greet(name):
    return "Hello {}".format(name)

@app.route("/two_sum/<x>/<y>") #要自行在網頁後輸入/two_sum/5/8
def two_sum(x,y):
    return str(int(x)+ int(y)) #只能接受字串str,結果為13

#以下方式[GET] /get_names/ department_id:string/team_id:string
"""Response:
    [
        {
            "emp_name":"Allen",
            "emp_id":13
        },
        {
            "emp_name":"Ted",
            "emp_id":44
        }, ...
    ]
"""
@app.route("/get_name/<department_code>/<team_id>")
def get_name(department_id,team_id):
    sql="""
        SELECT emp_name, emp_id FROM emp
        WHERE department_id ={}
        AND team_id ='{}';
    """.format(department_id,team_id)
    return sql

#在網頁上要用"?"來接name&age => /hello_get?name=Allen & age=22
@app.route("/hello_get")
def hello_get():
    name = request.args.get("name")
    age = request.args.get("age")

    if name is None:
        output_html = "<h1> What's your name?</h1>"
    elif age is None:
        output_html = "<h1> Hello {}.</h1>".format(name)
    else:
        output_html = "<h1>Hello {}, you are {} years old.</h1>".format(name,age)
    return output_html

#啟動網頁伺服器
#host="0.0.0.0",限制可以連入網頁伺服器的IP
#設置Debug,若有任何變動不需要重新啟動網頁伺服器,直接在網頁上refresh就可更新
if __name__ =="__main__":
    app.run(debug=True,host="0.0.0.0", port=5000)