from flask import Flask,render_template,request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello 蔡承翰!"
@app.route("/mis")
def index():
    return "<h1>資訊管理導論</h1>"


@app.route("/today")
def today():
    now=datetime.now()
    return render_tempalte("today.html",datetime=str(now))

@app.route("about")
def about():
    return render_tempalte("about.html")
    @app.route("/today")


@app.route("/account", methods=["GET", "POST"])
def account():
    if request.method == "POST":
        user = request.form["user"]
        pwd = request.form["pwd"]
        result = "您輸入的帳號是：" + user + "; 密碼為：" + pwd 
        return result
    else:
        return render_template("account.html")
@app.route("/")
def index():
 homepage = "<h1>楊子青Python網頁</h1>"
    homepage += "<a href=/mis>MIS</a><br>"
    homepage += "<a href=/today>顯示日期時間</a><br>"
    homepage += "<a href=/welcome?nick=tcyang>傳送使用者暱稱</a><br>"
    homepage += "<a href=/account>網頁表單傳值</a><br>"
    homepage += "<a href=/about>子青簡介網頁</a><br>"
    return homepage

<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <title>表單</title>
</head>
<body>
    <form action="#" method="post">
        帳號：
        <input type="text" name="user" value="子青">
        <br><br>密碼：
        <input type="password" name="pwd" value="123456">
        <br><br><input type="submit" value="確定送出">
    </form> 
</body>
</html>





if __name__ == "__main__":
    app.run()