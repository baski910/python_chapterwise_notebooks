from ansible.module_utils.basic import AnsibleModule
#import os
import subprocess

def main():
    argument_spec = {
        'scale': {'required': True, 'type':'str'}
    }

    module = AnsibleModule(
        argument_spec= argument_spec,
        supports_check_mode=True
    )

    timescale = module.params['scale']

    result={}
    changed = False

    #os.system('cat /proc/uptime')
    p = subprocess.Popen('uptime',stdout=subprocess.PIPE)
    m = subprocess.run(['awk','{print $3,$4}'],stdin=p.stdout,stdout=subprocess.PIPE,text=True)
    result['uptime'] = m.stdout
    #with(open('/proc/uptime')) as f:
    #    values = f.read().split()[0]
    #
    #    if timescale == "hour":
    #        result['uptime'] = float(values)/3600
    #    elif timescale == "minute":
    #        result["uptime"] = float(values)/60
    #    else:
    #        result["uptime"] = float(values)
    
    module.exit_json(changed=changed,**result)

if __name__ == '__main__':
    main()
