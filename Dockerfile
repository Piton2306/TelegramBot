FROM python:3.12.3

WORKDIR /usr/src/app

COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY file/logs/my_log_parsing.log file/logs/my_log_parsing.log
COPY file/logs/telegram.log file/logs/telegram.log
COPY file/dollar_exchange_rate.txt file/dollar_exchange_rate.txt
COPY database_parser_dollars.db database_parser_dollars.db
COPY parsing_rub_dollar.py parsing_rub_dollar.py
COPY file file
COPY telegram.py telegram.py
COPY sql.py sql.py
COPY logs.py logs.py
COPY main.py main.py

#CMD [ "python", "./main.py" ]
CMD [ "python", "./parsing_rub_dollar.py" ]