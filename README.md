# P++

准备工作：
1.一台部署了ubuntu 18.04系统的VPS
2.可以使用简单的SHELL命令符
手残认识不建议继续往下看！！

运行环境
python 3.7

1.Ubuntu系统安装python3.7，详细教程请参考：
https://blog.csdn.net/bz0446/article/details/105500585

2.安装Chrome和chromedrive,详细教程请参考：
https://blog.csdn.net/shuchuan0409/article/details/101615221?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.control&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.control

3.下载源码：
git clone git@github.com:U188/PJJ.git

如果无法git  请参考：https://blog.csdn.net/YanceChen2013/article/details/82218356

4.安装依赖:
pip install -r requirements.txt

6.运行
nohup python3.7 -u main.py >log .log 2>&1 &
nohup python3.7 -u run.py >log .log 2>&1 &


7.API使用
http://location:5000/pjj/user=联众账号pass=联众密码invitecode=邀请码   （提交各项信息）
http://location:5000/invitecode    (提交情况）
http://location:5000/invite_log    (完成情况）
http://location:5000/log1          (运行情况）








然后GIT
