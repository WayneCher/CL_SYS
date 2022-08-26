#-*- coding:utf-8 -*-

import argparse

def poll():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dispatcher-server',
                        help = 'dispatcher host:port,'\
                        'by default it uses localhost:8888',
                        default = 'localhost:8888',
                        action = 'store')
    parser.add_argument('repo',metavar = 'REPO', type = str,
                        help = 'path to the repository this will observe')
    args = parser.parser_args()
    dispatcher_host, dispatcher_port = args.dispatcher_server.split(':')

while True:
    try:
        subprocess.check_output(['./update_repo.sh',args.repo])
    except subprocess.CalledProcessError as e:
        raise Exception('Could not update and  check repository.' +
                        'Reason: %s'%e.output)
