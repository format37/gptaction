uvicorn app:app \
    --port 8080 \
    --host 0.0.0.0 \
    --ssl-certfile fullchain.pem \
    --ssl-keyfile privkey.pem \
    --reload \
    --workers 1
