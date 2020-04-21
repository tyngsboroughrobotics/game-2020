# Install chocolatey
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
refreshenv

# Install git
choco install -y git -params '"/GitAndUnixToolsOnPath"'

# Install 7zip
choco install -y 7zip

# Install python
choco install -y python

# Install vscode
choco install -y vscode

# Install github desktop
choco install -y github-desktop

# Install python dependencies
pip install fabric
