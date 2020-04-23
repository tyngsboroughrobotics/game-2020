###     Configuration     ###

IP_ADDRESS = '192.168.125.1'
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

ssh = Connection(IP_ADDRESS, user='pi', connect_kwargs={'password': SSH_PASSWORD})

# Copy the .zip over to the robot
print('\nCopying project to robot...\n')
# delete existing files
ssh.run(f'sudo rm -rf {PROJECT_PATH}', echo=True)
# copy zip file
ssh.run(f'sudo mkdir -p {PROJECT_PATH}', echo=True)
ssh.run(f'sudo chmod -R a+rwX {PROJECT_PATH}', echo=True)
scp_path = PROJECT_PATH.replace('\\ ', ' ')
if platform.system() == 'Windows':
    os.system(f'pscp -pw {SSH_PASSWORD} {ZIP_NAME} pi@{IP_ADDRESS}:\'"{scp_path}"\'')
else:
    import pexpect
    scp = pexpect.spawn(f'scp {ZIP_NAME} pi@{IP_ADDRESS}:\'"{scp_path}"\'')
    scp.expect('password:')
    scp.sendline(SSH_PASSWORD)
    scp.expect(pexpect.EOF)

# extract KISS files so the program can appear in the botui list
ssh.run(f'unzip {PROJECT_PATH}/{ZIP_NAME} \'bin/*\' -d {PROJECT_PATH}', echo=True)
ssh.run(f'unzip {PROJECT_PATH}/{ZIP_NAME} \'botball-game.project.json\' -d {PROJECT_PATH}', echo=True)

clear()

# Run the game on the robot
print('\nStarting game...\n')
ssh.run(f'source /home/pi/.botball && source {PROJECT_PATH}/bin/botball_user_program', echo=True)
