/**
来客有礼宠汪汪强制助力（助力一个好友可以获得30机会，一天上限是3好友，获得积分即90积分，不管助力是否成功，对方都会成为你的好友）
更新地址：https://raw.githubusercontent.com/lxk0301/scripts/master/jd_joy_help.js
更新时间：2020-08-26
目前提供了218位好友的friendPin供使用。助力成功后，退出小程序重写点击进去。
欢迎大家使用 https://jdjoy.jd.com/pet/getFriends?itemsPerPage=20&currentPage=1 (currentPage=1表示第一页好友，=2表示第二页好友)
提供各自账号列表的friendPin给我
如果想设置固定好友，那下载下来放到本地使用，可以修改friendPin换好友(助力一好友后，更换一次friendPin里面的内容)
感谢github @Zero-S1提供
使用方法：
①设置好相应软件的重写
②从京东APP宠汪汪->领狗粮->邀请好友助力，分享给你小号微信或者微信的文件传输助手。 自己再打开刚才的分享，助力成功后，退出小程序重新进去刚才分享的小程序即可

[MITM]
hostname = draw.jdfcloud.com
surge
[Script]
来客有礼宠汪汪强制助力= type=http-request,pattern=(^https:\/\/draw\.jdfcloud\.com\/\/pet\/enterRoom\?reqSource=weapp&invitePin=.*+(&inviteSource=task_invite&shareSource=\w+&inviteTimeStamp=\d+&openId=\w+)?|^https:\/\/draw\.jdfcloud\.com\/\/pet\/helpFriend\?friendPin),requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/lxk0301/scripts/master/jd_joy_help.js

圈x
[rewrite_local]
^https:\/\/draw\.jdfcloud\.com\/\/pet\/enterRoom\?reqSource=weapp&invitePin=.*+(&inviteSource=task_invite&shareSource=\w+&inviteTimeStamp=\d+&openId=\w+)?|^https:\/\/draw\.jdfcloud\.com\/\/pet\/helpFriend\?friendPin url script-request-header https://raw.githubusercontent.com/lxk0301/scripts/master/jd_joy_help.js

 LOON：
[Script]
http-request ^https:\/\/draw\.jdfcloud\.com\/\/pet\/enterRoom\?reqSource=weapp&invitePin=.*+(&inviteSource=task_invite&shareSource=\w+&inviteTimeStamp=\d+&openId=\w+)?|^https:\/\/draw\.jdfcloud\.com\/\/pet\/helpFriend\?friendPin script-path=https://raw.githubusercontent.com/lxk0301/scripts/master/jd_joy_help.js
 , requires-body=true, timeout=10, tag=来客有礼宠汪汪强制助力


下面提供了218位好友的friendPin，程序随机从里面获取一个
你也可从下面链接拿好友的friendPin(复制链接到有京东ck的浏览器打开即可)

https://jdjoy.jd.com/pet/getFriends?itemsPerPage=20&currentPage=1
**/
let url = $request.url
const friendsArr = ["jd_7da9924d92a2c", "jd_6fcfb7044255e"]

function randomFriendPin(m, n) {
    return Math.floor(Math.random() * (m - n) + n);
}
let friendPin = friendsArr[randomFriendPin(0, friendsArr.length - 1)] //强制为对方助力，有几率自动成为好友 (pin形如jd_xxxxxxxxx的几率大，其他的不会，原因未知)
friendPin = encodeURI(friendPin);
const timestamp = new Date().getTime()
newUrl = url.replace(/friendPin=.*?$/i, "friendPin=" + friendPin).replace(/invitePin=.*?$/i, "invitePin=" + friendPin).replace(/inviteTimeStamp=.*?$/i, "inviteTimeStamp=" + timestamp + "&")
console.log(newUrl)
$done({ url: newUrl })