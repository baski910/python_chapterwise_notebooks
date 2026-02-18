from celery import Celery
import ansible_runner
import os

celery_app = Celery('tasks', broker='redis://localhost:6379/0',backend='redis://localhost:6379/0')

@celery_app.task(ignore_result=False)
def run_ansible_playbook(playbook_path, inventory_path):
    # Run ansible-runner
    r = ansible_runner.run(private_data_dir='./project1', playbook=playbook_path, inventory=inventory_path)
    return {"status": r.status, "rc": r.rc}
