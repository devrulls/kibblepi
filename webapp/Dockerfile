FROM python:3.10-buster

COPY . /tmp

RUN pip install -e tmp/.[dev]

WORKDIR /home/webapp

CMD ["streamlit","run","__main__.py"]