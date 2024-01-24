FROM python:3.10-slim-bullseye as base
COPY requirements.txt /
RUN python -m pip install --upgrade pip --no-cache-dir
RUN pip install -r requirements.txt --no-cache-dir

FROM base as app

COPY . /app
WORKDIR /app
CMD ["python", "main.py"]
EXPOSE 5000
