# test_task_video_analytic_tg_bot

# Установка
- `docker compose up -d ollama`
- `docker compose exec ollama ollama pull llama3.1`

# History

- Установил основные зависимости
- LLM стянул llama2:13b-chat для ollama
- Базово описал таблицы
- Развернул docker compose для postgres
- Добавил миграции
- Добавил .env файл
- Добавил /start у бота
- добавил в зависимости langchain
- запулил llama3.1