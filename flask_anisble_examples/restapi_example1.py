from flask import Flask, request, jsonify
import threading
import ansible_runner
import os

app = Flask(__name__)

# In-memory storage for job statuses and outputs (for demonstration)
job_status = {}

def run_playbook_task(job_id, playbook_path, extra_vars):
    """Function to run ansible-runner in a separate thread."""
    try:
        # Define the working directory for ansible-runner
        # Ensure this directory (e.g., 'playbook_data') exists and contains
        # your inventory, playbooks, etc.
        #private_data_dir = os.path.join(os.getcwd(), 'playbook_data')
        data_dir = os.path.join(os.getcwd(), 'project1')
        
        # Run the playbook using the ansible_runner Python interface
        r = ansible_runner.run(
            private_data_dir=data_dir,
            playbook=playbook_path,
            extravars={
                'ansible_become': True,
                'ansible_become_method': 'sudo',
                'ansible_become_user': 'student',
                'ansible_become_pass': 'P@%%w0rd@26'
            json_mode=True
        )
        job_status[job_id]["status"] = r.status
        job_status[job_id]["artifacts"] = r.events
        job_status[job_id]["return_code"] = r.rc

    except Exception as e:
        job_status[job_id]["status"] = "failed"
        job_status[job_id]["error"] = str(e)
    
    finally:
        # Store the full stdout for later retrieval
        job_status[job_id]["stdout"] = r.stdout.read()


@app.route('/api/run_ansible', methods=['POST'])
def run_ansible():
    """Endpoint to trigger an Ansible playbook run."""
    data = request.get_json()
    playbook_name = data.get('playbook', 'site.yml')
    extra_vars = data.get('extra_vars', {})
    
    # Generate a unique job ID (in a real app, use a UUID or database ID)
    job_id = f"job_{len(job_status) + 1}"
    job_status[job_id] = {"status": "running", "stdout": "", "artifacts": None, "return_code": None}

    # Start the ansible-runner in a new thread
    thread = threading.Thread(target=run_playbook_task, args=(job_id, playbook_name, extra_vars))
    thread.start()

    return jsonify({"message": "Ansible playbook started", "job_id": job_id}), 202


@app.route('/api/status/<job_id>', methods=['GET'])
def get_status(job_id):
    """Endpoint to check the status of a running job."""
    status = job_status.get(job_id)
    if status:
        # Return a summarized status (don't return large artifacts here)
        summary = {
            "status": status["status"],
            "return_code": status["return_code"],
            "message": "Job details available via /api/output/<job_id>" if status["status"] != "running" else "Job is still running"
        }
        return jsonify(summary), 200
    return jsonify({"message": "Job not found"}), 404


@app.route('/api/output/<job_id>', methods=['GET'])
def get_output(job_id):
    """Endpoint to retrieve the full output of a completed job."""
    status = job_status.get(job_id)
    if status and status["status"] != "running":
        return jsonify({"job_id": job_id, "output": status.get("stdout", "N/A")}), 200
    elif status and status["status"] == "running":
        return jsonify({"message": "Job is still running. Check the status endpoint first."}), 200
    return jsonify({"message": "Job not found"}), 404

if __name__ == '__main__':
    # Create the directory required by ansible-runner if it doesn't exist
    if not os.path.exists('playbook_data'):
        os.makedirs('playbook_data')
    # Place your inventory in playbook_data/inventory, and playbooks in playbook_data/
    
    app.run(debug=True)
