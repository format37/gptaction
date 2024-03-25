uvicorn app:app \
    --port 8080 \
    --host 0.0.0.0 \
    --ssl-certfile /etc/letsencrypt/live/rtlm.info/fullchain.pem \
    --ssl-keyfile /etc/letsencrypt/live/rtlm.info/privkey.pem \
    --reload \
    --workers 1
