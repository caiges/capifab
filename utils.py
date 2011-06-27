class Utils:
    
    MESSAGES = {
        'shell_script_missing' : 'Shell script "$shell_script" missing for "$deploy_to" environment should be defined in "%s"' % (os.path.join(folders['config'], folders['scripts_dir'], '')),
        'config_missing' : 'Config "$config" missing for "$deploy_to" environment should be defined in "%s"' % (os.path.join(folders['config'], folders['config_dir'], ''))
    }
    
    @classmethod        
    def message(context, msg):
        print(">> %s -- %s" % (context, Utils.MESSAGES[msg]))
        
        