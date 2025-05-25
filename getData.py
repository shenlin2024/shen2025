import requests
import json
from dbUtil import db
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    ,"referer":"https://www.zhipin.com/web/geek/jobs?city=101010100&query=java"
    ,"cookie":"ab_guid=f9d51169-710e-4075-ae69-ff103fabf9e3; wt2=D1ii1V5R96mJkgNRIb7sandSRdyQ24fuloXwXgQ2Ld0bcibp4rJ54YAdmoSypQGSbgurSQkZlzp0dpcGyFx6GLg~~; wbg=0; zp_at=Yr6KnU5YaTFtZ4odtvRSNM6ffGDqVITZGzv0zeFHj1o~; __g=-; __zp_stoken__=15d6fMzjDm8KxwpjCuEUoCgsBFgw6KDQ4LzpAMyRHPjwzODE0RjM4OR44I8SFwrgXTgJnw47CqcK4Mi0xPkAzOEc%2BP0YdMTrEscK0MTgSwonCsglID2DDhD84DcO%2BwrQDw5%2FCsV07wrECY8K%2FLiLCgcKxODRHPsK9wr3ClMK8wrLCtMKYw4fCs8KzwpHCuzQ%2FPjEqOBUMDw04P01IXQ5NWUFnXEkEUElVLT46PjPDq8Ohw7EsMRUMCwoWDw4BCAQDAg0NAQEIDw4CAwINBAgwMcKZwrjDpMKUxILCr8Saxa7DlsKpxILDocWAxIbDg8KJw6vDuMOqwozFgMKWw4TCq8OSwqzDkMKvw5%2FCkMOZwpzDmcKmxL5Qw6vCo8OCwrjCiE3Cm8KIw77CqMKTw4fDusKEwpPCucKswpjCjsKfw7lPwqVOw77CkcOFXcKEwrdVwqvCmWBEwrjCgcOGwqBOwpJOwrhEwqTChsK7VMK2T2RpwqjDhUnCtMKHwoBvcl4KWRcENFguJsOB; bst=V2R9IuFuH_21hrVtRuyxUfKCOw7Drfwi8~|R9IuFuH_21hrVtRuyxUfKCOw7DrSwig~; __c=1748135527; __l=l=%2Fwww.zhipin.com%2Fweb%2Fgeek%2Fjobs%3Fcity%3D101010100%26query%3Djava&r=&g=&s=3&friend_source=0&s=3&friend_source=0; __a=46160719.1747831559.1748011035.1748135527.26.5.11.26"
}
job = input("请输入查询的工作:")
citya = input("请输入查询的地点:")
cityDic = {"全国":"100010000","南昌":"101240100","北京":"101010100",
           "上海":"101020100","广州":"101280100","深圳":"101280600",
"杭州":"101210100","天津":"101030100","西安":"101110100",
"苏州":"101190400","武汉":"101200100","厦门":"101230200",
"长沙":"101250100","成都":"101270100","郑州":"101180100"
           }
city = cityDic.get(citya,"100010000")
url = "https://www.zhipin.com/wapi/zpgeek/search/joblist.json?scene=1&query="+job+"&city="+city+"&experience=&payType=&partTime=&degree=&industry=&scale=&stage=&position=&jobType=&salary=&multiBusinessDistrict=&multiSubway=&page=1&pageSize=100&_=1741750103962"
resp = requests.get(url, headers=headers)
text = json.loads(resp.content.decode())
print(text)
# 获取数据
data = text["zpData"]["jobList"]
# 获取操作数据的对象
cursor = db.cursor()
for i in data:
    sql = '''
        insert into s_job values
        (null,'%s','%s','%s','%s','%s','%s')
    '''%(i["cityName"],i["brandName"],i["jobName"],i["jobDegree"],
         i["jobExperience"],i["salaryDesc"])
    try:
        cursor.execute(sql) # 执行sql
        db.commit() #提交数据
    except:
        print("数据有问题")
        db.rollback()