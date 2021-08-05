FROM python:3.9

COPY . ./FASTMLOPS

WORKDIR ./FASTMLOPS

RUN pip install -r requirements.txt

