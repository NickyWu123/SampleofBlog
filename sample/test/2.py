# -*- coding: utf-8 -*-  
from flask import Flask, jsonify, render_template, request  
app = Flask(__name__)  
  
@app.route("/")  
def index():  
# 主页面  
    return render_template("main.html")  
     
@app.route('/add')  
def add_numbers():  
    a = request.args.get('a', 0, type=int) 
    b = request.args.get('b', 0, type=int) 
    print a
    print b
    return jsonify(result = a + b)  
     
if __name__=="__main__":  
    app.run(host = "0.0.0.0",port = 8080, debug = True)  