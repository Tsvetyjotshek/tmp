from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from data import config


class Database:

    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME
        )

    async def execute(self, command, *args,
                      fetch: bool = False,  #забирает всё
                      fetchval: bool = False, #забирает одно значение
                      fetchrow: bool = False, #забирает одну строчку
                      execute: bool = False #не возвращает никакие данные, а просто выполняет команды
                      ):
        async  with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    @staticmethod
    async def dobavit_otziv(self, review, id_cafe):
        sql = """INSERT INTO review(review_cafe, id_cafe) VALUES ($1, &2)"""
        return await self.execute(sql, review, id_cafe, execute=True)

    async def get_review(self, id_cafe):
        sql = """SELECT review_cafe FROM review WHERE id_cafe = $1"""
        return await self.execute(sql, id_cafe, fetchval=True)

    async def dobavit_estimation(self, id_cafe, estimation):
        sql = """INSERT INTO estimation(estimation_cafe) VALUES ($1)"""
        return await self.execute(sql, id_cafe, estimation, execute=True)

    async def get_estimation(self, id_cafe):
        sql = """SELECT AVG(estimation_cafe) as avg FROM estimation WHERE id_cafe = $1"""
        return await self.execute(sql, id_cafe, fetchval=True)

    async def get_cafe(self):
        sql = """SELECT name_cafe FROM kafe"""
        return await self.execute(sql, fetchval=True)

    async def get_menu(self, id_cafe):
        sql = """SELECT url_menu FROM kafe WHERE id_cafe = $1"""
        return await self.execute(sql, id_cafe, fetchval=True)


