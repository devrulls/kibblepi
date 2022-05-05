FROM python:3.10-buster

WORKDIR /home/webapp

COPY . /home/webapp

RUN pip install -e /home/webapp

EXPOSE 8501

ENTRYPOINT ["streamlit", "run"]
CMD ["webapp/__main__.py"]
