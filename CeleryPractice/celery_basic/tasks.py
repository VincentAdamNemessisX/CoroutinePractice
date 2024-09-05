from celery import Celery

# broker="amqp://guest:guest@127.0.0.1:5672/team",  # middle task team
app = Celery(
    "tasks",
    broker="redis://127.0.0.1:6379/1",
    backend="redis://127.0.0.1:6379/2",  # final result storage
    broker_connection_retry_on_startup=True,
)

app.conf.update(
    task_serializer='json',  # 任务消息序列化方式
    result_serializer='json',  # 任务结果序列化方式
)
# 在 Celery 应用配置中设置并发参数
app.conf.update(
    worker_concurrency=4,  # 同时执行的工作进程数量
    task_max_retries=3,  # 单个任务的最大执行次数（重试次数）
)

app.conf.beat_schedule = {
    'my-periodic-task': {
        'task': 'test',  # 执行的任务
        'schedule': 10,  # 每1秒执行一次
    },
}


@app.task(name="test")
def my_periodic_task():
    print("test1111111")
