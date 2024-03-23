 # Базовый образ
FROM python:3.8

# Установка зависимостей
COPY requirements.txt /PythonAppiumProject/requirements.txt
WORKDIR /PythonAppiumProject
RUN pip install -r requirements.txt

# Копирование приложения и тестов
COPY . /PythonAppiumProject

# Команда для запус тестов
CMD ["/bin/bash"]
