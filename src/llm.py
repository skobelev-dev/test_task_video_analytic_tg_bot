import os

from langchain_ollama import ChatOllama
from src.logger import logger
print("here")
from src.db.utils import get_db_schema

base_url = os.getenv("OLLAMA_BASE_URL", "http://ollama:11434")
llm = OllamaLLM(
    model="llama3.1",  # Скачайте заранее: docker exec ollama ollama pull llama3.1
    base_url=base_url
)


def taking_the_ask(ask: str) -> str:
    logger.debug(msg=f"{ask=}")
    logger.info("The ask is ready to be asked")
    llm_response = llm.invoke(ask)
    content = llm_response.content
    logger.info("llm response is taken")
    logger.debug(f"{content=}")
    print(content)
    return content


SYSTEM_PROMPT = """
🔧 Ты SQL-эксперт для PostgreSQL. Преобразуй запросы НА РУССКОМ в SQL.

📊 СХЕМА БАЗЫ ДАННЫХ:
{table_schema}

⚠️ ПРАВИЛА (ОБЯЗАТЕЛЬНО):
1. ИСПОЛЬЗУЙ ТОЛЬКО таблицы/поля из схемы выше
2. ВСЕГДА добавляй LIMIT 100
3. НЕ используй DELETE/UPDATE/DROP/INSERT
4. Для дат: '2025-01-01' или NOW() - INTERVAL '1 day'
5. Русские тексты в БД как есть (не переводи)
6. Если не знаешь - верни "Не могу составить запрос"

📋 ФОРМАТ ОТВЕТА (СТРОГО):
SQL: SELECT ... LIMIT 100;

text

Пример:
Пользователь: "покажи пользователей"
Ответ:
SQL: SELECT * FROM users LIMIT 100;

text
"""

def build_prompt(question: str) -> str:
    schema = get_db_schema()
    return SYSTEM_PROMPT.format(table_schema=schema) + f"\n\n❓ Запрос: {question}"

if __name__ == '__main__':
    main()