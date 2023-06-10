from flask import Flask, request,jsonify,render_template #jsonify將json轉成dictionary/list
import poker as p
import model

app= Flask(__name__,static_url_path="/resource",static_folder="./my_resource")
#網頁後面加上: /resource/test.txt

@app.route("/") #接口名稱需為字串
#建立接口
def hello_flask():        #hello_flask自行命名
    return "<h1> Hello Flask!12444</h1>"  #回傳值需為字串


@app.route('/show_staff')
def hello_google():
    staff_data = model.getStaff()
    column = ['ID', 'Name', 'DeptId', 'Age', 'Gender', 'Salary']
    return render_template('show_staff.html', staff_data=staff_data,
                                              column=column)

if __name__ =="__main__":
    app.run(debug=True,host="0.0.0.0", port=5001)