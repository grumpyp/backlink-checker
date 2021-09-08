import requests
import time


headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}


print("---initialize")
not_found = []
to_check = open('data.txt', 'r+')
for check in to_check.read().splitlines():
    do_check = check.split(',')
    print("---checking ", do_check[0])
    r = requests.get(do_check[0], headers=headers)
    if do_check[1] in r.text:
        print("---ok")
    else:
        not_found.append(do_check[0])
        print("---", do_check[1], " not found on ", do_check[0])
    time.sleep(1)
print(len(not_found), " Links nicht gefunden")
print("\n",not_found)