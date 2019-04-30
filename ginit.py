# Gunicorn configuration file in staging/production
bind = '0.0.0.0:8000'
WORKER_PROCESSES = 1

timeout = 120
workers = WORKER_PROCESSES
loglevel = 'info'
accesslog = '-'
errorlog = '-'
limit_request_field_size = 0
preload_app = True
