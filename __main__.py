import sys; sys.path.insert(0, "/home/root/Documents/KISS/Default User/botball-game/_botball_build")

from botball.wallaby import shut_down_in
from botball.core.helpers.choose_game_procedure import RobotConfig

from threading import Thread

if __name__ == "__main__":
    def stop_program_listener():
        print("@@ Press [ENTER] to stop the program. @@")
        raw_input() # wait for the user to press a key
        print("@@ Stopping program. @@")
        shut_down_in(0)

    def run_procedures():
        config = RobotConfig()

        if config.robot_type == "demobot":
            from src.demobot_procedure import procedure
        else:
            from src.create_procedure import procedure

        procedure.run(debug=config.debug_enabled)

    Thread(target=stop_program_listener).start()
    Thread(target=run_procedures).start()
