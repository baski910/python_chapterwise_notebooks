from flask import Flask, request, jsonify
from celery.result import AsyncResult
from tasks import run_ansible_playbook
from tasks import celery_app

app = Flask(__name__)

@app.route('/run-playbook', methods=['POST'])
def trigger_playbook():
    data = request.json
    playbook = data.get('playbook')
    inventory = data.get('inventory')

    # Async call to Celery
    task = run_ansible_playbook.delay(playbook, inventory)
    return jsonify({"task_id": task.id, "status": "Queued"}), 202

@app.route("/status/<task_id>")
def get_status(task_id: str) -> dict[str, object]:
    #result = AsyncResult(task_id, app=current_app.extensions["celery"])
    result = AsyncResult(task_id,app=celery_app)
    return {
        "task_id": task_id,
        "status": result.status,
        "ready": result.ready(),
        "successful": result.successful(),
        "value": result.result if result.ready() else None,
    }

if __name__ == '__main__':
    app.run(debug=True)
