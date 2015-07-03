#### Here's a Flask app using Celery.

Startup command for flask:

```
NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program gunicorn app:app
```

Startup command for the Celery worker:

```
NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program celery -A tasks worker --loglevel=info
```

Command to start rabbimq:

```
/usr/local/sbin/rabbitmq-server
```