FROM python:3.9-slim

# Install necessary system packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends git-core gcc build-essential && \
    rm -rf /var/lib/apt/lists/*

# Add directories
RUN mkdir -p /srv/semkov/src/ && \
    mkdir -p /srv/semkov/static/ && \
    mkdir -p /srv/semkov/media/ && \
    mkdir -p /var/log/semkov/

# Install any needed packages specified in requirements
COPY requirements/base.txt /tmp/base.txt
COPY requirements/prod.txt /tmp/prod.txt
RUN pip install --trusted-host pypi.org --no-cache-dir --upgrade pip && \
    pip install --trusted-host pypi.org --no-cache-dir -r /tmp/prod.txt

# Remove system packages after use
RUN apt-get autoremove -y --purge git-core gcc build-essential && \
    apt-get clean -y

# Add wagtail system user
RUN useradd -m -s /bin/bash -d /home/manti manti && \
    mkdir -p /srv/semkov/src/ /var/lib/semkov/static/ /var/lib/semkov/media/ /var/log/semkov/ && \
    chown -R manti:manti /srv/semkov/src/ /var/lib/semkov/ /var/log/semkov/

# Select user, set working directory and run server
USER manti
WORKDIR /srv/semkov/src/
CMD python manage.py runserver
