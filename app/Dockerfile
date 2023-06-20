FROM python:latest

WORKDIR /app 

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app.py /app/

EXPOSE 5000

CMD [ "streamlit", "run", "app.py" ]

