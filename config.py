from fabric.api import *

class FabConfig(object):
    
    def __init__(self, config):
        pass
    
    
    
    web_servers = {
        'nginx' : {
            'commands' : {
                'restart' : 'restart',
                'start' : 'start',
                'stop' : 'stop'
            }
        }
    }
  
    def __initialize__(self, config):
        pass

    def check_config(deploy_to, config):
        if(exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), folders['config'], deploy_to, folders['config_dir'], config)) == False):
            abort(Template(messages['config_missing']).substitute(dict(deploy_to = deploy_to, config = config)))

    def check_script(deploy_to, script):
        if(exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), folders['config'], deploy_to, folders['scripts_dir'], script)) == False):
            abort(Template(messages['shell_script_missing']).substitute(dict(deploy_to = deploy_to, shell_script = script)))

    def check_setup(deploy_to = None):
        if(deploy_envs.has_key(deploy_to) == False):
            abort('Deployment environment "%s" is not defined' % deploy_to)

        check_script(deploy_to, configs['gunicorn']['script'])
        check_config(deploy_to, configs['supervisor']['config'])
        check_config(deploy_to, configs['nginx']['config'])

    # Web server control helper
    def web_server_ctl(web_server = None, web_server_command = None):
        if(web_servers.has_key(web_server) == False):
            abort('Invalid web server "%s"' % web_server)
        elif(web_servers[web_server]['commands'].has_key(web_server_command) == False):
            abort('Invalid "%s" command "%s", try {%s}' % (web_server, web_server_command, '|'.join(web_servers[web_server]['commands'])))
        else:
            message('WEB SERVER', 'Running "/etc/init.d/%s %s"' % (web_server, web_server_command))
            sudo('/etc/init.d/%s %s' % (web_server, web_server_command))

    # Update the application code and restart application
    def update_app():
        message('CODE', 'Updating to head')

    # Deploy our application
    def deploy():
        web_server_ctl('nginx', 'start')

    # Rollback the application code and restart application.
    def rollback():
        pass