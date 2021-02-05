from os import system
system('pip install requests')
print('=========\n\n')
print("""
           #----------------------------------------------------------#
           
                      # --------  Checker ------- #
                         
                -- By : HassanGamer555 - YouTube : Hassan Gamer 555 --
              
             ---------------------------------------------------------
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
                'username':input('[ HassanGamer555 ] اكتب اسم المستخدم :-'),
                'password':input('[ HassanGamer555 ] اكتب كلملة المرور :- '),
                'device_id':str( uuid4() )
        }
 
        global log
 
        log = browser.post("https://i.instagram.com/api/v1/accounts/login/",data=data, headers={'User-Agent': u}).text
 
        if 'logged_in_user' in log:
                session_id = browser.cookies.get_dict()['sessionid']
                csr = browser.cookies.get_dict()['csrftoken']
 
        else:
 
                if input('❌ حاول مجدداً ? y/n : ') == 'y':
                        print(log)
                login()
 
login()             
 
 
num = int(input('[ HassanGamer555 ] كم تريد عدد اسماء المستخدمين للتجربة ? (1-400): '))
 
print ('\n------------جاري التجربة------------\n') 

for _ in range(num):
        user = get_random_acc()
        source = get(f'https://www.instagram.com/{user}',headers = {'x-csrftoken':csr},cookies={'sessionid':session_id}).text
 
        if 'href="/static/bundles/es6/HttpErrorPage.js' in source:
                print(f'✅ {user}: متوفر')
                Available= open('Available.txt','a')
                Available.write(user+'\n')
                Available.close()
        else:
                print(f'❌ {user}: غير متوفر')
 
input('✅ اكتمل!\nاضغط Enter للاغلاق.. ')