# Use an official Python runtime as a parent image
FROM python:3.7

# Set environment varibles
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE core.settings.prod

# Update base image and clean it
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get autoremove --purge && \
    apt-get clean

# Add directories
RUN mkdir -p /srv/semkov/src/ && \
    mkdir -p /srv/semkov/static/ && \
    mkdir -p /var/log/semkov/

# Get app from repo
WORKDIR /srv/semkov/src/
RUN git init && \
    git remote add origin https://manti_by@bitbucket.org/manti_by/semkov.git && \
    git pull origin master

# Install any needed packages specified in requirements
RUN pip install --trusted-host pypi.org --no-cache-dir --upgrade pip && \
    pip install --trusted-host pypi.org --no-cache-dir -r deploy/requirements/prod.txt

# Add wagtail system user
RUN useradd wagtail -d /home/wagtail -m
RUN chown -R wagtail /home/wagtail/ && \
    chown -R wagtail /srv/semkov/ && \
    chown -R wagtail /var/log/semkov/
USER wagtail

# Run gunicorn
EXPOSE 8898
WORKDIR /srv/semkov/src/app/

# Run
CMD exec gunicorn core.wsgi:application --bind 0.0.0.0:8898 --workers 2
