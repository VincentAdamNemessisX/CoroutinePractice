# app.py --- 初始化celery对象
from celery import Celery
from task import test_one

celery = Celery(__name__, include=["task"])  # 设置需要导入的模块
# 引入配置文件
celery.config_from_object(seting)

if __name__ == '__main__':
    test_one.apply_async(
        (2, 2),  # 传入参数
        routing_key='default', # 指定队列
        priority=0, # 优先级
        exchange='default' # 交换机
    )

# task.py  --- 定义需要执行的任务
from app import celery


@celery.task
def test_one(x, y):
    return x + y


@celery.task(name="one_name")
def test_two(x, y):
    return x * y
