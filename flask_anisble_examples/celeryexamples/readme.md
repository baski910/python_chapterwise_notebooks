# pre-requisite<br>
sudo apt install redis<br>
pip install celery redis<br>

celery -A tasks worker --loglevel=info<br>


