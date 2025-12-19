import asyncio
from .bot.core import main
from .logger import logger

if __name__ == '__main__':
    if logger:
        pass
    asyncio.run(main())
