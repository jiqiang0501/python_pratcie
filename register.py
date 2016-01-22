#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib
import urllib2
import json

import urllib2
from cookielib import CookieJar
loginUrl = 'http://210.51.17.146:7340/serviceAgent/rest/users/register'
headers = {
    'Content-Type': 'application/json; charset=gb2312',
	'User-Agent': 'Dalvik/1.6.0 (Linux; U; Android 4.1.1; M040 Build/JRO03H)',
    'Host': '210.51.17.146:7340',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
    'Content-Length': '251',
	'appId': 'MB-DEVELOPERSITE-0000',
	'sequenceId': '20160114174011000001',
    }
	
values = {
	"password":"11111111",
	"user": {
		"userBase": {
			"loginName":"hive2",
			"email":"guwn531@163.com",
			"mobile":"13456565656",
			"accType": 99
		},
		"userProfile": {
			"nickName":"Hive3",
			"userName":"Hive3",
			"points":"0",
			"focusCount":"0",
			"followCount":"0"
		}
	}
}

postdata = json.JSONEncoder().encode(values)
cookieJar = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))
req = urllib2.Request(loginUrl, postdata, headers)
loginResult = opener.open(req).read()
#loginResult.encode('gb2312')
print loginResult.decode('utf-8').encode('gb18030')

