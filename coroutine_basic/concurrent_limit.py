# 问题7：并发限制
# 编写一个异步函数，使用asyncio.Semaphore来限制并发任务的数量。
# 例如，限制同时进行的HTTP请求数量，确保不会超出限制。

import asyncio

import aiohttp

max_concurrent = asyncio.Semaphore(1)


async def fetch_rs(url: str):
    async with aiohttp.ClientSession() as cs, max_concurrent:
        return await cs.get(url=url)


async def work(queue):
    while not queue.empty():
        task = await queue.get()
        try:
            result = await task
            print(result)
        finally:
            queue.task_done()


async def main():
    # tasks = asyncio.Queue()
    # for i in range(15):
    #     await tasks.put(fetch_rs("https://baidu.com"))
    # max_concurrent = 10
    # workers = [asyncio.create_task(work(tasks)) for _ in range(max_concurrent)]
    # await tasks.join()  # 等待所有任务完成
    # for worker in workers:
    #     worker.cancel()  # 取消所有worker任务
    tasks = [fetch_rs(url="https://baidu.com") for _ in range(15)]
    for res in asyncio.as_completed(tasks):
        print(await res)


asyncio.run(main())
