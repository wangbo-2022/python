from flask import Flask,render_template,request
import datetime

app = Flask(__name__)


# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!你好'

@app.route('/user/<name>')
def user(name):
    return '你好%s' % name

@app.route('/user/<int:id>')
def user1(id):
    return '你好%d号会员' % id

@app.route('/')
def index():
    time = datetime.date.today()
    name = ["小张","小王"]
    task = {"任务":"打扫卫生","时间":"3小时"}
    return render_template("index.html", var=time,list=name,task=task)

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/result',methods=['POST','GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html",result=result)


if __name__ == '__main__':
    app.run()
