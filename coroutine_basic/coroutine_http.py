# 问题2：异步HTTP请求
# 使用aiohttp库编写一个异步函数，向多个URL发送HTTP GET请求，并并发地获取它们的响应。
# 将每个响应的状态码和内容长度打印出来。

import asyncio
import time

import aiohttp


async def fetch_res(url: str):
    async with aiohttp.ClientSession() as session:
        return await session.get(url=url)


async def main():
    tasks = [fetch_res("https://baidu.com") for _ in range(10)]
    for res in asyncio.as_completed(tasks):
        time.sleep(1)
        print(await res)


asyncio.run(main())
