let cookiesArr = [],
    cookie = '';
if ($.isNode()) {
    Object.keys(jdCookieNode).forEach((item) => {
        cookiesArr.push(jdCookieNode[item])
    })
} else {
    cookiesArr.push($.getdata('CookieJD'));
    cookiesArr.push($.getdata('CookieJD2'));
}
const JD_API_HOST = 'https://api.m.jd.com/client.action';
!(async() => {
    if (!cookiesArr[0]) {
        $.msg($.name, '【提示】请先获取京东账号一cookie\n直接使用NobyDa的京东签到获取', 'https://bean.m.jd.com/', { "open-url": "https://bean.m.jd.com/" });
        return;
    }
    for (let i = 0; i < cookiesArr.length; i++) {
        if (cookiesArr[i]) {
            cookie = cookiesArr[i];
            $.UserName = decodeURIComponent(cookie.match(/pt_pin=(.+?);/) && cookie.match(/pt_pin=(.+?);/)[1])
            console.log(`\n===============开始【京东账号${$.index}】${$.UserName}==================\n`);
            $.errorMsg = '';
            await bc_taskList();
        }
    }
})()
.catch((e) => {
        $.log('', `❌ ${$.name}, 失败! 原因: ${e}!`, '')
    })
    .finally(() => {
        $.done();
    })

function getNewslinteractionInfo() {
    return new Promise(resolve => {
        $.get(taskUrl('getNewslinteractionInfo'), async(err, resp, data) => {
            try {
                if (err) {
                    console.log(`${JSON.stringify(err)}`)
                    console.log(`${$.name} API请求失败，请检查网路重试`)
                } else {
                    if (data) {
                        $.homeData = JSON.parse(data);
                        console.log(data);
                    } else {
                        console.log(`京东服务器返回空数据`)
                    }
                }
            } catch (e) {
                $.logErr(e, resp)
            } finally {
                resolve();
            }
        })
    })
}

function taskUrl(function_id, body = {}) {
    return {
        url: `${JD_API_HOST}&functionId=${function_id}&clientVersion=8.0.0&client=m&body=${escape(JSON.stringify(body))}`,
        headers: {
            'Origin': `https://h5.m.jd.com`,
            'Cookie': cookie,
            'Connection': `keep-alive`,
            'Referer': `https://h5.m.jd.com/babelDiy/Zeus/WgmkHMiiV1JUtcrZAUZTbL3hQss/index.html`,
            'Host': 'api.m.jd.com',
            'Accept-Encoding': `gzip, deflate, br`,
            'Accept-Language': `zh-cn`,
            'Content-Type': `application/x-www-form-urlencoded`,
            'User-Agent': `Mozilla/5.0 (iPhone; CPU iPhone OS 14_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Mobile/15E148 Safari/604.1;`

        }
    }
}