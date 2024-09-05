# 问题6：异步数据库操作
# 使用aiomysql或asyncpg库或aiosqlite，编写一个异步函数，连接到数据库并执行简单的查询操作。
# 确保查询操作是异步执行的，并处理可能的异常。
import asyncio
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlmodel import SQLModel, Field


class Item(SQLModel, table=True):
    __tablename__ = "item"
    name: str = Field(nullable=True, primary_key=True)
    desc: str = Field()


engine = create_async_engine(url="sqlite+aiosqlite:///./test.sqlite3")


async def get_db():
    async with AsyncSession(engine) as session:
        yield session


async def get_something(session):
    async for s in session:
        # s.add(Item(name="bug", desc="bugfx"))
        # await s.commit()
        return await s.get(Item, "bug")


async def main():
    rs = await get_something(get_db())
    print(rs)


asyncio.run(main())
