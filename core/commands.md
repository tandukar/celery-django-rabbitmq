### To install rabbit mq (github codespace)
```bash
sudo apt update
```
```bash
sudo apt install rabbitmq-server
```
### To start rabbit mq
```bash
sudo service rabbitmq-server start
```
### To start celery worker
```bash
celery -A core worker -l info
```
```bash
celery -A core worker -l info --pool=solo
```
### Flower
```bash
pip install flower
```
### start flower
```bash
flower -A core --port-5555
```
