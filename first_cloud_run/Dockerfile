FROM python:3.10

COPY . ./

RUN python3.10 -m pip install pip
RUN apt-get update && apt-get install -y \
        python3-distutils \
        python3-setuptools

RUN python3.10 -m pip install pip --upgrade pip
RUN python3.10 -m pip install -r requirements.txt

CMD exec python3.10 app.py --host 0.0.0.0 --port 8080