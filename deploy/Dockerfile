# Use an official Python runtime as a parent image
FROM python:3.7-slim

# Install necessary system packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends git gcc linux-headers-generic

# Add directories
RUN mkdir -p /srv/semkov/src/ && \
    mkdir -p /srv/semkov/static/ && \
    mkdir -p /var/log/semkov/

# Install any needed packages specified in requirements
COPY requirements/base.txt /tmp/base.txt
COPY requirements/prod.txt /tmp/prod.txt
RUN pip install --trusted-host pypi.org --no-cache-dir --upgrade pip && \
    pip install --trusted-host pypi.org --no-cache-dir -r /tmp/prod.txt

# Remove system packages after use
RUN apt-get purge -y --auto-remove git gcc linux-headers-generic

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
