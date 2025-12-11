from sqlalchemy.ext.asyncio import create_async_engine


DATABASE_URL = "postgresql+asyncpg://user:pass@localhost:5432/mydb"
DATABASE_URL_TEST = DATABASE_URL + "_test"

async_engine = create_async_engine(DATABASE_URL)
async_engine_test = create_async_engine(DATABASE_URL_TEST)