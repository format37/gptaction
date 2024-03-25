# gptaction
Chat-GPT actions server example
#### Installation
* Copy your cert files locally
```
sudo cp /etc/letsencrypt/live/rtlm.info/fullchain.pem ./webhook_cert.pem
sudo cp /etc/letsencrypt/live/rtlm.info/privkey.pem ./webhook_pkey.pem
```
* Open the 8080 https port on your firewall
```
git clone https://github.com/format37/gptaction.git
cd gptaction
python3 -m pip install -r requirements.txt
sh run.sh
```