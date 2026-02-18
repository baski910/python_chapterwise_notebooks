from ansible.module_utils.basic import AnsibleModule

def main():
    argument_spec = {
        'name': {'required': True,'type':'str'},
        'new': {'required': False,'type': 'bool','default': False}
    }

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode= True
    )

    name = module.params['name']
    new_state = module.params['new']

    result = {}
    changed = False
    ### here the 
    if new_state:
        result['message'] = f"Hello {name}! state changed"
        changed = True
    else:
        result['message'] = f"Hello {name}!"

    module.exit_json(changed=changed, **result)

if __name__ == '__main__':
    main()
