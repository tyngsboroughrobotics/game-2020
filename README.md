# Tyngsborough Robotics Botball Game

<p align="center">
  <img src="https://i.postimg.cc/3NZfHT1n/THS-Robotics-Logo-Dual.png" height=240>
</p>

This repository holds the code for the Tyngsborough High School Robotics team's Botball game strategy.

We developed and are using the [Botball for Python](botball) library to write our code. The library is open source and we encourage other teams to use it and contribute!

## Viewing and using our code

The code in this repository contains *our team's code* for *our strategy* in the competition. While other teams may use it for guidance and inspiration, it would be cheating and against the spirit of the game to directly use our code for your team's robots. Therefore there are some conditions attached to the use of this repository, which you can read [here](LICENSE).

## Setup

### Windows

Press the Windows key on your keyboard and then type "cmd". Then click the "run as administrator" button on the right side underneath the icon. Click "Yes" when the prompt appears. Then copy and paste this code, and press Enter:

```batch
powershell iex ((New-Object System.Net.WebClient).DownloadString('https://raw.githubusercontent.com/tyngsboroughrobotics/game/master/setup-windows.ps1'))
```

### Mac

Press <kbd>Cmd</kbd><kbd>Space</kbd> on your keyboard and then type "Terminal", and press Return. Then copy and paste this code, and press Enter:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/tyngsboroughrobotics/game/master/setup-macos.sh)"
```

You will have to enter your password — when you type it nothing will appear, but it's still being entered. Just press Return when you finish.

## Running on your Wombat

Connect to your Wombat's WiFi network and run the `run_on_robot.py` script on your computer. The contents of the repository will be zipped, sent over WiFi to the robot, and executed.

To change the configuration (including the IP address and password of the Wombat), edit `run_on_robot.py`.

If you're using VSCode as an editor, you can also run the "Run on Robot" task from the run/debug pane.

## Contributing

We welcome all contributions to [Botball for Python](botball) — feel free to submit an issue or pull request!
