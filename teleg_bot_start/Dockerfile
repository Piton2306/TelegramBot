FROM python:3.12.3

WORKDIR /usr/src/app

COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN rm -rf /etc/localtime
RUN ln -s /usr/share/zoneinfo/Europe/Moscow /etc/localtime
RUN echo "Europe/Moscow" > /etc/timezone
COPY sql_postgress.py sql_postgress.py
COPY telegram.py telegram.py
#CMD [ "python", "./main.py" ]
CMD [ "python", "./telegram.py" ]

#docker build -t name-image .  Создание image