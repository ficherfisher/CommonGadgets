import asyncio
import aiohttp
import time


def test(number):
    start = time.time()

    async def get(url):
        session = aiohttp.ClientSession()
        response = await session.get(url)
        await response.text()
        await session.close()
        return response

    async def request():
        url = 'https://www.baidu.com'
        await get(url)

    tasks = [asyncio.ensure_future(request()) for i in range(number)]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    end = time.time()
    print("number", number, "cost time", end - start, "avg", (end - start) / number)


if __name__ == "__main__":
    for i in [1, 5, 10, 100, 500, 1000]:
        test(i)











