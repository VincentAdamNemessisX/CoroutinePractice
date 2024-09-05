# 问题3：任务取消
# 编写一个异步函数，模拟一个长时间运行的任务（例如，使用asyncio.sleep）。
# 在运行一段时间后，取消该任务，并处理取消异常，确保程序能够优雅地退出。
import asyncio
import time


async def mock_long_task():
    try:
        await asyncio.sleep(5)
    except asyncio.CancelledError:
        print("task canceled")


async def main():
    t_s = time.time()
    long_task = asyncio.create_task(mock_long_task())  # if only create task, it almost takes 0 sec
    await asyncio.sleep(1)
    if time.time() - t_s >= 1:
        long_task.cancel()
    await long_task


asyncio.run(main())
