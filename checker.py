from os import system
system('pip install requests')
print('============ YouTube : HassanGamer555 ============\n\n')
print("""      
┏━━┓╋╋╋╋╋┏┓
┗┫┣┛╋╋╋╋┏┛┗┓
╋┃┃┏━┓┏━┻┓┏╋━━┳━━┳━┳━━┳┓┏┓
╋┃┃┃┏┓┫━━┫┃┃┏┓┃┏┓┃┏┫┏┓┃┗┛┃
┏┫┣┫┃┃┣━━┃┗┫┏┓┃┗┛┃┃┃┏┓┃┃┃┃
┗━━┻┛┗┻━━┻━┻┛┗┻━┓┣┛┗┛┗┻┻┻┛
╋╋╋╋╋╋╋╋╋╋╋╋╋╋┏━┛┃
╋╋╋╋╋╋╋╋╋╋╋╋╋╋┗━━┛
┏┓╋┏┓
┃┃╋┃┃
┃┃╋┃┣━━┳━━┳━┳━┓┏━━┳┓┏┳━━┓
┃┃╋┃┃━━┫┃━┫┏┫┏┓┫┏┓┃┗┛┃┃━┫
┃┗━┛┣━━┃┃━┫┃┃┃┃┃┏┓┃┃┃┃┃━┫
┗━━━┻━━┻━━┻┛┗┛┗┻┛┗┻┻┻┻━━┛
┏━━━┳┓╋╋╋╋╋╋╋┏┓
┃┏━┓┃┃╋╋╋╋╋╋╋┃┃
┃┃╋┗┫┗━┳━━┳━━┫┃┏┳━━┳━┓
┃┃╋┏┫┏┓┃┃━┫┏━┫┗┛┫┃━┫┏┛
┃┗━┛┃┃┃┃┃━┫┗━┫┏┓┫┃━┫┃
┗━━━┻┛┗┻━━┻━━┻┛┗┻━━┻┛
┏━━━┓╋╋╋╋┏┓
┃┏━┓┃╋╋╋╋┃┃
┃┃╋┃┣━┳━━┫┗━┳┳━━┓
┃┗━┛┃┏┫┏┓┃┏┓┣┫┏━┛
┃┏━┓┃┃┃┏┓┃┗┛┃┃┗━┓
┗┛╋┗┻┛┗┛┗┻━━┻┻━━┛
𝗕𝘆 𝗛𝗮𝘀𝘀𝗮𝗯𝗚𝗮𝗺𝗲𝗿𝟱𝟱𝟱
                                                """)
from time import sleep,time,strftime
from requests import get,post,session
from uuid import uuid4
import string
import random
 
 
browser = session()
u = 'Instagram 123.1.0.26.114 (iPhone8s)'
 
 
def get_random_acc():
    # Random string with the combination of lower and upper case
    letters = string.ascii_letters
    return ''.join(random.choice(letters).lower() for i in range(4))
 
 
def login():
        global data,session_id,csr
 
        data = {
                'username':input('[ YouTube:HassanGamer555 ] ﻡﺪﺨﺘﺴﻤﻟﺍ ﻢﺳﺍ ﺐﺘﻛﺍ :- '),
                'password':input('[ YouTube:HassanGamer555 ] ﺭﻭﺮﻤﻟﺍ ﺔﻤﻠﻛ ﺐﺘﻛﺍ :- '),
                'device_id':str( uuid4() )
        }
 
        global log
 
        log = browser.post("https://i.instagram.com/api/v1/accounts/login/",data=data, headers={'User-Agent': u}).text
 
        if 'logged_in_user' in log:
                session_id = browser.cookies.get_dict()['sessionid']
                csr = browser.cookies.get_dict()['csrftoken']
 
        else:
 
                if input('❌  ًﺍﺩﺪﺠﻣ ﻝﻭﺎﺣ ? y/n : ') == 'y':
                        print(log)
                login()
 
login()             
 
 
num = int(input('[ YouTube:HassanGamer555 ] ﺔﺑﺮﺠﺘﻠﻟ ﻦﻴﻣﺪﺨﺘﺴﻤﻟﺍ ﺀﺎﻤﺳﺍ ﺩﺪﻋ ﺪﻳﺮﺗ ﻢﻛ ? (1-400) : '))
 
print ('\n------------ﺔﺑﺮﺠﺘﻟﺍ ﻱﺭﺎﺟ------------\n') 

for _ in range(num):
        user = get_random_acc()
        source = get(f'https://www.instagram.com/{user}',headers = {'x-csrftoken':csr},cookies={'sessionid':session_id}).text
 
        if 'href="/static/bundles/es6/HttpErrorPage.js' in source:
                print(f'✅ {user} : ﺮﻓﻮﺘﻣ')
                Available= open('Available.txt','a')
                Available.write(user+'\n')
                Available.close()
        else:
                print(f'❌ {user} : ﺮﻓﻮﺘﻣ ﺮﻴﻏ')
 
input('✅ ﻞﻤﺘﻛﺍ!\nﻂﻐﺿﺍ Enter ﻕﻼﻏﻼﻟ..')
