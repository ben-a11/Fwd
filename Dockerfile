FROM python:3.9.4

WORKDIR /app

COPY requirements.txt /app/

RUN pip3 install -r requirements.txt

COPY . /app

#def cmd

CMD python3 main.py
