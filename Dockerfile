FROM python:3.9.13-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app


# here no command is given to run the app