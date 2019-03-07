# Use an official Python runtime as a parent image
FROM python:3.7

# Set environment varibles
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE core.settings.prod

# Update base image and clean it
RUN apt-get update && apt-get autoremove --purge && apt-get clean

# Install any needed packages specified in requirements
RUN mkdir -p /tmp/requirements/
COPY ./requirements/base.txt /tmp/requirements/base.txt
COPY ./requirements/prod.txt /tmp/requirements/prod.txt

RUN pip install --trusted-host pypi.org --no-cache-dir --upgrade pip
RUN pip install --trusted-host pypi.org --no-cache-dir -r /tmp/requirements/prod.txt

# Add directories
RUN mkdir -p /srv/semkov/src/
RUN mkdir -p /srv/semkov/static/
RUN mkdir -p /var/log/semkov/

# Get app from repo
WORKDIR /srv/semkov/src/
RUN git init
RUN git remote add origin https://manti_by@bitbucket.org/manti_by/semkov.git
RUN git pull origin master

# Add wagtail system user
RUN useradd wagtail
RUN chown -R wagtail /srv/semkov/
RUN chown -R wagtail /var/log/semkov/
USER wagtail

# Run gunicorn
EXPOSE 8898
WORKDIR /srv/semkov/src/app/

# Run
CMD exec gunicorn core.wsgi:application --bind 0.0.0.0:8898 --workers 2
