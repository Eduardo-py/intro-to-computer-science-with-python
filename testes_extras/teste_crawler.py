# from bs4 import BeautifulSoup
# import requests
 
# url = "https://www.linkedin.com/in/ezefranca"
 
# # Getting the webpage, creating a Response object.
# response = requests.get(url)
 
# # Extracting the source code of the page.
# data = response.text
 
# # Passing the source code to BeautifulSoup to create a BeautifulSoup object for it.
# #soup = BeautifulSoup(data, 'lxml')
# print(data) 
# # Extracting all the <a> tags into a list.
# #tags = soup.find_all('a')
 
# # Extracting URLs from the attribute href in the <a> tags.
# #for tag in tags:
# #    print(tag.get('href'))
import requests

cookies = {
    '$uuid2': '184102770358913852',
    'icu': 'ChgI0bwwEAoYASABKAEwz7fY0gU4AUABSAEQz7fY0gUYAA..',
    'sess': '1',
    'anj': 'dTM7k!M4/YDZ3#YF\']wIg2GU$eqbYd!nN-V3)2H2jLM68*uoI-En5DTBj<hH.^n7PRx(WKjpO4w%UyU@3Xk1ibQ`2fIa/ooTsCfWiF\'Gd!k0MROuuX2ONtI6NO#6f+c=GhuNqA2J(XUUY)_9RK.+cukMISolQIkp:m8L+<%i6bVu^Pe0YA`rD(mj-B3dz\'qN<1uW:qQdkk7x!>#CwBBuw%CL8wm#Z+8e^WO5!lBx2Vhg4$1mRB)NpJJFr*t167aOC^yR`k-ffQ/nV#SfIIx]ezoH3Q9@o3P635-$Z>34GfJ:/?)bADmXS+9pbxf)M.<fBsbo8#)sVG/Y9XUEJm*njHy1ze(\'oUF0<79?hNnTnX73sGp]Yf08N%s2i6M8)F=hC#2E<o4zr*FYKSg:o!?REo5ABU!yzC6Yf4R2+l?C]7=Up4]BmI#gibOQtC2s?%b=S2dKi#gT8Rh#2FzIf>#+J(dS`9[TBbSU=<qMRC%+<9jkK#-F*b$[wFL`gu0_BT-$dD4:4PYrA^Fb>%pu_mx1Gt4k<?yd3R6T4.%g#U!Ok^KrndM<lmn!DBb^u1]Mvl9>/+r.OkPn:R2cQV=meh-J^/0wT)#w$izrY(>#)cfh00CdN?sxhjlWX2QhIF7Qvh%6[mVU_gvG4m%>W=qDnm/*(xq1V=3r3nXnry(YqlV5T+#\'lHj]uD%VGKA-%(o)$H)Ia23$)#%nug>*L6AK',
}

headers = {
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,pt;q=0.8',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
    'accept': '*/*',
    'authority': 'www.linkedin.com',
    'cookie': 'JSESSIONID=ajax:2792013909897240625; bcookie="v=2&7cc7ceec-bb1b-4b2d-8de2-a2b398ab26e1"; bscookie="v=1&201801111743506d27bdd7-3910-4064-87d9-770f983f7118AQG_f5axNtc8n-cE0EhSxpq-KPzV4kWn"; lidc="b=VGST00:g=658:u=1:i=1515692630:t=1515779030:s=AQH0J1UpfYQJeyyNrTRtRXcPPEUUZ200"; _ga=GA1.2.1525272826.1515692631; visit="v=1&G"; lang="v=2&lang=en-us"; _gid=GA1.2.105297552.1515692643; join_wall=v=2&AQEpe8a3fYpXJwAAAWDmU1u51awGEgUbA6MZwIVH8w5iVjetdDXjub5bFRfo1-bzYn_cQVfY1EbnPUkXvPEZE-ETVrlurPWOZo0mOdECOO08oOcw9-uh9p0_Nx7E2f_Bj05DFBU; leo_auth_token="GST:873qnJn0wtqAHC4vE29fWnFgT2cfNMO-8u3InlFQwI2qVCbBwY-mRY:1515692712:38d21d8e4da396e494237c451df8b439415238bd"',
    'Referer': 'https://radar.cedexis.com/1515620938/radar.html?customer-id=11326',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
    'Origin': 'https://radar.cedexis.com',
    'origin': 'https://www.linkedin.com',
    'content-type': 'application/json',
    'referer': 'https://www.linkedin.com/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,pt;q=0.8',
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'csrf-token': 'ajax:2792013909897240625',
    'x-isajaxform': '1',
    'Content-Type': 'text/plain;charset=UTF-8',
    'Cache-Control': 'max-age=0',
    'Content-Length': '0',
}

data = [
  ('plist', '{"totalTime":1437,"dnsTime":0,"connectTime":0,"firstByteTime":770,"pageDownloadTime":156,"frontendTime":446,"navigationTimingApi":true,"serverStartTime":1515692711064,"treeId":"yrNuan3SCBUAYvAmqisAAA==","pageKey":"public_profile_v3_desktop","boomerangStart":1515692712074,"boomerangEnd":1515692712075,"redirectCount":0,"navigationType":0,"navigationStart":1515692710600,"unloadEventStart":0,"unloadEventEnd":0,"redirectStart":0,"redirectEnd":0,"fetchStart":1515692710624,"domainLookupStart":1515692710624,"domainLookupEnd":1515692710624,"connectStart":1515692710624,"connectEnd":1515692710624,"requestStart":1515692710630,"responseStart":1515692711394,"responseEnd":1515692711550,"domLoading":1515692711432,"domInteractive":1515692711958,"domContentLoadedEventStart":1515692711958,"domContentLoadedEventEnd":1515692711958,"domComplete":1515692711996,"loadEventStart":1515692711996,"loadEventEnd":1515692712037,"timeDone":1483,"timePage":689,"timeResponse":794,"timeSource":"navigation","isSSL":1,"usedCDN":{"static_domain":"static-exp2.licdn.com","media_domain":"media-exp2.licdn.com","media-exp2.licdn.com":"unknown","static-exp2.licdn.com":"ecst"},"pointOfPresenceId":"prod-edc2","rawXLiFabricHeader":"prod-lva1","resourceTiming":{"jsTime":59,"jsCount":11,"cssTime":22,"cssCount":2,"sImgTime":46,"sImgCount":11,"mImgTime":0,"mImgCount":0,"sDnsTime":0,"mDnsTime":0},"nativeTimings":[],"trackingClientTimestampMs":1515692712082}'),
]

response = requests.post('https://www.linkedin.com/in/ezefranca', headers=headers, cookies=cookies, data=data)

print(response.text)