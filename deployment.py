class Deployment(object):
    
    def __init__(self, config):
        self.config = config
    
    def setup(deploy_to = None):
        if(confirm('Are you sure you want to setup the server', default = False)):
            message('SETUP','Preparing server for deployment')

            # Copy templated shell script to $deploy_dir/shared/scripts
            unicorn_shell_script = Template(file.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), folders['config'], deploy_to, folders['scripts_dir'], configs['gunicorn']['script']), 'r').substitute(dict(deploy_dir = deploy_to, app_name = app_name, num_workers = configs['gunicorn']['workers']))
            # Copy any other scripts to $deploy_dir/shared/scripts

            # Copy database settings to $deploy_dir/shared

            # Create $deploy_dir/releases

            # Copy web server config but don't link it up yet
        else:
            abort(message('SETUP', 'Setup was cancelled by user'))