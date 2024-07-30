FROM python:3.11.4-slim
LABEL maintainer="Arnab <raj713335@gmail.com>"

RUN apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0 ffmpeg build-essential libpq-dev
RUN apt-get update & apt-get install sqlite3
RUN pip install pysqlite3-binary
RUN pip install psycopg2-binary

COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /app
COPY . /app
WORKDIR /app/

EXPOSE 5000

#CMD ["/usr/bin/supervisord"]
CMD ["python", "main.py"]

# Corrected ENV format
ENV PYTHONBUFFERED=1
