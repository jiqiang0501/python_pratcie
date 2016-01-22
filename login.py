#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib
import urllib2
import json

import urllib2
from cookielib import CookieJar
loginUrl = 'http://210.51.17.146:7340/serviceAgent/rest/security/userlogin'
headers = {
    'Content-Type': 'application/json; charset=utf-8',
	'User-Agent': 'Dalvik/1.6.0 (Linux; U; Android 4.1.1; M040 Build/JRO03H)',
    'Host': '210.51.17.146:7340',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
    'Content-Length': '173',
	'appId': 'MB-DEVELOPERSITE-0000',
	'sequenceId': '20160114174011000001',
	'appKey': '6EC2E68669260E5C9129DB2A4C8C676B',
	'appVersion': '10.01.11.00025',
	'clientId': '356877020056553-08002700DC94',
    }
	
values = {
	"sequenceId":"20160120112000000001",
	"accType": "99",
	"loginId":"14759167292",
	"password":"123456",
	"thirdpartyAppId":"",
	"thirdpartyAccessToken":"",
	"loginType":"1"
}

postdata = json.JSONEncoder().encode(values)
cookieJar = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))
req = urllib2.Request(loginUrl, postdata, headers)
loginResult = opener.open(req).read()
#loginResult.encode('gb2312')
print loginResult.decode('utf-8').encode('gb18030')

