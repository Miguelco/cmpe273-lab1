import requests


def callsynchronous():
    url = 'https://webhook.site/9b7d5a9b-c1d0-4997-9f78-1a7941190e96'
    loop_count = 3
    for n in range(loop_count):
        r = requests.get(url)
        print(r.headers['Date'])


callsynchronous()
