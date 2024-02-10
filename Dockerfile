FROM python:3.12.1-slim-bullseye as base

COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


FROM python:3.12.1-slim-bullseye as build

RUN apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0

COPY --from=base /usr/local/lib/python3.12/site-packages/ /usr/local/lib/python3.12/site-packages/
COPY --from=base /usr/local/bin/ /usr/local/bin/

RUN mkdir -p /app
COPY . /app
WORKDIR /app/

EXPOSE 5000

CMD ["python", "main.py"]
ENV prometheus_multiproc_dir /tmp
ENV PYTHONBUFFERED 1