# Gunicorn configuration for Horilla-HR
# This file provides advanced configuration options for the WSGI server

import multiprocessing
import os

# Bind settings
bind = f"0.0.0.0:{os.environ.get('PORT', '8000')}"
host = "0.0.0.0"
port = int(os.environ.get("PORT", "8000"))

# Worker settings.
# The old default (2 * CPU + 1, cap 8) is a web-scale formula. On a 4-core
# VPS that is 8 full Django processes, each holding pandas + spaCy, which
# lands around 2GB idle. An HR team does not need that. Two gthread workers
# (8 concurrent requests) is enough; raise GUNICORN_WORKERS when you scale.
def _default_workers():
    configured = os.environ.get("GUNICORN_WORKERS", "").strip()
    if configured:
        return int(configured)
    return 2


workers = _default_workers()
worker_class = "gthread"
threads = int(os.environ.get("GUNICORN_THREADS", "4"))
worker_connections = 1000
max_requests = 1000
max_requests_jitter = 50
# preload_app is disabled with gthread workers to avoid ORM connection issues
preload_app = False

# Timeout settings
timeout = 120
keepalive = 5

# Logging
accesslog = "-"
errorlog = "-"
loglevel = os.environ.get("GUNICORN_LOG_LEVEL", "info")
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(D)s'

# Process naming
proc_name = "horilla-hrms"

# Server mechanics
pidfile = "/tmp/gunicorn.pid"
user = None  # Run as current user in container
group = None
tmp_upload_dir = None

# Development settings
reload = os.environ.get("GUNICORN_RELOAD", "false").lower() == "true"

# SSL settings (if needed)
# ssl_keyfile = os.environ.get('SSL_KEYFILE')
# ssl_certfile = os.environ.get('SSL_CERTFILE')
