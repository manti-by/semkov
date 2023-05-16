FROM python:3.11-slim

# Add directories
RUN mkdir -p /srv/semkov/src/ && \
    mkdir -p /var/lib/semkov/static/ && \
    mkdir -p /var/lib/semkov/media/ && \
    mkdir -p /var/log/semkov/

# Install any needed packages specified in requirements
COPY requirements.txt /tmp/requirements.txt
RUN pip install --trusted-host pypi.org --no-cache-dir -r /tmp/requirements.txt

# Add manti system user
RUN useradd -m -s /bin/bash -d /home/manti manti && \
    mkdir -p /srv/semkov/src/ /var/lib/semkov/static/ /var/lib/semkov/media/ /var/log/semkov/ && \
    chown -R manti:manti /srv/semkov/src/ /var/lib/semkov/ /var/log/semkov/

# Select user, set working directory and run server
USER manti
WORKDIR /srv/semkov/src/
CMD python manage.py runserver
