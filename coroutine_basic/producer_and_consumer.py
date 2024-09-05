# 问题4：生产者-消费者模式
# 实现一个简单的生产者-消费者模型。生产者异步生成数据并放入队列中，消费者从队列中异步获取数据并处理。
# 确保生产者和消费者能够并发运行，并在所有数据处理完毕后正确退出。
import asyncio

products = asyncio.Queue()


async def product_prod():
    for _ in range(5):
        print("Producing a product...")
        await asyncio.sleep(0.3)
        await products.put("prod")
        print("Product produced")


async def cost_prod():
    for _ in range(5):
        print("Consuming a product...")
        await asyncio.sleep(0.3)
        product = await products.get()
        print(f"Product consumed: {product}")
        products.task_done()


async def main():
    producer = asyncio.create_task(product_prod())
    consumer = asyncio.create_task(cost_prod())

    await asyncio.gather(producer, consumer)
    await products.join()  # Ensure all products are consumed

asyncio.run(main())
