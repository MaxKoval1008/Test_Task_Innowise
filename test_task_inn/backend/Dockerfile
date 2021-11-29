# образ на основе которого создаём контейнер
FROM python:3.8.6-alpine

# рабочая директория внутри проекта
WORKDIR /usr/src/app

# переменные окружения для python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# устанавливаем зависимости
RUN pip install --upgrade pip
COPY ../../../../Test_Task_Innowise/test_task_inn/test_task_inn/requirements.txt .
RUN pip install -r requirements.txt

# копируем содержимое текущей папки в контейнер
COPY ../build /usr/src/app
