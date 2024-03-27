FROM ubuntu:jammy

RUN mkdir /cron_jobs
COPY cron/clear_gunicorn_logs /cron_jobs

RUN apt update && apt -y install cron
RUN crontab /cron_jobs/clear_gunicorn_logs
