import requests, json, time, os, random, re, choice,lianzhong_api
from base64 import b64decode

def main(invitecode, user, pass1):
    try:
        #print(user,pass1)
        email_random = random.randint(10000, 99999)
        url2 = 'https://10minutemail.net/address.api.php?sessionid=76ade80fb2d3b0f9' + str(
            email_random) + 'e8b0e93bbcb&_=1585393885861'
        r = requests.get(url2)
        if r.status_code == 200:
            email = r.json()['mail_get_mail']
            #print(email)
        session = requests.session()
        res = session.get(url='https://pjj.one/api/common/image/captcha').json()
        img_token = res['data']['token']
        img_str = res['data']['image']

        #print(img_token)
        # print(img_base)
    
        img_str = img_str.split(",")[-1]  # 删除前面的 “data:image/jpeg;base64,”
        img_str = img_str.replace("%0A", '\n')  # 将"%0A"替换为换行符
        img_data = b64decode(img_str)  # b64decode 解
        with open('./captcha.gif', 'wb') as fout:
            fout.write(img_data)
            fout.close()
        time.sleep(2)
        im = './captcha.gif'
        s = lianzhong_api.main(user, pass1, im, 'http://v1-http-api.jsdama.com/api.php?mod=php&act=upload', '',
                               '', '1008', '8dc962b56f1968a844450834ef91bfd0')
        print(s.json())
        code = s.json()['data']['val']
        yzm_id = s.json()['data']['id']
        #print(code)
        # print(yzm_id)
        data = {'appId': '1013','email':email,'imageCode':code,'imageToken': img_token}

        headers = {
            'Content-Type':'application/json',
            'Accept': '*/*',
            'Cache-Control': 'no-cache',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Length': '1055',
            'Connection': 'keep-alive',
            'cache-control':'no-cache'

        }
        s = session.post(url='https://pjj.one/api/common/email/captcha',headers=headers, data=json.dumps(data))
        #print(s.json())
        time.sleep(8)
        url3 = 'https://10minutemail.net/address.api.php?sessionid=76ade80fb2d3b0f9' + str(
            email_random) + 'e8b0e93bbcb&_=1585393885861'
        mail_id = get_emailid(url3, user, pass1, yzm_id)
        mail_id_url = 'https://10minutemail.net//mail.api.php?mailid=' + mail_id + '&sessionid=76ade80fb2d3b0f9' + str(
            email_random) + 'e8b0e93bbcb'
        # print(mail_id_url)
        # print(result)
        yanzhenma = requests.get(url=mail_id_url).json()['body'][1]['body']
        im_code = re.findall(r'(?<=验证码为 <b>).+(?=</b>，有效)', yanzhenma)[0]
        #print(im_code)
        deviceID='7c6706ae956edb'+str(email_random)+'53ecf'+str(email_random)+'a86'
        passw='qwer'+str(email_random)
        js_data={
            "appId": 1013,
            "channelId": "",
            "inviterCode": invitecode,
            "deviceId": deviceID,
            "version": "1.1.1",
            "userIp": "",
            "email": email,
            "password": passw,
            "randStr": "",
            "ticket": "",
            "captcha": im_code
        }
        ss=session.post(url='https://pjj.one/api/app/email/register',headers=headers,data=json.dumps(js_data)).text
        #print(ss)
        if '"message":"执行成功"' in ss :
            print(invitecode+'-邀请完成')
        else:print(invitecode+'-邀请失败！')
    except:
        print('未知错误！跳出！')

def get_emailid(url2,user,pass1,yzm_id):
    r = requests.get(url2).json()
    # print(r)

    mail_id = r['mail_list'][0]['mail_id']
    print(mail_id)
    if mail_id == 'welcome':
        time.sleep(20)
        r = requests.get(url2).json()
        print(r)
        s =lianzhong_api.re_err(user,pass1,yzm_id)
        mail_id = r['mail_list'][0]['mail_id']
        return mail_id
    else:
        return mail_id
def frist_write(invitecode):  # 判断是否第一次写入
    f = open('111.txt', 'r')
    s1 = f.read()
    f.close()
    if invitecode in s1:
        return True
    else:
        f = open('111.txt', 'a')
        f.write(invitecode + '邀请成功:1次!\n')
        f.close()


def find_invite(invitecode):
    # 找到需要替换的
    f = open('111.txt', 'r')
    s = f.readlines()
    for line in s:
        if invitecode in line:
            # print('find')
            d = re.findall(r'(?<=邀请成功:).*(?=次!\n)', line)
            d = int(d[0]) + 1
            break
    f.close()
    return line, d



def re_line(line, d, invitecode):
    f = open('111.txt', 'r')
    s1 = f.read()
    newline = invitecode + '邀请成功:' + str(d) + '次!\n'
    line = s1.replace(line, newline)
    # print(line)
    f.close()
    f = open('111.txt', 'w')
    f.write(line)
    f.close()


def invite_log_write(invitecode):  # 写入LOG
    if frist_write(invitecode):
        # print('not frist')
        line, d = find_invite(invitecode)
        re_line(line, d, invitecode)


def get_seetting():  # 联众账户
    with open('setting.txt', 'r') as f:
        f = f.readlines()
        r=random.choice(f)
        user = re.findall(r'(?<=user=).+(?=pas)', r)[0].replace('\n','')
        pass1 = re.findall(r'(?<=ass=).+(?=inviteco)', r)[0].replace('\n','')
        invitecode = re.findall(r'(?<=invitecode=).+', r)[0].replace('\n','')
        return user, pass1,invitecode
if __name__ == '__main__':
    m = 0
    while True:
        user,pass1,invitecode=get_seetting()
        points = lianzhong_api.get_points(user, pass1)
        points = points.json()['data']
        print(invitecode + '剩余点数：' + str(points))
        m+=1
        if int(points) <= 2:
            print(invitecode + '点数不足！！')
            time.sleep(10)
            continue
        else:
            print('正在运行第：' + str(m) + '次!')
            main(invitecode, user,pass1)
