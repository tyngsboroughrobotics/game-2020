import sys; sys.path.insert(0, "/home/root/Documents/KISS/Default User/botball-game/_botball_build")

from botball.core.helpers.choose_game_procedure import RobotConfig

if __name__ == "__main__":
    print("GETTING CONFIG")

    config = RobotConfig()

    print("IMPORTING PROCEDURE")

    if config.robot_type == "demobot":
        from src.demobot_procedure import procedure
    else:
        from src.create_procedure import procedure

    print("RUNNING PROCEDURE")

    procedure.run(
        debug=config.debug_enabled
    )
