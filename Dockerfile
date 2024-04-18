FROM python:3.11

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

#
COPY ./main.py /code/
COPY ./src /code/src

#
CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8888"]
