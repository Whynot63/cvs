import os
import sys
import shutil

path = os.getcwd()
command = sys.argv[1]

if command == 'init':
    project_name = sys.argv[2]
    os.mkdir(project_name)
    os.chdir('mycvs')
    version = open('info.txt', 'w')
    version.write('0')
    version.close()
elif command == 'commit':
    version = int(open('info.txt', 'r').read()) + 1
    os.mkdir('v' + str(version))
    shutil.copyfile(path + '/main.py', path + '/v' + str(version) + '/main.py')
    open('info.txt', 'w').write(str(version))
elif command == 'checkout':
    checkout_version = sys.argv[2]
    shutil.copyfile(path + '/' + checkout_version + '/main.py', path + '/main.py')
