# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
ENV GOOGLE_APPLICATION_CREDENTIALS="service_account.json"
ENV TWILIO_ACCOUNT_SID='ACdb0749096a5c2ee4b61459b3a1ce6ea9'
ENV TWILIO_AUTH_TOKEN='9c8f5b81948f21c82f3175b436de1367'
ENV TWILIO_PHONE='+12693672928'
ENV RECEIVER_PHONE='+14088052770'
WORKDIR /spreadsheet
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . . 
#CMD [ "python3", "./spreadsheet.py"]
