import asyncio
import requests


async def callasync():
    loop = asyncio.get_event_loop()
    url = 'https://webhook.site/9b7d5a9b-c1d0-4997-9f78-1a7941190e96'
    loop_count = 3
    futures = [loop.run_in_executor(None, requests.get, url) for i in range(loop_count)]
    for response in await asyncio.gather(*futures):
        print(response.headers['Date'])

asyncio.get_event_loop().run_until_complete(callasync())
