from __future__ import(absolute_import,division,print_function)
from ansible.module_utils.basic import AnsibleModule
import psutil
import logging
import requests

def main():
    argument_spec = {
        'log_path': {'required':True,'type':'str'}
    }
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True
    )
    log_path=module.params['log_path']
    result = {}
    changed = False

    cpu_load =  psutil.cpu_percent(interval=1)
    memroy_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent

    logging.basicConfig(filename=log_path,filemode='w',level=logging.DEBUG)
    logger = logging.getLogger('sample-logger')
    message = f"load: {cpu_load}, mem: {memroy_usage}, disk: {disk_usage}"
    logger.info(message)

    payload = {'metrics': message}
    r = requests.post('http://172.20.0.115:5000/metrics',json=payload)

    if r.status_code==200:
        pass
    result['cpu_load'] = cpu_load
    result['memory_usage']= memroy_usage
    result['disk_usage']=disk_usage

    module.exit_json(changed=changed,**result)


if __name__ == '__main__':
    main()

    
