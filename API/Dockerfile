FROM python:3.9

EXPOSE 8000

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt 

COPY script.py script.py

CMD uvicorn script:app --host 0.0.0.0