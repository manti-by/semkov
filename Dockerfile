FROM python:3.13-slim

RUN mkdir -p /srv/app/src/ /var/lib/app/static/ /var/lib/app/media/ /var/lib/app/data/ /var/log/app/
RUN useradd -m -s /bin/bash -d /home/manti manti && \
    chown -R manti:manti /srv/app/src/ /var/lib/app/ /var/log/app/

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv
COPY requirements.txt /tmp/requirements.txt
RUN uv pip install --system --no-cache-dir --requirement /tmp/requirements.txt

USER manti
WORKDIR /srv/app/src/
CMD ["gunicorn", "--timeout", "60", "--log-level", "warning", "--bind", "127.0.0.1:8000", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "semkov.asgi:application"]
