import asyncio

from sqlalchemy import text
from sqlalchemy.ext.asyncio import async_sessionmaker

from src.db.engine import async_engine as engine

import re

MyAsyncSession = async_sessionmaker(bind=engine, expire_on_commit=False)

async def get_db_schema() -> str:
    """Возвращает текстовое описание схемы БД"""
    async with MyAsyncSession() as session:
        result = await session.execute(text("""
            SELECT table_name, column_name, data_type, is_nullable
            FROM information_schema.columns 
            WHERE table_schema = 'public'
            ORDER BY table_name, ordinal_position;
        """))

        tables = {}
        for row in result:
            table, col, dtype, nullable = row
            if table not in tables:
                tables[table] = []
            tables[table].append(f"{col} ({dtype} {'NULL' if nullable else 'NOT NULL'})")

        schema_text = "\n".join([
            f"📋 Таблица '{table}': {', '.join(cols)}"
            for table, cols in tables.items()
        ])
        return schema_text


DANGEROUS_WORDS = {'delete', 'drop', 'update', 'insert', 'alter', 'create', 'truncate'}


def is_safe_sql(sql: str) -> bool:
    sql_lower = sql.lower()
    return not any(word in sql_lower for word in DANGEROUS_WORDS)


def safe_execute(sql: str, session):
    if not is_safe_sql(sql):
        raise ValueError("🚫 Опасный SQL!")

    # Только SELECT
    if not sql.strip().upper().startswith('SELECT'):
        raise ValueError("🚫 Только SELECT запросы!")

    return session.execute(text(sql + " LIMIT 100"))

async def main():
    r = await get_db_schema()
    print(r)

if __name__ == '__main__':

    asyncio.run(main())
