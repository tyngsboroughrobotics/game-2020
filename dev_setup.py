'''
Script to install all the necessary developer tools and programs on the user's
computer.
'''

import os
import sys
import platform

def cmd(command):
    if '--debug' in sys.argv:
        print(command)

    if '--dry-run' not in sys.argv:
        os.system(command)

if platform.system() not in ['Windows', 'Darwin']:
    print('Sorry, you need to be running on Windows or macOS.')
    exit(1)

print('👉  Ready to install! Make sure you have administrator priveliges. Press ENTER to continue')
input()

if platform.system() == 'Windows':
    print('\n➡️  Install Chocolatey...\n')
    cmd('powershell')
    cmd('Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString(\'https://chocolatey.org/install.ps1\'))')
    cmd('exit')
    cmd('cmd') # open new terminal to reflect changes

    print('\n➡️  Install Git...\n')
    cmd('choco install git -params \'"/GitAndUnixToolsOnPath"\'')

    print('\n➡️  Install OpenSSH...\n')
    cmd('choco install openssh --pre')

    print('\n➡️  Install Python...\n')
    cmd('choco install python')

    print('\n➡️  Install VSCode...\n')
    cmd('choco install vscode')

    print('\n➡️  Install GitHub Desktop...\n')
    cmd('choco install github-desktop')
else:
    print('\n➡️  Install Homebrew...\n')
    cmd('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"')
    cmd('$SHELL') # open new terminal to reflect changes

    print('\n➡️  Install Git...\n')
    cmd('brew install git')

    print('\n➡️  Install Python...\n')
    cmd('brew install python')

    print('\n➡️  Install VSCode...\n')
    cmd('brew cask install visual-studio-code')

    print('\n➡️  Install GitHub Desktop...\n')
    cmd('brew cask install github-desktop')

print('\n✅  All set! Now just clone the project and open it in VSCode!')
