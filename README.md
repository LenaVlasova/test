# test
<!-- Для создания виртуальной среды разработки -->
python -m venv venv
<!-- Для активации виртуальной среды (Windows)-->
venv\Scripts\activate.bat

<!-- Для запуска проверки работы (в ссылке на страницу дописываем /docs)-->
uvicorn test:app --reload


<!-- Для запуска миграции Alembic -->
alembic revision --autogenerate -m "Data"

<!-- Переходим в PgAdmin4, выбираем таблицы и прописываем команду-->
SELECT *FROM alembic_version;

<!-- В терминале VSCode пишем команду -->
alembic upgrade название_версии_присвоенное_после_команды_ (alembic revision --autogenerate -m "Data")

<!-- Далее в pgAdmin4 запускаем еще раз команду -->
SELECT *FROM alembic_version;

<!-- После этого обновляем таблицы, таким образом они отображаются в PgAdmin4 -->
