FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN apt-get update -y && apt-get install -y

COPY . .

CMD ["echo", "you need to override this command"]
