import abc
import requests
import aiohttp
import asyncio


class AbstractIotApi(abc.ABC):
    @abc.abstractmethod
    def get(self, url, **kwargs):
        raise NotImplementedError

    @abc.abstractmethod
    def post(self, url, data=None, **kwargs):
        raise NotImplementedError


class SyncIotApi(AbstractIotApi):
    def get(self, url, **kwargs):
        return requests.get(url, **kwargs)

    def post(self, url, data=None, **kwargs):
        return requests.post(url, data, **kwargs)


class AsyncIotApi(AbstractIotApi):
    async def get(self, url, **kwargs):
        async with aiohttp.ClientSession() as session:
            async with session.get(url, **kwargs) as response:
                return await response.text()

    async def post(self, url, data=None, **kwargs):
        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=data, **kwargs) as response:
                return await response.text()


if __name__ == '__main__':
    config_use_async = True  # 或從設定檔載入
    client = AsyncIotApi() if config_use_async else SyncIotApi()

    # 使用同步客戶端
    if not config_use_async:
        response = client.get('http://example.com')
        print(response.text)

    # 使用非同步客戶端
    else:
        loop = asyncio.get_event_loop()
        response = loop.run_until_complete(client.get('http://example.com'))
        print(response)