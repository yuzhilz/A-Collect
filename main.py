from  flask import Flask,jsonify,request
app = Flask(__name__)
@app.route("/pjj/<invitecode>",methods=["GET"])
def disco(invitecode):
    invitecode=invitecode+'\n'
    with open('setting.txt','r') as f:
        if invitecode in f.read():
            return jsonify({'code' :400, 'msg': '已提交！请勿重复提交！'})
        else:
            with open('setting.txt','a') as s:
                s.write(invitecode)
                return jsonify({'code' :200, 'msg': '提交成功！请勿重复提交！'})
@app.route("/pjj/delete",methods=["GET"])
def delete_code():
    with open('setting.txt','w') as f:
        f.write('')
        return jsonify({'msg':'True'})
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
    log = open('setting.txt', 'r')
    return log.read()

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)
