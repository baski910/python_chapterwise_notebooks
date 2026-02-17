from flask import Flask,request,render_template, jsonify
import ansible_runner
import threading
import os

app = Flask(__name__)

def run_playbook_task(playbook_path,become_pass,extravars):
    try:
        # Define the working directory for ansible-runner
        # Ensure this directory (e.g., 'playbook_data') exists and contains
        # your inventory, playbooks, etc.
        #private_data_dir = os.path.join(os.getcwd(), 'playbook_data')
        data_dir = os.path.join(os.getcwd(), 'project2')
    
    
        r = ansible_runner.run(
            private_data_dir=data_dir,
            playbook=playbook_path,
            extravars={
                'ansible_become': True,
                'ansible_become_method':'sudo',
                'ansible_become_user':'root',
                'ansible_become_pass':'P@%%w0rd@26'
            },
         
            json_mode=True
        )
   

    except Exception as e:
            #job_status[job_id]["status"] = "failed"
            #job_status[job_id]["error"] = str(e)
            print(str(e))
    finally:
            # Store the full stdout for later retrieval
            print(r.status)
            print(r.stdout.read())

@app.route('/') # http://127.0.0.1:5000
def index():
    return render_template("my.html")
    #return "<h1>helloworld</h1>"

@app.route('/showMessage',methods=['POST'])
def message():
    #data = request.get_json()
    playbook =  request.form['playbook']
    password = request.form['password']
    extra_vars = {}
    thread = threading.Thread(target=run_playbook_task, args=(playbook,password, extra_vars))
    thread.start()

    return jsonify({"message": "Ansible playbook completed"}), 202

    #return f"<h1>Playbook - {playbook} and Password = {password}</h1>"

if __name__ == "__main__":
    app.run()
