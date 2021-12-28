import requests

body = {
    "user":
    {
        "email_address": "XXXXXXXX@XXXX.COM",
        "password": "XXXXXXXXXX"
    }
}


url = 'XXXXXXXXXXXXXXXXx'
r_login = requests.post(url=url, json=body, timeout=3)

if r_login.ok is True:
    print('user was created')
else:
    print('nope!')
print(r_login.status_code)
