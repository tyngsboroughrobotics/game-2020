###     Configuration     ###

IP_ADDRESS = 'pi@192.168.125.1'
SSH_PASSWORD = 'wallaby'
ZIP_NAME = '.game.zip'
PROJECT_PATH = '/home/root/Documents/KISS/Default\\ User/botball-game'

###   End Configuration   ###

import os, sys, platform
from fabric import Connection

def cmd(command):
    os.system(command)

def clear():
    if platform.system() == 'Windows':
        cmd('cls')
    else:
        cmd('clear')

clear()

# Bundle the project into a .zip
print('Bundling project...\n')
cmd(f'rm {ZIP_NAME}')
if platform.system() == 'Windows':
    cmd(f'7z a -r {ZIP_NAME} . -xr"!*__pycache__*" -xr"!.*"')
else:
    cmd(f'zip -r {ZIP_NAME} . -x \\*__pycache__\\* -x .\\* -x .\\*/')

if '--build-only' in sys.argv:
    exit(0)

clear()

ssh = Connection(host=f'pi@{IP_ADDRESS}', connect_kwargs={'password': SSH_PASSWORD})

# Copy the .zip over to the robot
print('\nCopying project to robot...\n')
# delete existing files
ssh.run(f'rm -rf {PROJECT_PATH}/{ZIP_NAME}')
# copy zip file
ssh.upload(ZIP_NAME, f'{PROJECT_PATH}/{ZIP_NAME}')
# extract KISS files so the program can appear in the botui list
ssh.run(f'unzip {PROJECT_PATH}/{ZIP_NAME} \'bin/*\' -d {PROJECT_PATH}')
ssh.run(f'unzip {PROJECT_PATH}/{ZIP_NAME} \'botball-game.project.json\' -d {PROJECT_PATH}')

clear()

# Run the game on the robot
print('\nStarting game...\n')
ssh.run(f'python3 {PROJECT_PATH}/{ZIP_NAME}')
