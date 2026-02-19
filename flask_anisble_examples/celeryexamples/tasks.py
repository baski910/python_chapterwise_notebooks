from celery import Celery
import ansible_runner
import os

celery_app = Celery('tasks', broker='redis://localhost:6379/0',backend='redis://localhost:6379/0')

@celery_app.task(ignore_result=False)
def run_ansible_playbook(playbook_path, inventory_path):
    # Run ansible-runner
    inv_path = os.path.join(os.getcwd(),f"project2/inventory/{inventory_path}")
    r = ansible_runner.run(private_data_dir='./project2', playbook=playbook_path, inventory=inv_path)
    return {"status": r.status,"stats":r.stats, "rc": r.rc}
