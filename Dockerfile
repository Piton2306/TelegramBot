FROM python:3.12.3

WORKDIR /usr/src/app

COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN rm -rf /etc/localtime
RUN ln -s /usr/share/zoneinfo/Europe/Moscow /etc/localtime
RUN echo "Europe/Moscow" > /etc/timezone
COPY /file /file
COPY .gitignore .gitignore
COPY sql_postgress.py sql_postgress.py
COPY database_parser_dollars.db database_parser_dollars.db
COPY parsing_rub_dollar.py  parsing_rub_dollar.py
#CMD [ "python", "./main.py" ]
CMD [ "python", "./parsing_rub_dollar.py" ]

#docker build -t name-image .  Создание image