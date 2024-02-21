FROM ubuntu:jammy

COPY . /pi_scan
WORKDIR /pi_scan

RUN apt update && apt -y install nano python3 python3-pip libsane libsane-hpaio sane-utils
RUN pip3 install -r requirements.txt

RUN chmod +x scripts/entrypoint.sh