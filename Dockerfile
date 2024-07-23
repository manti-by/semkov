FROM python:3.12-slim

# Add directories
RUN mkdir -p /srv/app/src/ && \
    mkdir -p /var/lib/app/static/ && \
    mkdir -p /var/lib/app/media/ && \
    mkdir -p /var/lib/app/data/ && \
    mkdir -p /var/log/app/

# Install any needed packages specified in requirements
COPY requirements.txt /tmp/requirements.txt
RUN pip install --trusted-host pypi.org --no-cache-dir -r /tmp/requirements.txt

# Add manti system user
RUN useradd -m -s /bin/bash -d /home/manti manti && \
    chown -R manti:manti /srv/app/src/ /var/lib/app/ /var/log/app/

# Select user, set working directory and run server
USER manti
WORKDIR /srv/app/src/
CMD ["python", "manage.py", "runserver"]
