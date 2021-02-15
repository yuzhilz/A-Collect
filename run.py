from selenium import webdriver
import lianzhong_api
import requests,json,time,os,random,re,choice
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import pyperclip
import pyautogui
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_experimental_option('useAutomationExtension', False)
def p_main(invitecode):
    try:
        email_random=random.randint(10000,99999)
        url2 = 'https://10minutemail.net/address.api.php?sessionid=76ade80fb2d3b0f9'+str(email_random)+'e8b0e93bbcb&_=1585393885861'
        r = requests.get(url2)
        if r.status_code == 200:
            result_json = r.json()
            email = result_json['mail_get_mail']
        url='https://pjj.one/share?userid='+invitecode
        #option = webdriver.ChromeOptions()
        #option.add_argument('headless')
        driver=webdriver.Chrome()
        driver.get(url)
        driver.implicitly_wait(3)
        #输入邮箱
        driver.find_element_by_xpath('//*[@id="app"]/section/main/div/div/div[2]/form/div[1]/div[2]/div/span/span/input').send_keys(email)
        #获取验证码url
        pic=driver.find_elements_by_xpath('//*[@id="app"]/section/main/div/div/div[2]/form/div[2]/div[2]/div/span/span/span/span/img')
        pic_urls = [i.get_attribute('src') for i in pic]  # 得到图片的urls 列表
        pic_names = [i.split('/')[-1:][0] for i in pic_urls]  # 得到图片的 图片名列表
        pic_root = os.path.abspath(os.path.dirname(os.getcwd()))  # 得到当前根目录的 上一级目录
        print(pic_root)
        image_file = os.path.join(pic_root, 'image')  # 新建一个文件夹 ，和当前项目同级目录
        if not os.path.exists(image_file):
            os.makedirs(image_file)
        pic_rejoin_path = [os.path.join(image_file, i) for i in pic_names]  # 新建
        #print(pic_rejoin_path)
        for i in range(len(pic)):
            actions = ActionChains(driver)
            # 找到图片后右键单击图片
            actions.move_to_element(pic[i])  # 定位到元素
            actions.context_click(pic[i])  # 点击右键
            actions.perform()  # 执行
            pyautogui.typewrite(['v'])  # v 是保存的快捷键
            time.sleep(1)  # 等待一秒
            pyperclip.copy(pic_rejoin_path[i])  # 把 指定的路径拷贝到过来
            time.sleep(1)  # 等待一秒
            pyautogui.hotkey('ctrlleft', 'v')  # 粘贴
            time.sleep(0.5)  # 等待一秒
            pyautogui.press('enter')
            time.sleep(0.5)  # 等待一秒
            #print("图片下载完成:%s" % pic_urls[i])
            time.sleep(1)
            im=pic_root+'//image//'+pic_names[0]+'.gif'
            s=lianzhong_api.main('lz378904298','zxc123@',im,'http://v1-http-api.jsdama.com/api.php?mod=php&act=upload','','','1008','d425c5c6135b7542c994bde770dfd340')
            code=s.json()['data']['val']
        driver.find_element_by_xpath('//*[@id="app"]/section/main/div/div/div[2]/form/div[2]/div[2]/div/span/span/span/input').send_keys(code)
        driver.find_element_by_xpath('//*[@id="app"]/section/main/div/div/div[2]/form/div[3]/div[2]/div/span/span/span/span/button').click()
        time.sleep(5)
        os.remove(im)
        url2 = 'https://10minutemail.net/address.api.php?sessionid=76ade80fb2d3b0f9'+str(email_random)+'e8b0e93bbcb&_=1585393885861'
        r = requests.get(url2).json()
        mail_id=r['mail_list'][0]['mail_id']
        mail_id_url='https://10minutemail.net//mail.api.php?mailid='+mail_id+'&sessionid=76ade80fb2d3b0f9'+str(email_random)+'e8b0e93bbcb'
        #print(mail_id_url)
        result=requests.get(url=mail_id_url).json()
        #print(result)
        yanzhenma=result['body'][1]['body']
        im_code=re.findall(r'(?<=验证码为 <b>).+(?=</b>，有效)', yanzhenma)
        #print(im_code)
        driver.find_element_by_xpath('//*[@id="app"]/section/main/div/div/div[2]/form/div[3]/div[2]/div/span/span/span/input').send_keys(im_code[0])
        driver.find_element_by_xpath('//*[@id="app"]/section/main/div/div/div[2]/form/div[4]/div[2]/div/span/span/input').send_keys('qwer1234')
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="app"]/section/main/div/div/div[2]/div/p[1]/button').click()
        time.sleep(1)
        driver.switch_to.frame("tcaptcha_iframe")
        driver.find_element_by_xpath('//*[@id="captcha_close"]/div').click()
        print('邀请成功1次！')
        time.sleep(2)
        driver.close()
    except:
        print('程序有错误，跳出！')
        driver.close()
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
    return invitecode.replace('\n','')
def main():
    # num=input('请输入次数：')
    m = 0
    while m < int(100):
        m = m + 1
        invitecode = get_invietecode()
        p_main(invitecode)

if __name__ == '__main__':
    main()
