FROM ubuntu:jammy

COPY cron/jobs cron_jobs

RUN apt update && apt -y install cron
RUN crontab cron_jobs
