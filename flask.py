# coding=utf-8
import invite,os
from  flask import Flask,jsonify,request
app = Flask(__name__)
@app.route("/disco/<invitecode>",methods=["GET"])
def disco(invitecode):
    a=invite.write_code(invitecode)
    if a:
        return jsonify({'code' :200, 'msg': '已提交！请勿重复提交！'})
    else:
        return jsonify({'code': 404, 'msg': '提交错误！'})           

def delete_code():
    a=invite.delete_code()
    if a:
        return jsonify({'msg':'True'})
    else:
        return jsonify({'msg':'False'})
@app.route("/invite_log",methods=["GET"])
def disco_log():
    log=open('111.txt','r')
    return log.read()
@app.route("/log",methods=["GET"])
def log():
        log = open('logg.log', 'r')
        return log.read()
@app.route("/log1",methods=["GET"])
def logg():
        log = open('log1.log', 'r')
        return log.read()
@app.route("/invitecode",methods=["GET"])
def invitelog():
    log = open('invitecode.txt', 'r')
    return log.read()
@app.route('/invite/<num>',methods=['GET'])
def mun(num):
    if invite.code_num(num):
        return jsonify({'msg':'true','num':num})
    else:
        return jsonify({'msg':'false'})
if __name__ == '__main__':
    app.run(host='10.170.0.8',port=5000, debug=True)
