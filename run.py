from selenium import webdriver
import lianzhong_api
import requests,json,time,os,random,re,choice
from base64 import b64decode
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
#import pyperclip
#import pyautogui

def p_main(invitecode,user,pass1,token2):
    try:
        email_random=random.randint(10000,99999)
        url2 = 'https://10minutemail.net/address.api.php?sessionid=76ade80fb2d3b0f9'+str(email_random)+'e8b0e93bbcb&_=1585393885861'
        r = requests.get(url2)
        if r.status_code == 200:
            result_json = r.json()
            email = result_json['mail_get_mail']
        if email:
            print('邮箱已获取！')
        url='https://pjj.one/share?userid='+invitecode
        chrome_opt = Options()  # 创建参数设置对象.
        chrome_opt = webdriver.ChromeOptions()
        chrome_opt.add_argument('--headless')  # 无界面化.
        chrome_opt.add_argument('--disable-gpu')  # 配合上面的无界面化.
        chrome_opt.add_argument('--window-size=1366,768')  # 设置窗口大小, 窗口大小会有影响.
        chrome_opt.add_argument("--no-sandbox")  
        driver = webdriver.Chrome(options=chrome_opt)
        #driver=webdriver.Chrome()
        driver.get(url)
        driver.implicitly_wait(8)
        time.sleep(1)
        #输入邮箱
        driver.find_element_by_xpath('//*[@id="app"]/section/main/div/div/div[2]/form/div[1]/div[2]/div/span/span/input').send_keys(email)
        print('正在输入邮箱！')
        #获取验证码url
        img_str = driver.find_element_by_xpath('//*[@id="app"]/section/main/div/div/div[2]/form/div[2]/div[2]/div/span/span/span/span/img').get_attribute('src')
        print('找到图片！')
        img_str = img_str.split(",")[-1]  # 删除前面的 “data:image/jpeg;base64,”
        img_str = img_str.replace("%0A", '\n')  # 将"%0A"替换为换行符
        img_data = b64decode(img_str)  # b64decode 解码
        with open('./captcha.gif', 'wb') as fout:
            fout.write(img_data)
            fout.close()
        time.sleep(2)
        print('验证码图片已保存！')
        im='./captcha.gif'
        if im:
            s=lianzhong_api.main(user,pass1,im,'http://v1-http-api.jsdama.com/api.php?mod=php&act=upload','','','1008',token2)
            code=s.json()['data']['val']
            print('图片已识别！')
            driver.find_element_by_xpath('//*[@id="app"]/section/main/div/div/div[2]/form/div[2]/div[2]/div/span/span/span/input').send_keys(code)
            print('正在输入图片验证码！')
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="app"]/section/main/div/div/div[2]/form/div[3]/div[2]/div/span/span/span/span/button').click()
            print('正在发送邮箱验证码！')
            time.sleep(5)
            print('等待邮箱验证码！')
            os.remove(im)
            print('正在移除保存的图片！')
            url2 = 'https://10minutemail.net/address.api.php?sessionid=76ade80fb2d3b0f9'+str(email_random)+'e8b0e93bbcb&_=1585393885861'
            mail_id=get_emailid(url2)
            mail_id_url='https://10minutemail.net//mail.api.php?mailid='+mail_id+'&sessionid=76ade80fb2d3b0f9'+str(email_random)+'e8b0e93bbcb'
            #print(mail_id_url)
            result=requests.get(url=mail_id_url).json()
            #print(result)
            yanzhenma=result['body'][1]['body']

            im_code=re.findall(r'(?<=验证码为 <b>).+(?=</b>，有效)', yanzhenma)
            #print(im_code)
            driver.find_element_by_xpath('//*[@id="app"]/section/main/div/div/div[2]/form/div[3]/div[2]/div/span/span/span/input').send_keys(im_code[0])
            print('正在输入邮箱验证码！')
            driver.find_element_by_xpath('//*[@id="app"]/section/main/div/div/div[2]/form/div[4]/div[2]/div/span/span/input').send_keys('qwer1234')
            print('正在输入密码！')
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="app"]/section/main/div/div/div[2]/div/p[1]/button').click()
            print('正在点击注册完成！')
            time.sleep(1)
            driver.switch_to.frame("tcaptcha_iframe")
            driver.find_element_by_xpath('//*[@id="captcha_close"]/div').click()
            print('正在关闭滑块！')

            time.sleep(2)
            driver.quit()
            return True

    except:
        print('程序有错误，跳出！')
        driver.quit()
def get_emailid(url2):
    r = requests.get(url2).json()
    #print(r)

    mail_id = r['mail_list'][0]['mail_id']
    print(mail_id)
    if mail_id == 'welcome':
        time.sleep(20)
        r = requests.get(url2).json()
        print(r)
        mail_id = r['mail_list'][0]['mail_id']
        return mail_id
    else:
        return mail_id

def get_invietecode():
    s = open('invitecode.txt', 'r')
    k = s.readlines()
    i = len(k)
    # print(i)
    if i == 0:
        return False
    elif i == 1:
        a = 0
    else:
        i = i + 1
        a = random.randrange(1, i)  # 1-9中生成随机数
        a = a - 1
        # 从文件poem.txt中对读取第a行的数据
    # print(a)
    invitecode = k[a]
    # print(invitecode)
    s.close()
    print('挑选邀请码！')
    return invitecode.replace('\n','')
def get_num():
    with open('num.txt','r')as f :
        return f.read().replace('\n','')
def get_seetting():
    with open('setting.txt','r') as f:
        f=f.readlines()
        user=f[0].replace('user:','').replace('\n','')
        pass1=f[1].replace('pass:','').replace('\n','')
        token2=f[2].replace('token:', '').replace('\n', '')
        return user,pass1,token2
def main():
    #num=input('请输入次数：')
    num=get_num()
    user,pass1,token2=get_seetting();
    if num.isdigit():
        if num==0:
            print('请在NUM.txt中修改！')
        else:
            m = 0
            while m < int(num):
                m = m + 1
                invitecode = get_invietecode()
                if p_main(invitecode,user,pass1,token2):
                    print(invitecode+'--邀请成功：'+str(m)+'次！--')
                    print('-'*50)
    else:print('Num.txt不是整数！')

if __name__ == '__main__':
    main()
