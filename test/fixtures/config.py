config = {
    'app_name' : 'conferencepros',
    'deploy_environments' : {
        'staging' : {
            'host' : 'cp.crudmud.com',
            'app_group' : 'conferencepros',
            'app_user' : 'conferencepros',
            'deploy_dir' : '/home/conferencepros/app/',
            'services' : {
                'gunicorn' : {
                  'workers' : '2'
                },
                'nginx' : {
                  'workers' : '2'
                },
                'supervisor' : {
                  'email_admin' : 'yes'
                },
                'memcached' : {
                  'max_mem' : '1000M',
                }
            }
        }
    },
    'folders' : {
        'config' : 'deploy',
        'scripts_dir' : 'shell_scripts',
        'config_dir' : 'config'
    },
    'services' : {
        'gunicorn' : {
          'script' : 'gunicorn.sh'
        },
        'nginx' : {
          'config' : 'nginx.conf'
        },
        'supervisor' : {
          'config' : 'supervisor.conf'
        },
        'memcached' : {
          'config' : 'memcached.conf',
        }
    }
}