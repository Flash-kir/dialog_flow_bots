# syntax=docker/dockerfile:1

FROM python:3.9-slim-bullseye
WORKDIR /app
COPY key.json .
COPY dialog_flow_utils.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY bot_vk.py .
COPY bot_tm.py .
RUN apt-get update
RUN apt-get install -y apt-transport-https ca-certificates gnupg curl sudo
RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg  add - && apt-get update -y && apt-get install google-cloud-cli -y
RUN gcloud auth activate-service-account --key-file=/app/key.json
RUN gcloud init
RUN export GOOGLE_APPLICATION_CREDENTIALS=/app/key.json
CMD ["python", "bot_vk.py"]