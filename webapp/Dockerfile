FROM python:3.10-buster

WORKDIR /home/webapp

COPY . /home/webapp

RUN pip install -e /home/webapp

CMD ["streamlit", "run", "webapp/__main__.py"]
