from __future__ import(absolute_import,division,print_function)
from ansible.module_utils.basic import AnsibleModule
import psutil

def main():
    argument_spec = {}
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True
    )

    result = {}
    changed = False

    result['cpu_load'] = psutil.cpu_percent(interval=1)
    result['memory_usage']=psutil.virtual_memory().percent
    result['disk_usage']=psutil.disk_usage('/').percent

    module.exit_json(changed=changed,**result)


if __name__ == '__main__':
    main()

    
