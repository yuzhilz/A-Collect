from selenium import webdriver
import lianzhong_api
import requests, json, time, os, random, re, choice
from base64 import b64decode
from selenium.webdriver.chrome.options import Options
def p_main(invitecode, user, pass1):
    try:
        email_random = random.randint(10000, 99999)
        url2 = 'https://10minutemail.net/address.api.php?sessionid=76ade80fb2d3b0f9' + str(
            email_random) + 'e8b0e93bbcb&_=1585393885861'
        r = requests.get(url2)
        if r.status_code == 200:
            result_json = r.json()
            email = result_json['mail_get_mail']
        if email:
            print('邮箱已获取！')
        url = 'https://pjj.one/share?userid=' + invitecode
        chrome_opt = Options()  # 创建参数设置对象.
        chrome_opt = webdriver.ChromeOptions()
        chrome_opt.add_argument('--headless')  # 无界面化.
        chrome_opt.add_argument('--disable-gpu')  # 配合上面的无界面化.
        chrome_opt.add_argument('--window-size=1366,768')  # 设置窗口大小, 窗口大小会有影响.
        chrome_opt.add_argument("--no-sandbox")
        driver = webdriver.Chrome(options=chrome_opt)
        # driver=webdriver.Chrome()
        driver.get(url)
        driver.implicitly_wait(8)
        time.sleep(1)
        # 输入邮箱
        driver.find_element_by_xpath(
            '//*[@id="app"]/section/main/div/div/div[2]/form/div[1]/div[2]/div/span/span/input').send_keys(email)
        #print('正在输入邮箱！')
        # 获取验证码url
        img_str = driver.find_element_by_xpath(
            '//*[@id="app"]/section/main/div/div/div[2]/form/div[2]/div[2]/div/span/span/span/span/img').get_attribute(
            'src')
        print('找到图片！')
        img_str = img_str.split(",")[-1]  # 删除前面的 “data:image/jpeg;base64,”
        img_str = img_str.replace("%0A", '\n')  # 将"%0A"替换为换行符
        img_data = b64decode(img_str)  # b64decode 解码
        with open('./captcha.gif', 'wb') as fout:
            fout.write(img_data)
            fout.close()
        time.sleep(2)
        #print('验证码图片已保存！')
        im = './captcha.gif'
        if im:
            s = lianzhong_api.main(user, pass1, im, 'http://v1-http-api.jsdama.com/api.php?mod=php&act=upload', '', '',
                                   '1008', '8dc962b56f1968a844450834ef91bfd0')
            #print(s.json())
            code = s.json()['data']['val']
            yzm_id=s.json()['data']['id']
            print('图片已识别:'+code)
            driver.find_element_by_xpath(
                '//*[@id="app"]/section/main/div/div/div[2]/form/div[2]/div[2]/div/span/span/span/input').send_keys(
                code)
            #print('正在输入图片验证码！')
            time.sleep(1)
            driver.find_element_by_xpath(
                '//*[@id="app"]/section/main/div/div/div[2]/form/div[3]/div[2]/div/span/span/span/span/button').click()
            #print('正在发送邮箱验证码！')
            time.sleep(5)
            #print('等待邮箱验证码！')
            os.remove(im)
            #print('正在移除保存的图片！')
            url2 = 'https://10minutemail.net/address.api.php?sessionid=76ade80fb2d3b0f9' + str(
                email_random) + 'e8b0e93bbcb&_=1585393885861'
            mail_id = get_emailid(url2,user,pass1,yzm_id)
            mail_id_url = 'https://10minutemail.net//mail.api.php?mailid=' + mail_id + '&sessionid=76ade80fb2d3b0f9' + str(
                email_random) + 'e8b0e93bbcb'
            # print(mail_id_url)
            result = requests.get(url=mail_id_url).json()
            # print(result)
            yanzhenma = result['body'][1]['body']

            im_code = re.findall(r'(?<=验证码为 <b>).+(?=</b>，有效)', yanzhenma)
            # print(im_code)
            driver.find_element_by_xpath(
                '//*[@id="app"]/section/main/div/div/div[2]/form/div[3]/div[2]/div/span/span/span/input').send_keys(
                im_code[0])
            print('正在输入邮箱验证码！')
            driver.find_element_by_xpath(
                '//*[@id="app"]/section/main/div/div/div[2]/form/div[4]/div[2]/div/span/span/input').send_keys(
                'qwer1234')
            #print('正在输入密码！')
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="app"]/section/main/div/div/div[2]/div/p[1]/button').click()
            print('正在点击注册完成！')
            time.sleep(2)
            driver.switch_to.frame("tcaptcha_iframe")
            driver.find_element_by_xpath('//*[@id="captcha_close"]/div').click()
            print('正在关闭滑块！')
            invite_log_write(invitecode)
            time.sleep(2)
            driver.quit()
            return True

    except:
        print('程序有错误，跳出！')
        lianzhong_api.re_err(user, pass1, yzm_id)
        driver.quit()


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


def main():
    m=0
    while m < int(2000):
        user, pass1, invitecode = get_seetting()
        # print(user,pass1,invitecode)
        points=lianzhong_api.get_points(user,pass1)
        points=points.json()['data']
        print(invitecode+'剩余点数：'+str(points))

        if int(points)<=2:
            print(invitecode+'点数不足！！')
        else:
            m = m + 1
            if m % 70 == 0:
                with open('log.log', 'w')as f:
                    f.write('')
                print('*'*20+'wait 3600S!'+'*'*20)
                time.sleep(3600)
            print('正在运行第：' + str(m) + '次!')
            if p_main(invitecode, user, pass1):
                print(invitecode + '--邀请成功：1次！--')
                print('-' * 50)

if __name__ == '__main__':
    main()
