# pre-requisite<br>
sudo apt install redis<br>
pip install celery redis<br>

celery -A tasks worker --loglevel=info<br>

curl -X POST -H 'Content-Type: application/json' -d '{"playbook":"playbook.yml","inventory":"hosts"}' http://localhost:5000/run-playbook


