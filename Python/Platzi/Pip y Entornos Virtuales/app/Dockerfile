FROM python:3.8

WORKDIR /app
COPY "Python/Platzi/Pip y Entornos Virtuales/app/requirements.txt" '/app/requirements.txt'

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app/

CMD bash -c "while true; do sleep 1; done"