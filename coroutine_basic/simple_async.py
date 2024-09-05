# 问题1：简单的异步任务
# 编写一个简单的异步函数，模拟一个耗时的I/O操作（例如，使用asyncio.sleep），
# 并在多个协程中并发执行它们。计算并打印所有任务完成所需的总时间。
import asyncio
import time

x = 1


async def mock_io():
    # mock I/O takes time
    await asyncio.sleep(0.1)
    global x
    x *= 5


async def main():
    s_t = time.time()
    await asyncio.gather(mock_io(), mock_io(), mock_io(), mock_io(), mock_io())
    print(x)
    print(f"takes {time.time() - s_t}ms")


asyncio.get_event_loop().run_until_complete(main())
