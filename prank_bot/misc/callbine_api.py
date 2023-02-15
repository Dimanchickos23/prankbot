import aiohttp
import requests
#https://callbine.ru/app/?action=apiaccess

CALLBINE_API_KEY = '083a968c-8fe1-50e8-8cdc-61d625eb'


async def get(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

requests.post()
