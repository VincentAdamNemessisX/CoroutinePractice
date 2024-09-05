# 问题5：超时处理
# 编写一个异步函数，使用asyncio.wait_for来设置一个超时时间。
# 如果任务在超时时间内没有完成，则抛出超时异常并处理它。
import asyncio
import warnings


async def time_task():
    await asyncio.sleep(0.5)


async def main():
    try:
        await asyncio.wait_for(time_task(), 0.5)
    except TimeoutError:
        warnings.warn("Function takes too much time to execute.")

asyncio.run(main())
